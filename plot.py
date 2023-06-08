import plotly.graph_objects as go
import pandas as pd


def create_graph():
    # CSVファイルの読み込み
    data = pd.read_csv("data/20230531-141219-E0653-1BChiGlowH003K_perp000deg_40000.000000mV_1PLC_sekisan1-Major1.csv")



    # グラフの作成
    colums = data.columns
    fontsize = 20
    Layout = go.Layout(
                    xaxis_title=dict(text=colums[0], font=dict(size=fontsize)),
                    yaxis_title=dict(text=colums[1], font=dict(size=fontsize)),
                    xaxis=dict(showline=True, ticks='inside', showgrid=True, tickfont=dict(size=fontsize), mirror=False, ticklen=5, tickwidth=1, tickcolor='black'),
                    yaxis=dict(showline=True, ticks='inside', showgrid=True, tickfont=dict(size=fontsize), mirror=False, ticklen=5, tickwidth=1, tickcolor='black'),
                    width=1000, height=600
                    )
    fig = go.Figure(data=go.Scatter(x=data[colums[0]], y=data[colums[1]]) , layout=Layout)

    return fig.to_html(full_html=False, default_height=600, default_width=1000)


if __name__ == '__main__':
    create_graph()