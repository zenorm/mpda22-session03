from flask import Flask
import ghhops_server as hs

app = Flask(__name__)
hops = hs.Hops(app)

import meshpath as mp
import meshutils as mu
import drawutils as du



@hops.component(
    "/meshgraph",
    name = "meshgraph",
    inputs=[
        hs.HopsMesh("Input Mesh", "M", "Mesh"),
        hs.HopsBoolean("Plot", "P", "Plot", optional=True),
        hs.HopsBoolean("Save", "S", "Save", optional=True)



    ],
    outputs=[
        hs.HopsString("text","T","shortest path points"),

    ]
)
def meshToGraph(mesh, plot=False, save = False):

    G = mp.SimpleGraphFromMesh(mesh)
    if plot: du.plotGraph(G)
    if save: du.plotGraphSave(G) 
    
    return str(G)


@hops.component(
    "/shortestpath",
    name = "shortestpath",
    inputs=[
        hs.HopsINteger(),
        hs.HopsMesh("Input Mesh", "M", "Mesh"),
        hs.HopsInteger("face Index 1","f1","Face index one"),
        hs.HopsInteger("face Index 2","f2","Face index two")

    ],
    outputs=[
        hs.HopsInteger("SP","SP","Shortest path nodes", hs.HopsParamAccess.LIST),

    ]
)
def shortestPath(mesh, f1, f2):

    G = mp.SimpleGraphFromMesh(mesh)
    SP = mp.shortestPath(G, f1, f2)
    
    return SP






if __name__== "__main__":
    app.run(debug=True)
