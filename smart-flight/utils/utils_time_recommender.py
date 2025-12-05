
import pandas as pd

weekday_names = {
    0: "Monday", 1: "Tuesday", 2: "Wednesday",
    3: "Thursday", 4: "Friday", 5: "Saturday", 6: "Sunday"
}

month_names = {
    1: "January", 2: "February", 3: "March", 4: "April",
    5: "May", 6: "June", 7: "July", 8: "August",
    9: "September", 10: "October", 11: "November", 12: "December"
}

def best_time_to_buy(processed_df, source=None, destination=None, top_n=3):
    df = processed_df.copy()
    if source: df = df[df['Source']==source]
    if destination: df = df[df['Destination']==destination]
    months = (df.groupby('Journey_Month')['Price'].agg(['mean','count']).sort_values('mean').head(top_n).reset_index())
    months['Journey_Month'] = months['Journey_Month'].map(month_names)
    weekdays = (df.groupby('Journey_Weekday')['Price'].agg(['mean','count']).sort_values('mean').head(top_n).reset_index())
    weekdays['Journey_Weekday'] = weekdays['Journey_Weekday'].map(weekday_names)    

    return {
        'top_months': months.to_dict(orient='records'),
        'top_weekdays': weekdays.to_dict(orient='records'),
        'advice': 'Consider booking 2-3 weeks before travel.; Weekdays like Tuesdays/Wednesdays are often cheaper.'
    }
