from dash import Dash, html, dcc, Input, Output
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc

import numpy as np 

import base64
from PIL import Image


import plotly.graph_objects as go
from scipy.spatial import ConvexHull



app = Dash(external_stylesheets=[dbc.themes.DARKLY])
application = app.server


def b64_image(image_filename):
    with open(image_filename, 'rb') as f:
        image = f.read()
    return 'data:image/png;base64,' + base64.b64encode(image).decode('utf-8')


# Comparing images of cells ----------------
image_path_a='./images/normal_2.png'
img = Image.open(image_path_a).convert('L')
fig1=px.imshow(img)
fig1.update_layout(dragmode="drawrect")
fig1.update_layout({'title':{'text':'Normal Cell', 'x':0.5}})
fig1.update_layout({'paper_bgcolor': 'rgba(0,0,0,0)', 'font':{'color':'white'}})


image_path_b='./images/apoptotic_2.png'
img2 = Image.open(image_path_b).convert('L')
fig2=px.imshow(img2)
fig2.update_layout(dragmode="drawrect")
fig2.update_layout({'title':{'text':'Apoptotic Cell', 'x':0.5}})
fig2.update_layout({'paper_bgcolor': 'rgba(0,0,0,0)'})
fig2.update_layout({'paper_bgcolor': 'rgba(0,0,0,0)', 'font':{'color':'white'}})



image_path_c='./images/necrotic_2.png'
img3 = Image.open(image_path_c).convert('L')
fig3=px.imshow(img3)
fig3.update_layout(dragmode="drawrect")
fig3.update_layout({'title':{'text':'Necrotic Cell', 'x':0.5}})
fig3.update_layout({'paper_bgcolor': 'rgba(0,0,0,0)'})
fig3.update_layout({'paper_bgcolor': 'rgba(0,0,0,0)', 'font':{'color':'white'}})


config = {
    "modeBarButtonsToAdd": [
        "drawline",
        "drawclosedpath",
        "drawopenpath",
        "drawcircle",
        "drawrect",
        "ereaseshape"
    ]
}

image_path_d = './images/normal_2.png'
image_path_e = './images/apoptotic_2.png'
img4 = Image.open(image_path_d)
img5 = Image.open(image_path_e)
img4 = np.array(img4)
img5 = np.array(img5)
image4 = np.resize(img4, img5.shape)
image5 = img5
diff = np.abs(image4-image5)
diff_flat = diff.flatten()

x_coords, y_coords = np.meshgrid(range(diff.shape[1]), range(diff.shape[0]))
x_coords = x_coords.flatten()
y_coords = y_coords.flatten()

fig4 = go.Figure(
    go.Scatter(
        x=x_coords,
        y=y_coords,
        mode='markers',
        marker=dict(
            size=3,
            color=diff_flat,
            colorscale='viridis',
            opacity=0.8
        )
    )
)

# Define the layout of the scatter plot
fig4.update_layout(
    title='Pixel-wise difference between Normal and Apoptotic Cell',
    xaxis=dict(
        title='X pixel coordinate',
        range=[0, diff.shape[1]]
    ),
    yaxis=dict(
        title='Y pixel coordinate',
        range=[0, diff.shape[0]]
    )
)
fig4.update_layout({'paper_bgcolor': 'rgba(0,0,0,0)', 'font':{'color':'white'}})
fig4.update_layout({'title':{'x':0.5}})


image_path_f = './images/necrotic_2.png'
img6 = Image.open(image_path_d)
img7 = Image.open(image_path_f)
img6 = np.array(img6)
img7 = np.array(img7)
image6 = np.resize(img6, img7.shape)
image7 = img7
diff = np.abs(image6-image7)
diff_flat = diff.flatten()

x_coords, y_coords = np.meshgrid(range(diff.shape[1]), range(diff.shape[0]))
x_coords = x_coords.flatten()
y_coords = y_coords.flatten()

fig5 = go.Figure(
    go.Scatter(
        x=x_coords,
        y=y_coords,
        mode='markers',
        marker=dict(
            size=3,
            color=diff_flat,
            colorscale='viridis',
            opacity=0.8
        )
    )
)

# Define the layout of the scatter plot
fig5.update_layout(
    title='Pixel-wise difference between Normal and Necrotic Cell',
    xaxis=dict(
        title='X pixel coordinate',
        range=[0, diff.shape[1]]
    ),
    yaxis=dict(
        title='Y pixel coordinate',
        range=[0, diff.shape[0]]
    )
)
fig5.update_layout({'paper_bgcolor': 'rgba(0,0,0,0)', 'font':{'color':'white'}})
fig5.update_layout({'title':{'x':0.5}})




