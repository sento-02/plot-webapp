import plotly.graph_objects as go
import pandas as pd


def create_graph(datafile):
    # CSVファイルの読み込み
    data = pd.read_csv(datafile.path)

    # グラフの作成
    colums = data.columns
    fontsize = 20
    Layout = go.Layout(
                    plot_bgcolor='white',
                    width=1000, height=600,
                    xaxis_title=dict(text=colums[0], font=dict(size=fontsize)),
                    yaxis_title=dict(text=colums[1], font=dict(size=fontsize)),
                    xaxis=dict(showline=True, linecolor="black", ticks='inside', showgrid=True, tickfont=dict(size=fontsize), mirror=False, ticklen=5, tickwidth=1, tickcolor='black'),
                    yaxis=dict(showline=True, linecolor="black", ticks='inside', showgrid=True, tickfont=dict(size=fontsize), mirror=False, ticklen=5, tickwidth=1, tickcolor='black'),
                    )
    fig = go.Figure(data=go.Scatter(x=data[colums[0]], y=data[colums[1]], mode='lines+markers', line=dict(width=3)), layout=Layout)
    return fig.to_html(full_html=False, default_height=600, default_width=1000)


if __name__ == '__main__':
    create_graph()