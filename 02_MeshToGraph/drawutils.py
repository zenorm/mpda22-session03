import matplotlib.pyplot as plt
import networkx as nx

def plotGraph(G, node_size = 5):
    
    #pos = nx.kamada_kawai_layout(G)
    #pos = nx.planar_layout(G)
    pos = nx.random_layout(G)

    
    nx.draw(G,pos, node_size=node_size, with_labels=True, node_color="red", alpha=0.5)
    plt.tight_layout()
    #plt.show(block=False)
    plt.show()

def plotGraphSave(G, node_size = 5, file_name=  "nxplot.png"):

    #pos = nx.kamada_kawai_layout(G)
    #pos = nx.planar_layout(G)
    pos = nx.random_layout(G)

    nx.draw(G,pos, node_size=node_size, with_labels=True, node_color="red", alpha=0.5)
    plt.tight_layout()
    plt.savefig(file_name, format="PNG")
    plt.clf()

