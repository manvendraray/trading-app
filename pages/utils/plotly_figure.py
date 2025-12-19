import plotly.graph_objects as go 
import dateutil 
import pandas_ta as pta 
import datetime

def plotly_table(dataframe):
    # Colors
    header_color = "#1f4fd8"
    row_even_color = "#f5f7fb"
    row_odd_color = "#ffffff"
    border_color = "#e0e6f1"

    # Header (blank for index)
    header_values = [""] + [f"<b>{str(col)[:15]}</b>" for col in dataframe.columns]

    # Cell values
    index_values = [str(i) for i in dataframe.index]
    cell_values = [index_values] + [dataframe[col].astype(str).tolist()
                                    for col in dataframe.columns]

    # Row striping
    n_rows = len(dataframe)
    row_colors = [
        row_odd_color if i % 2 == 0 else row_even_color
        for i in range(n_rows)
    ]
    cell_fill_color = [row_colors] * (len(dataframe.columns) + 1)

    fig = go.Figure(
        data=[
            go.Table(
                columnwidth=[60] + [120] * len(dataframe.columns),
                header=dict(
                    values=header_values,
                    fill_color=header_color,
                    line_color=border_color,
                    align="center",
                    font=dict(color="white", size=16),
                    height=42,
                ),
                cells=dict(
                    values=cell_values,
                    fill_color=cell_fill_color,
                    line_color=border_color,
                    align=["center"] + ["left"] * len(dataframe.columns),
                    font=dict(color="#1f2937", size=14),
                    height=36,
                ),
            )
        ]
    )

    fig.update_layout(
        height=min(60 + n_rows * 38, 600),
        margin=dict(l=10, r=10, t=10, b=10),
        paper_bgcolor="white",
    )

    return fig



def filter_data(dataframe, num_period):
    if num_period == '1mo':
        date = dataframe.index[-1] + dateutil.relativedelta.relativedelta(months=-1)
    elif num_period == '5d':
        date = dataframe.index[-1] + dateutil.relativedelta.relativedelta(days=-5)
    elif num_period == '6mo':
        date = dataframe.index[-1] + dateutil.relativedelta.relativedelta(months=-6)
    elif num_period == '1y':
        date = dataframe.index[-1] + dateutil.relativedelta.relativedelta(years=-1)
    elif num_period == '5y':
        date = dataframe.index[-1] + dateutil.relativedelta.relativedelta(years=-5)
    elif num_period == 'ytd':
        date = datetime.datetime(dataframe.index[-1].year, 1, 1).strftime('%Y-%m-%d')
    else:
        date = dataframe.index[0]

    return dataframe.reset_index()[dataframe.reset_index()['Date'] > date]


def close_chart(dataframe, num_period=False):
    if num_period:
        dataframe = filter_data(dataframe, num_period)

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=dataframe['Date'], y=dataframe['Open'],
        mode='lines', name='Open',
        line=dict(width=2, color='#5ab7ff')
    ))

    fig.add_trace(go.Scatter(
        x=dataframe['Date'], y=dataframe['Close'],
        mode='lines', name='Close',
        line=dict(width=2, color='black')
    ))

    fig.add_trace(go.Scatter(
        x=dataframe['Date'], y=dataframe['High'],
        mode='lines', name='High',
        line=dict(width=2, color='#0078ff')
    ))

    fig.add_trace(go.Scatter(
        x=dataframe['Date'], y=dataframe['Low'],
        mode='lines', name='Low',
        line=dict(width=2, color='red')
    ))

    fig.update_xaxes(rangeslider_visible=True)

    fig.update_layout(
        height=500,
        margin=dict(l=0, r=20, t=20, b=0),
        plot_bgcolor='white',
        paper_bgcolor='#e1efff',
        legend=dict(
            yanchor="top",
            y=0.2,
            xanchor="right",
            x=1
        )
    )

    return fig

def candlestick(dataframe, num_period):
    dataframe = filter_data(dataframe, num_period)

    fig = go.Figure()

    fig.add_trace(
        go.Candlestick(
            x=dataframe["Date"],
            open=dataframe["Open"],
            high=dataframe["High"],
            low=dataframe["Low"],
            close=dataframe["Close"],
            increasing=dict(
                line=dict(color="#16a34a", width=1.2),
                fillcolor="#16a34a",
            ),
            decreasing=dict(
                line=dict(color="#dc2626", width=1.2),
                fillcolor="#dc2626",
            ),
        )
    )

    fig.update_layout(
        template="plotly_white",
        height=520,
        showlegend=False,
        hovermode="x unified",
        margin=dict(l=40, r=40, t=40, b=40),
        paper_bgcolor="#102434",
        plot_bgcolor="#FFFFFF",
    )

    fig.update_xaxes(
        showgrid=True,
        gridcolor="#e5e7eb",
        showline=True,
        linecolor="#d1d5db",
        rangeslider=dict(visible=False),
        tickfont=dict(size=12),
    )

    fig.update_yaxes(
        showgrid=True,
        gridcolor="#e5e7eb",
        showline=True,
        linecolor="#d1d5db",
        tickfont=dict(size=12),
    )

    return fig


