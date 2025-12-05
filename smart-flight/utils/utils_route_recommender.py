
import pandas as pd
import numpy as np

def recommend_best_route(processed_df, source, destination, max_options=5):
    df = processed_df[(processed_df['Source']==source) & (processed_df['Destination']==destination)].copy()
    if df.empty:
        return []
    grouped = df.groupby(['Total_Stops_num','Duration_min']).agg(
        Price=('Price','mean'),
        Duration=('Duration_min','first'),
        Stops=('Total_Stops_num','first')).reset_index()
    # normalize
    def normalize(s): return (s - s.min())/(s.max()-s.min()+1e-9)
    grouped['p_norm'] = normalize(grouped['Price'])
    grouped['d_norm'] = normalize(grouped['Duration_min'])
    grouped['s_norm'] = normalize(grouped['Total_Stops_num'])
    grouped['score'] = 0.5*grouped['p_norm'] + 0.3*grouped['d_norm'] + 0.2*grouped['s_norm']
    ranked = grouped.sort_values('score').head(1)
    results = ranked.to_dict(orient='records')
    return results
