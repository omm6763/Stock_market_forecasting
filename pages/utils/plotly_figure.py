import plotly.graph_objects as go
import dateutil
import pandas_ta as pta
import datetime

def plotly_table(dataframe):
    headerColor='grey'
    rowEvenColor='#f8fafd'
    rowOddColor='#e1efff'
    fig=go.Figure(data=[go.Table(
        header=dict(
            values=["<b></b>"] +["<b>"+str(i)[:10]+"</b>" for i in dataframe.columns],
           line_color='#0078ff' ,fill_color='#0078ff',
            align='center',
            font=dict(color='white',size=15),height=35
        ),
        cells=dict(
            values=[["<b>"+str(i)+"</b>"for i in dataframe.index]]+[dataframe[i] for i in dataframe.columns],fill_color=[[rowOddColor,rowEvenColor]*len(dataframe.columns)],
align='left',line_color=['white'],font=dict(color=["black"],size=15)
        ))
    ])
    fig.update_layout(height=400,margin=dict(l=0,r=0,b=0,t=0))
    return fig 

def filter_data(dataframe,num_period):
    if num_period=='5d':
       date=dataframe.index[-1]+dateutil.relativedelta.relativedelta(days=-5)
    elif num_period=='1mo':
       date=dataframe.index[-1]+dateutil.relativedelta.relativedelta(months=-1)
    elif num_period=='6mo':
       date=dataframe.index[-1]+dateutil.relativedelta.relativedelta(months=-6)
    elif num_period=='ytd':
       date=datetime.datetime(dataframe.index[-1].year,1,1).strftime('%Y-%m-%d')
    elif num_period=='1y':
       date=dataframe.index[-1]+dateutil.relativedelta.relativedelta(years=-1)
       
    elif num_period=='5y':
       date=dataframe.index[-1]+dateutil.relativedelta.relativedelta(years=-5)
    else:
         date=dataframe.index[0]
         
    df_reset = dataframe.reset_index()
    return df_reset[df_reset['Date'] > date]

def close_chart(dataframe,num_period=False):
    if num_period:
        dataframe=filter_data(dataframe,num_period)
    fig=go.Figure()
    fig.add_trace(go.Scatter(x=dataframe['Date'],y=dataframe['Open'],mode='lines',name='Open',line=dict(width=2,color='#5ab7ff')))
    fig.add_trace(go.Scatter(x=dataframe['Date'],y=dataframe['Close'],mode='lines',name='Close',line=dict(width=2,color='black')))
    fig.add_trace(go.Scatter(x=dataframe['Date'],y=dataframe['High'],mode='lines',name='High',line=dict(width=2,color='#0078ff')))
    fig.add_trace(go.Scatter(x=dataframe['Date'],y=dataframe['Low'],mode='lines',name='Low',line=dict(width=2,color='red')))
    fig.update_xaxes(rangeslider_visible=True)
    fig.update_layout(margin=dict(l=0,r=20,b=0,t=20),height=500,plot_bgcolor='white',paper_bgcolor='#e1efff',legend=dict(yanchor='top',xanchor='right'))
    return fig

def candlestick(dataframe,num_period):
    dataframe = filter_data(dataframe,num_period)
    fig =go.Figure()
    fig.add_trace(go.Candlestick(x=dataframe['Date'],
                                 open=dataframe['Open'],
                                 high=dataframe['High'],
                                 low=dataframe['Low'],
                                 close=dataframe['Close'],))
    fig.update_layout(showlegend=False,margin=dict(l=0,r=20,b=0,t=20),height=500,plot_bgcolor='white',paper_bgcolor='#e1efff')
    return fig
def RSI(dataframe,num_period):
    dataframe['RSI']=pta.rsi(dataframe['Close'])
    
    dataframe = filter_data(dataframe, num_period)
    
    fig=go.Figure()
    fig.add_trace(go.Scatter(
        x=dataframe['Date'],
        y=dataframe['RSI'],name='RSI',marker_color='red',line=dict(width=2,color='red',dash='dash')
    ))
    fig.add_trace(go.Scatter(
        x=dataframe['Date'],
        y=[70]*len(dataframe),name='Overbought',marker_color='red',line=dict(width=2,color='red',dash='dash')
    ))
    fig.add_trace(go.Scatter(
        x=dataframe['Date'],
        y=[30]*len(dataframe),fill ='tozeroy',name='Oversold',marker_color='#79da84',line=dict(width=2,color='#79da84',dash='dash')
    ))
    
    fig.update_layout(yaxis_range=[0,100],margin=dict(l=0,r=0,b=0,t=0),height=200,plot_bgcolor='white',paper_bgcolor='#e1efff',legend=dict(orientation="h",
                                                                                                                                           yanchor='top',y=1.02,xanchor='right',x=1))
    return fig
