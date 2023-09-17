


import plotly.graph_objects as go

import pandas as pd
from datetime import datetime
def plot_stock(file_name):
    
    path = r''
    file_type = '.csv'

    df = pd.read_csv(path + file_name + file_type)

    fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                    open=df[file_name + '.Open'],
                    high=df[file_name + '.High'],
                    low=df[file_name + '.Low'],
                    close=df[file_name + '.Close'])])

    fig.show()