# contout plot
image_path_g = './images/normal_2.png'
img8 = Image.open(image_path_g)
img8 = np.array(img8)
threshold = 0.3
mask = np.where(img8 > threshold, 1, 0)

contour_points = np.argwhere(mask)
hull = ConvexHull(contour_points)
contour = contour_points[hull.vertices]

# Create the scatter plot of the object contour
scatter = go.Scatter(
    x=contour[:, 1],
    y=contour[:, 0],
    mode='lines',
    line=dict(
        color='blue',
        width=2
    )
)

# Define the layout of the scatter plot
layout = go.Layout(
    title='Contour plot of a Normal Cell',
    xaxis=dict(
        title='X coordinate',
        range=[0, img8.shape[1]-1]
    ),
    yaxis=dict(
        title='Y coordinate',
        range=[0, img8.shape[0]-1]
    )
)

# Create the figure with the scatter plot and layout
fig6 = go.Figure(data=[scatter], layout=layout)
fig6.update_layout({'paper_bgcolor': 'rgba(0,0,0,0)', 'font':{'color':'white'}})
fig6.update_layout({'title':{'x':0.5}})


image_path_h = './images/apoptotic_2.png'
img9 = Image.open(image_path_h)
img9 = np.array(img9)
threshold = 0.3
mask = np.where(img9 > threshold, 1, 0)

contour_points = np.argwhere(mask)
hull = ConvexHull(contour_points)
contour = contour_points[hull.vertices]

# Create the scatter plot of the object contour
scatter = go.Scatter(
    x=contour[:, 1],
    y=contour[:, 0],
    mode='lines',
    line=dict(
        color='blue',
        width=2
    )
)

# Define the layout of the scatter plot
layout = go.Layout(
    title='Contour plot of an Apoptotic Cell',
    xaxis=dict(
        title='X coordinate',
        range=[0, img9.shape[1]-1]
    ),
    yaxis=dict(
        title='Y coordinate',
        range=[0, img9.shape[0]-1]
    )
)

# Create the figure with the scatter plot and layout
fig7 = go.Figure(data=[scatter], layout=layout)
fig7.update_layout({'paper_bgcolor': 'rgba(0,0,0,0)', 'font':{'color':'white'}})
fig7.update_layout({'title':{'x':0.5}})


image_path_i = './images/necrotic_2.png'
img10 = Image.open(image_path_i)
img10 = np.array(img10)
threshold = 0.3
mask = np.where(img10 > threshold, 1, 0)

contour_points = np.argwhere(mask)
hull = ConvexHull(contour_points)
contour = contour_points[hull.vertices]

# Create the scatter plot of the object contour
scatter = go.Scatter(
    x=contour[:, 1],
    y=contour[:, 0],
    mode='lines',
    line=dict(
        color='blue',
        width=2
    )
)

# Define the layout of the scatter plot
layout = go.Layout(
    title='Contour plot of a Necrotic Cell',
    xaxis=dict(
        title='X coordinate',
        range=[0, img10.shape[1]-1]
    ),
    yaxis=dict(
        title='Y coordinate',
        range=[0, img10.shape[0]-1]
    )
)

# Create the figure with the scatter plot and layout
fig8 = go.Figure(data=[scatter], layout=layout)
fig8.update_layout({'paper_bgcolor': 'rgba(0,0,0,0)', 'font':{'color':'white'}})
fig8.update_layout({'title':{'x':0.5}})
#-------------------------------------------


# from here app layout and callback


