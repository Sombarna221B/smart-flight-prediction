
import pandas as pd
import numpy as np
import re
from datetime import datetime

def parse_date_of_journey(val):
    return pd.to_datetime(val, dayfirst=True, errors='coerce')

def parse_duration_to_minutes(s):
    if pd.isna(s): return np.nan
    s = str(s).lower().strip()
    h = 0; m = 0
    m_h = re.search(r'(\d+)\s*h', s)
    if m_h: h = int(m_h.group(1))
    m_m = re.search(r'(\d+)\s*m', s)
    if m_m: m = int(m_m.group(1))
    if not m_h and not m_m:
        digits = re.findall(r'\d+', s)
        if digits:
            m = int(digits[0])
    return int(h*60 + m)

def parse_total_stops(s):
    if pd.isna(s): return np.nan
    s = str(s).lower().strip()
    if s in ['non-stop','non stop','nonstop','direct','none','0']:
        return 0
    m = re.search(r'(\d+)', s)
    if m: return int(m.group(1))
    return np.nan

def parse_hour(s):
    if pd.isna(s): return np.nan
    try:
        t = pd.to_datetime(s, errors='coerce')
        return t.hour if not pd.isna(t) else np.nan
    except:
        return np.nan

def preprocess_full_dataframe(df):
    df = df.copy()
    df['Journey_Date'] = df['Date_of_Journey'].apply(parse_date_of_journey)
    df['Journey_Day'] = df['Journey_Date'].dt.day
    df['Journey_Month'] = df['Journey_Date'].dt.month
    df['Journey_Weekday'] = df['Journey_Date'].dt.weekday
    df['Duration_min'] = df['Duration'].apply(parse_duration_to_minutes)
    df['Total_Stops_num'] = df['Total_Stops'].apply(parse_total_stops)
    df['Dep_Hour'] = df['Dep_Time'].apply(parse_hour)
    df['Arr_Hour'] = df['Arrival_Time'].apply(parse_hour)
    # numeric cleaning
    numeric_cols = ['Duration_min','Total_Stops_num','Dep_Hour','Arr_Hour','Journey_Day','Journey_Month','Journey_Weekday']
    for c in numeric_cols:
        df[c]=pd.to_numeric(df[c],errors='coerce')
    # drop incomplete rows for essential features
    df = df.dropna(subset=['Price','Duration_min','Total_Stops_num'])
    df['Total_Stops_num'] = df['Total_Stops_num'].astype(int)
    df['Duration_min'] = df['Duration_min'].astype(int)
    df['Dep_Hour'] = df['Dep_Hour'].fillna(-1).astype(int)
    df['Arr_Hour'] = df['Arr_Hour'].fillna(-1).astype(int)
    for c in ['Airline','Source','Destination','Additional_Info','Route']:
        if c in df.columns:
            df[c]=df[c].astype(str).str.strip()
    return df