def Moving_average(dataframe, num_period):

    dataframe['SMA_50'] = pta.sma(dataframe['Close'], 50)
    dataframe = filter_data(dataframe, num_period)
    fig = go.Figure()

    fig.add_trace(go.Scatter(x=dataframe['Date'], y=dataframe['Open'],
        mode='lines',
        name='Open', line = dict(width=2, color = '#5ab7ff')))

    fig.add_trace(go.Scatter(x=dataframe['Date'], y=dataframe['Close'],
        mode='lines',
        name='Close', line = dict(width=2, color = 'black')))

    fig.add_trace(go.Scatter(x=dataframe['Date'], y=dataframe['High'],
        mode='lines', name='High', line = dict(width=2, color = '#0078ff')))

    fig.add_trace(go.Scatter(x=dataframe['Date'], y=dataframe['Low'],
        mode='lines', name='Low', line = dict(width=2, color = 'red')))

    fig.add_trace(go.Scatter(x=dataframe['Date'], y=dataframe['SMA_50'],
        mode='lines', name='SMA 50', line = dict(width=2, color = 'purple')))

    fig.update_xaxes(rangeslider_visible=True)
    fig.update_layout(height = 500, margin=dict(l=0, r=20, t=20, b=0), plot_bgcolor = 'White', paper_bgcolor = '#e1efff', legend=dict(
        yanchor="top",
        xanchor="right"
    ))

    return fig
def MACD(dataframe, num_period):
    # 1. Calculate MACD *once*. This returns a DataFrame.
    macd_df = pta.macd(dataframe['Close'])
    
    # 2. Assign the columns correctly
    # By default, the columns are named:
    # 'MACD_12_26_9' (The MACD Line)
    # 'MACDh_12_26_9' (The Histogram)
    # 'MACDs_12_26_9' (The Signal Line)
    
    dataframe['MACD'] = macd_df['MACD_12_26_9']
    dataframe['MACD Hist'] = macd_df['MACDh_12_26_9'] 
    dataframe['MACD Signal'] = macd_df['MACDs_12_26_9']

    # 3. Filter the data *after* calculations
    dataframe = filter_data(dataframe, num_period)

    # 4. Create colors for the histogram *after* filtering
    c = ['green' if cl > 0 else 'red' for cl in dataframe['MACD Hist']]

    fig = go.Figure()
    
    # 5. Add the MACD Line (Fixed name)
    fig.add_trace(go.Scatter(
        x=dataframe['Date'],
        y=dataframe['MACD'], name = 'MACD', 
        line = dict(width=2, color = 'orange')
    ))

    # 6. Add the Signal Line (Fixed name)
    fig.add_trace(go.Scatter(
        x=dataframe['Date'],
        y=dataframe['MACD Signal'], name = 'MACD Signal',
        line = dict(width=2, color = 'red', dash='dash')
    ))

    # 7. ADD THE HISTOGRAM BARS
    fig.add_trace(go.Bar(
        x=dataframe['Date'],
        y=dataframe['MACD Hist'], name = 'MACD Hist',
        marker_color=c  # Use the colors
    ))

    fig.update_layout(
        height=200, plot_bgcolor = 'white', paper_bgcolor = '#e1efff', 
        margin=dict(l=0, r=0, t=0, b=0), 
        legend=dict(orientation="h", yanchor="top", y=1.02, xanchor="right", x=1)
    )

    return fig
def Moving_average_forecast(forecast):
    fig = go.Figure()

    fig.add_trace(go.Scatter(x=forecast.index[:-30], y=forecast['Close'].iloc[:-30],
        mode='lines',
        name='Close Price', line = dict(width=2, color = 'black')))

    fig.add_trace(go.Scatter(x=forecast.index[-31:], y=forecast['Close'].iloc[-31:],
        mode='lines', name='Future Close Price', line = dict(width=2, color = 'red')))


    fig.update_xaxes(rangeslider_visible=True)
    fig.update_layout(height = 500, margin=dict(l=0, r=20, t=20, b=0), plot_bgcolor = 'white', paper_bgcolor = '#efefff', legend=dict(
        yanchor="top",
        xanchor="right"
    ))

    return fig

def Moving_average_forecast(forecast):
    fig = go.Figure()

    fig.add_trace(go.Scatter(x=forecast.index[:-30], y=forecast['Close'].iloc[:-30],
        mode='lines',
        name='Close Price', line = dict(width=2, color = 'black')))

    fig.add_trace(go.Scatter(x=forecast.index[-31:], y=forecast['Close'].iloc[-31:],
        mode='lines', name='Future Close Price', line = dict(width=2, color = 'red')))


    fig.update_xaxes(rangeslider_visible=True)
    fig.update_layout(height = 500, margin=dict(l=0, r=20, t=20, b=0), plot_bgcolor = 'white', paper_bgcolor = '#efefff', legend=dict(
        yanchor="top",
        xanchor="right"
    ))

    return fig