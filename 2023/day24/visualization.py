import plotly.graph_objs as go
import numpy as np 

max_time = 1000000000000

fig = go.Figure()
i = 0
for line in open("input.txt"):
    if(i == 3):
        break
    position, velocity = line.strip().split("@")
    position = tuple(map(int, position.split(",")))
    velocity = tuple(map(int, velocity.split(",")))
    x = np.array([position[0], position[0] + velocity[0] * max_time])
    y = np.array([position[1], position[1] + velocity[1] * max_time])
    z = np.array([position[2], position[2] + velocity[2] * max_time])
    fig = fig.add_trace(go.Scatter3d(x=x, y=y,z=z, mode='lines'))
    i += 1
fig.show() 