def RSI(dataframe, num_period):
    dataframe['RSI'] = pta.rsi(dataframe['Close'])
    dataframe = filter_data(dataframe, num_period)

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=dataframe['Date'], y=dataframe['RSI'],
        name='RSI',
        marker_color='orange',
        line=dict(width=2, color='orange')
    ))

    fig.add_trace(go.Scatter(
        x=dataframe['Date'], y=[70]*len(dataframe),
        name='Overbought',
        marker_color='red',
        line=dict(width=2, color='red', dash='dash')
    ))

    fig.add_trace(go.Scatter(
        x=dataframe['Date'], y=[30]*len(dataframe),
        name='Oversold',
        marker_color='#79da84',
        line=dict(width=2, color='#79da84', dash='dash')
    ))

    fig.update_layout(
    yaxis_range=[0, 100],
    height=200,
    plot_bgcolor='white',
    paper_bgcolor='#e1efff',
    margin=dict(l=0, r=0, t=0, b=0),
    legend=dict(
        orientation='h',
        yanchor='top',
        y=1.02,
        xanchor='right',
        x=1
    )
)

    


    return fig

def Moving_average(dataframe, num_period):
    dataframe['SMA_50'] = pta.sma(dataframe['Close'], 50)
    dataframe = filter_data(dataframe, num_period)
    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=dataframe['Date'], y=dataframe['Open'],
        mode='lines',
        name='Open',
        line=dict(width=2, color='#5ab7ff')
    ))

    fig.add_trace(go.Scatter(
        x=dataframe['Date'], y=dataframe['Close'],
        mode='lines',
        name='Close',
        line=dict(width=2, color='black')
    ))

    fig.add_trace(go.Scatter(
        x=dataframe['Date'], y=dataframe['High'],
        mode='lines',
        name='High',
        line=dict(width=2, color='#0078ff')
    ))

    fig.add_trace(go.Scatter(
        x=dataframe['Date'], y=dataframe['Low'],
        mode='lines',
        name='Low',
        line=dict(width=2, color='red')
    ))

    fig.add_trace(go.Scatter(
        x=dataframe['Date'], y=dataframe['SMA_50'],
        mode='lines',
        name='SMA 50',
        line=dict(width=2, color='purple')
    ))

    fig.update_xaxes(rangeslider_visible=True)

    fig.update_layout(
        height=500,
        margin=dict(l=0, r=20, t=20, b=0),
        plot_bgcolor='white',
        paper_bgcolor='#e1efff',
        legend=dict(
            yanchor="top",
            y=0.2,
            xanchor="right",
            x=1
        )
    )

    return fig


def Moving_average_candle_stick(dataframe, num_period):
    dataframe['SMA_50'] = pta.sma(dataframe['Close'], 50)
    dataframe = filter_data(dataframe, num_period)
    fig = go.Figure()

    fig.add_trace(go.Candlestick(
        x=dataframe.index,
        open=dataframe['Open'],
        high=dataframe['High'],
        low=dataframe['Low'],
        close=dataframe['Close'],
        name='Price'
    ))

    fig.add_trace(go.Scatter(
        x=dataframe.index,
        y=dataframe['SMA_50'],
        mode='lines',
        name='SMA 50',
        line=dict(width=2, color='purple')
    ))

    fig.update_layout(
        showlegend=True,
        height=500,
        margin=dict(l=0, r=20, t=20, b=0),
        plot_bgcolor='white',
        paper_bgcolor='#e1efff'
    )

    return fig


def MACD(dataframe, num_period):
    macd = pta.macd(dataframe['Close']).iloc[:, 0]
    macd_signal = pta.macd(dataframe['Close']).iloc[:, 1]
    macd_hist = pta.macd(dataframe['Close']).iloc[:, 2]

    dataframe['MACD'] = macd
    dataframe['MACD Signal'] = macd_signal
    dataframe['MACD Hist'] = macd_hist

    dataframe = filter_data(dataframe, num_period)

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=dataframe['Date'], y=dataframe['MACD'],
        name='RSI',            # (label as in your screenshot)
        marker_color='orange',
        line=dict(width=2, color='orange')
    ))

    fig.add_trace(go.Scatter(
        x=dataframe['Date'], y=dataframe['MACD Signal'],
        name='Overbought',     # (label as in your screenshot)
        marker_color='red',
        line=dict(width=2, color='red', dash='dash')
    ))

    c = ['red' if c1 < 0 else 'green' for c1 in macd_hist]

    fig.update_layout(
        height=200,
        plot_bgcolor='white',
        paper_bgcolor='#e1efff',
        margin=dict(l=0, r=0, t=0, b=0),
        legend=dict(orientation='h')
    )

    return fig



def Moving_average_forecast(forecast):
    fig = go.Figure()

    # Historical prices
    fig.add_trace(
        go.Scatter(
            x=forecast.index[:-30],
            y=forecast['Close'].iloc[:-30],
            mode='lines',
            name='Historical Close',
            line=dict(width=2.8),
            hovertemplate="Date: %{x}<br>Close: %{y:.2f}<extra></extra>",
        )
    )

    # Forecasted prices
    fig.add_trace(
        go.Scatter(
            x=forecast.index[-31:],
            y=forecast['Close'].iloc[-31:],
            mode='lines',
            name='Forecast',
            line=dict(width=2.8, dash='dash'),
            hovertemplate="Date: %{x}<br>Forecast: %{y:.2f}<extra></extra>",
        )
    )

    fig.update_layout(
        template="plotly_white",
        title=dict(
            text="Moving Average Forecast",
            x=0.5,
            font=dict(size=20, color="#1f2937"),
        ),
        height=520,
        hovermode="x unified",
        margin=dict(l=40, r=40, t=70, b=40),
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="center",
            x=0.5,
            font=dict(size=13),
        ),
    )

    fig.update_xaxes(
        title="Date",
        showgrid=True,
        gridcolor="#e5e7eb",
        showline=True,
        linecolor="#d1d5db",
        rangeslider=dict(visible=True, thickness=0.05),
    )

    fig.update_yaxes(
        title="Price",
        showgrid=True,
        gridcolor="#e5e7eb",
        showline=True,
        linecolor="#d1d5db",
    )

    return fig
