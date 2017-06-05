#
# https://plot.ly/python/3d-mesh/


import plotly.plotly as py
import plotly.graph_objs as go
import numpy as np

pts=np.loadtxt('dataset.txt')
x,y,z=zip(*pts)

trace = go.Mesh3d(x=x,y=y,z=z,
                   alphahull=5,
                   opacity=0.4,
                   color='00FFFF')
py.iplot([trace])
