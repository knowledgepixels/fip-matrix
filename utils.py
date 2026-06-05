import re
import pandas as pd
import streamlit as st
from config import AVAILABLE_MAP, TBD_MAP

@st.cache_data(ttl=3600)
def load_and_prepare_data(url):
    df = pd.read_csv(url)
    df['c'] = df['c'].map(shorten_label)
    df['mapped_values'] = df.apply(map_relation_value, axis=1)
    return df

def shorten_label(value):
    # Most communities arrive as short labels (e.g. "indigeo"); some arrive as
    # full URIs (e.g. ".../ACTRIS-DC"). Reduce URIs to their last #/ segment.
    if isinstance(value, str) and '://' in value:
        return re.split(r'[#/]', value)[-1]
    return value

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
