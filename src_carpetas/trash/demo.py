# en la terminal
# sudo pip install plotly
#
# https://plot.ly/matplotlib/trisurf/

import numpy as np
import matplotlib.cm as cm
from scipy.spatial import Delaunay




def map_z2color(zval, colormap, vmin, vmax):
    #map the normalized value zval to a corresponding color in the colormap

    if vmin>vmax:
        raise ValueError('incorrect relation between vmin and vmax')
    t=(zval-vmin)/float((vmax-vmin))#normalize val
    R, G, B, alpha=colormap(t)
    return 'rgb('+'{:d}'.format(int(R*255+0.5))+','+'{:d}'.format(int(G*255+0.5))+\
           ','+'{:d}'.format(int(B*255+0.5))+')'

def tri_indices(simplices):
    #simplices is a numpy array defining the simplices of the triangularization
    #returns the lists of indices i, j, k

    return ([triplet[c] for triplet in simplices] for c in range(3))


import plotly.plotly as py
import plotly.graph_objs as go
from plotly.graph_objs import *

def plotly_trisurf(x, y, z, simplices, colormap=cm.RdBu, plot_edges=None):
    #x, y, z are lists of coordinates of the triangle vertices
    #simplices are the simplices that define the triangularization;
    #simplices  is a numpy array of shape (no_triangles, 3)
    #insert here the  type check for input data

    points3D=np.vstack((x,y,z)).T
    tri_vertices=map(lambda index: points3D[index], simplices)# vertices of the surface triangles
    zmean=[np.mean(tri[:,2]) for tri in tri_vertices ]# mean values of z-coordinates of
                                                      #triangle vertices
    min_zmean=np.min(zmean)
    max_zmean=np.max(zmean)
    facecolor=[map_z2color(zz,  colormap, min_zmean, max_zmean) for zz in zmean]
    I,J,K=tri_indices(simplices)

    triangles=go.Mesh3d(x=x,
                     y=y,
                     z=z,
                     facecolor=facecolor,
                     i=I,
                     j=J,
                     k=K,
                     name=''
                    )

    if plot_edges is None:# the triangle sides are not plotted
        return Data([triangles])
    else:
        #define the lists Xe, Ye, Ze, of x, y, resp z coordinates of edge end points for each triangle
        #None separates data corresponding to two consecutive triangles
        lists_coord=[[[T[k%3][c] for k in range(4)]+[ None]   for T in tri_vertices]  for c in range(3)]
        Xe, Ye, Ze=[reduce(lambda x,y: x+y, lists_coord[k]) for k in range(3)]

        #define the lines to be plotted
        lines=Scatter3d(x=Xe,
                        y=Ye,
                        z=Ze,
                        mode='lines',
                        line=Line(color= 'rgb(50,50,50)', width=1.5)
               )
        return Data([triangles, lines])


# hello world  figure

n=12# number of radii
h=1.0/(n-1)
r = np.linspace(h, 1.0, n)
theta= np.linspace(0, 2*np.pi, 36)

r,theta=np.meshgrid(r,theta)
r=r.flatten()
theta=theta.flatten()

#Convert polar coordinates to cartesian coordinates (x,y)
x=r*np.cos(theta)
y=r*np.sin(theta)
x=np.append(x, 0)#  a trick to include the center of the disk in the set of points. It was avoided
                 # initially when we defined r=np.linspace(h, 1.0, n)
y=np.append(y,0)
z = np.sin(-x*y)

points2D=np.vstack([x,y]).T
tri=Delaunay(points2D)

data2=plotly_trisurf(x,y,z, tri.simplices, colormap=cm.cubehelix, plot_edges=None)
fig2 = Figure(data=data2, layout=layout)
fig2['layout'].update(dict(title='Triangulated surface',
                          scene=dict(camera=dict(eye=dict(x=1.75,
                                                          y=-0.7,
                                                          z= 0.75)
                                                )
                                    )))

py.sign_in('empet', '')
py.iplot(fig2, filename='trisurf-cubehx')
