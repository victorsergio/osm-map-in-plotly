# Run this app with `python test.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from utils import map_vis_without_lanelet_plotly


from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
import numpy as np

import plotly.graph_objects as go


app = Dash(__name__)

trajectory = np.array([
    [1000,1003],
    [1005,1003],
    [1010,1003],
    [1015,1003],
    [1020,1003],
    [1025,1003],
    [1030,1003],
    [1035,1003],
    [1040,1003]
])

df =  pd.DataFrame(trajectory, columns=['x', 'y'])


fig = go.Figure()

fig.update_yaxes(
    scaleanchor="x",
    scaleratio=1,
    showgrid=False
  )

fig.update_xaxes(showgrid=False)

# Call to the visualization lib
map_vis_without_lanelet_plotly.draw_map_without_lanelet("map.osm", fig = fig, lat_origin=0.0, lon_origin=0.0 )

fig.add_trace(go.Scatter(x=df["x"], y=df["y"]))  



fig.show()



app.layout = html.Div(children=[

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)