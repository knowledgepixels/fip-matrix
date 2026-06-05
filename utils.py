import pandas as pd
import streamlit as st
from config import AVAILABLE_MAP, TBD_MAP

@st.cache_data(ttl=3600)
def load_and_prepare_data(url):
    df = pd.read_csv(url)
    df['mapped_values'] = df.apply(map_relation_value, axis=1)
    return df

def map_relation_value(row):
    if row['resourcetype'] == 'https://w3id.org/fair/fip/terms/Available-FAIR-Enabling-Resource':
        return AVAILABLE_MAP.get(row['rel'], None)
    elif row['resourcetype'] == 'https://w3id.org/fair/fip/terms/FAIR-Enabling-Resource-to-be-Developed':
        return TBD_MAP.get(row['rel'], None)
    return None

@st.cache_data
def filter_data(df, fip_q=None, comms=None, fips=None):
    filtered = df
    if fip_q:
        filtered = filtered[filtered['q'].isin(fip_q)]
    if comms:
        filtered = filtered[filtered['c'].isin(comms)]
    if fips:
        filtered = filtered[filtered['fip_title'].isin(fips)]
    return filtered

@st.cache_data
def latest_fip_per_community(df):
    """Return the most recent fip_title for each community (by declaration date)."""
    t = df.dropna(subset=['fip_title', 'date'])
    if t.empty:
        return []
    fip_dates = t.groupby(['c', 'fip_title'], as_index=False)['date'].max()
    latest = fip_dates.sort_values('date').groupby('c', as_index=False).tail(1)
    return sorted(latest['fip_title'].unique())
