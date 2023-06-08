import plotly.graph_objects as go
import pandas as pd


def create_graph(datafile_list):
    default_height = 600
    default_width = 1000

    # CSVファイルの読み込み
    scatters = []
    for datafile in datafile_list:
        data = pd.read_csv(datafile.path)
        colums = data.columns
        scatter=go.Scatter(x=data[colums[0]], y=data[colums[1]], mode='lines+markers', line=dict(width=3))
        scatters.append(scatter)

    # グラフの作成
    fontsize = 20
    Layout = go.Layout(
                    plot_bgcolor='white',
                    width=1000, height=600,
                    xaxis_title=dict(text=colums[0], font=dict(size=fontsize)),
                    yaxis_title=dict(text=colums[1], font=dict(size=fontsize)),
                    xaxis=dict(showline=True, linecolor="black", ticks='inside', showgrid=True, tickfont=dict(size=fontsize), mirror=False, ticklen=5, tickwidth=1, tickcolor='black'),
                    yaxis=dict(showline=True, linecolor="black", ticks='inside', showgrid=True, tickfont=dict(size=fontsize), mirror=False, ticklen=5, tickwidth=1, tickcolor='black'),
                    ) 
    fig = go.Figure(data=scatters, layout=Layout)

    return fig.to_html(full_html=False, default_height=default_height, default_width=default_width)


if __name__ == '__main__':
    create_graph()