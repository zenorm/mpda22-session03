from flask import Flask
import ghhops_server as hs
import rhino3dm 

app = Flask(__name__)
hops = hs.Hops(app)


@hops.component(
    "/meshFromPoints",
    name = "meshFromPoints",
    inputs=[
        hs.HopsPoint("Points", "P", "Some Points", hs.HopsParamAccess.LIST)
    ],

    outputs=[
        hs.HopsMesh("Mesh","M","A simple rhino3dm mesh"),

    ]
)
def meshFromPoints(pts):

    m = rhino3dm.Mesh()

    for p in pts:
        m.Vertices.Add(p.X, p.Y, p.Z)

    
    m.Faces.AddFace(2,4,1,5) #triangular meshes repeat the last number!
    m.Faces.AddFace(0,5,1,3)

    print (m.Faces[0])
    print (m.Faces.TriangleCount)


    return m



@hops.component("/gridMesh",
    name = "gridMesh",
    inputs=[
        hs.HopsInteger("U_count", "U", None), 
        hs.HopsInteger("V_count", "V", None),
    ],

    outputs=[
        hs.HopsMesh("Mesh","M","A simple rhino3dm mesh"),
    ]
)

def gridMesh(U,V):


 #   U = 5
 #   V = 5

    #creating a simple mesh from a grid of points
    grid = []
    mesh = rhino3dm.Mesh()
    
    for i in range(U):
        for j in range(V):
            p = rhino3dm.Point3d(i,j,0)
            grid.append(p)
            mesh.Vertices.Add(p.X, p.Y, p.Z) 
            
    for i in range(len(grid)-(V)):
        if ( i % V != V -1 ):
            mesh.Faces.AddFace(i,i+1, i+V+1,i+V)

    print(mesh.Faces.Count)

    for i in range(mesh.Faces.Count):
        print(mesh.Faces[i])

    return mesh



if __name__== "__main__":
    app.run(debug=True)
