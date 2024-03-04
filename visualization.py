from dijkstra_algorithm import Graph 
from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox as me
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

def open_file():

    file_name = fd.askopenfilename(filetypes=(("Text Files", "*.txt"),))
    first = start.get()
    last = end.get()

    if file_name == '' or first == '' or last == '':

        me.showinfo('Return', 'Error')

    else:

        f = open(file_name, 'r')

        G = nx.Graph()

        graph = Graph(file_name)
        returned_path, returned_distance = graph.shortest_path(first, last)
        
        returned_path = list(deque(returned_path))

        correct_way = []
        for i in range(len(returned_path)-1):
            correct_way.append((returned_path[i],returned_path[i+1]))

        with open(file_name) as file:
            array = [row.strip() for row in file]
            for i in range(len(array)):
                
                way = array[i].split()
                start_node = way[0]
                end_node = way[1]


                G.add_node(start_node)
                G.add_node(end_node)
                G.add_edge(start_node, end_node, weight = way[2])

        

        pos = nx.circular_layout(G)
        nx.draw(G, pos, with_labels = True)
        labels = nx.get_edge_attributes(G,'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
        nx.draw_networkx_edges(G, pos, edgelist = correct_way, edge_color="tab:green", width=5, alpha=0.5)
        plt.text(0.5,-1,"Shortest distance is: " + str(returned_distance))
        plt.show()

        f.close()

if __name__ == "__main__":

    root = Tk()
    start = Entry(root)
    end = Entry(root)
    btn_open = Button(root, text="Открыть", command=open_file)
    

    Label(root, text='Enter start position:').pack(side=TOP)
    start.pack()

    Label(root, text='Enter end position:').pack(side=TOP)
    end.pack()
    
    btn_open.pack(fill=X)
    root.mainloop()