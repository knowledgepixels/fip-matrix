import pandas as pd
import streamlit as st
from config import AVAILABLE_MAP, TBD_MAP

@st.cache_data
def load_and_prepare_data(path):
    df = pd.read_csv(path)
    df['mapped_values'] = df.apply(map_relation_value, axis=1)
    return df

def map_relation_value(row):
    if row['resourcetype'] == 'https://w3id.org/fair/fip/terms/Available-FAIR-Enabling-Resource':
        return AVAILABLE_MAP.get(row['rel'], None)
    elif row['resourcetype'] == 'https://w3id.org/fair/fip/terms/FAIR-Enabling-Resource-to-be-Developed':
        return TBD_MAP.get(row['rel'], None)
    return None

@st.cache_data
def filter_data(df, fip_q=None, comms=None):
    filtered = df
    if fip_q:
        filtered = filtered[filtered['q'].isin(fip_q)]
    if comms:
        filtered = filtered[filtered['c'].isin(comms)]
    return filtered
