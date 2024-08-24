import plotly.graph_objs as go
import plotly.io as pio

values = [1, 5, 8, 9, 2, 0, 3, 10, 4, 7]
values2 = [3,2,4,5,6,7,10,15,8,-1,5,-10]
fig = go.Figure()

fig.add_trace(go.Scatter(x=list(range(1, 11)), y=values, mode='lines', name='Empresa A'))
fig.add_trace(go.Scatter(x=list(range(1, 11)), y=values2, mode='lines', name='Empresa B'))
pio.show(fig)