# ------------------------------------------
app.layout = html.Div([
    html.H1('Identification of Cells', style={'textAlign': 'center'}),
    html.Div([
        dcc.Slider(
            id='apoptosis-slider',
            min=0,
            max=1,
            step=0.2,
            value=0,
            marks={
                0: {'label': 'Normal Cell'},
                1: {'label': 'Apoptotic Cell'}
            }
        ),
        html.Div(id='apoptosis-output-container'),
        html.Div("a Normal Cell in contrast with a Apoptotic cell showing the typical round shape and chromatin condensation", style={'textAlign': 'center', 'marginTop': '30px'})
    ], style={'display': 'inline-block', 'width': '40%', 'verticalAlign': 'top', 'paddingRight': '20px', 'marginTop': '30px'}),
    html.Div([
        dcc.Slider(
            id='necrosis-slider',
            min=0,
            max=1,
            step=0.2,
            value=0,
            marks={
                0: {'label': 'Normal Cell'},
                1: {'label': 'Necrotic Cell'}
            }
        ),
        html.Div(id='necrosis-output-container'),
        html.Div("a Normal Cell in contrast with a Necrotic cell showing increased cell size, rupture of cell membrane and vacuoles formation.", style={'textAlign': 'center', 'marginTop': '30px'})
    ], style={'display': 'inline-block', 'width': '40%', 'verticalAlign': 'top', 'paddingLeft': '20px','marginTop': '30px'}),
    html.Div('Using a Heuristic approach, identifying dead cells from live cells can be done by looking at these principal characteristics of dead cells:', style={'marginTop': '80px'}),
    html.Ul(style={'display': 'flex', 'flex-direction': 'column', 'align-items': 'flex-start', "display": "inline-block", "text-align": "left", "padding-left": "0"},
    children=[
        html.Li('Cell morphology'),
        html.Li('Cell membrane integrity'),
        html.Li('Metabolic activity'),
        html.Li('Nucleus morphology'),
        html.Li('Cytoplasmic granularity'),
        html.Li('Fluorescence staining')
    ]),
    html.Div(
        children=[
            html.Div(
            [
                dcc.Graph(figure=fig1, config=config)
            ], style={'width':'30%', 'display':'inline-block'}),
            html.Div(
            [
                dcc.Graph(figure=fig2, config=config)
            ], style={'width':'30%', 'display':'inline-block'}),
            html.Div(
            [
                dcc.Graph(figure=fig3, config=config)
            ], style={'width':'30%', 'display':'inline-block'})
        ]
    ),
    html.Div(
        children=[
            html.Div(
            [
                dcc.Graph(figure=fig4, config=config)
            ], style={'width':'45%', 'display':'inline-block'}),
            html.Div(
            [
                dcc.Graph(figure=fig5, config=config)
            ], style={'width':'45%', 'display':'inline-block'})
        ]
    ),
    html.Div(
        children=[
            html.Div(
            [
                dcc.Graph(id='mask-plot1',figure=fig6, config=config)
            ], style={'width':'30%', 'display':'inline-block'}),
            
            html.Div(
            [
                dcc.Graph(id='mask-plot2',figure=fig7, config=config)
            ], style={'width':'30%', 'display':'inline-block'}),
            html.Div(
            [
                dcc.Graph(id='mask-plot3',figure=fig8, config=config)
            ], style={'width':'30%', 'display':'inline-block'})

        ]
    )
], style={'textAlign': 'center'})

# Define the callback to update the image for apoptosis
@app.callback(
    Output('apoptosis-output-container', 'children'),
    [Input('apoptosis-slider', 'drag_value')])
def update_output_apoptosis(drag_value):
    if drag_value == 0:
        image = 'Normal cell image'
        image_path = './images/normal_2.png'
    elif drag_value == 0.2:
        image_path = './images/normal_apoptotic_1.png'
    elif drag_value == 0.4:
        image_path = './images/normal_apoptotic_2.png'
    elif drag_value == 0.6:
        image_path = './images/normal_apoptotic_3.png'
    elif drag_value == 0.8:
        image_path = './images/normal_apoptotic_4.png'
    else:
        image_path = './images/apoptotic_2.png'

    pic = html.Img(src=b64_image(image_path), style={'width': '188px', 'margin': 'auto'})
    return [pic]

# Define the callback to update the image for necrosis
@app.callback(
    Output('necrosis-output-container', 'children'),
    [Input('necrosis-slider', 'drag_value')])
def update_output_necrosis(drag_value):
    if drag_value == 0:
        image_path = './images/normal_2.png'
    elif drag_value == 0.2:
        image_path = './images/normal_necrotic_1.png'
    elif drag_value == 0.4:
        image_path = './images/normal_necrotic_2.png'
    elif drag_value == 0.6:
        image_path = './images/normal_necrotic_3.png'
    elif drag_value == 0.8:
        image_path = './images/normal_necrotic_4.png'
    else:
        image_path = './images/necrotic_2.png'

    pic = html.Img(src=b64_image(image_path), style={'width': '188px', 'margin': 'auto'})
    return [pic]
# ------------------------------------------



if __name__ == '__main__':
    app.run_server(debug=True)
