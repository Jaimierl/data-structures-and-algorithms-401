class Graph:
    """
    This is an implementation of a graph data structure.
    """
    def __init__(self):
        self.adjacency = []

    def add_node(self,value):
        """Arguments: value
        Returns: The added node
        Add a node to the graph adjacency dictionary as a key with an empty list as a value"""
        vertex = Vertex(value)
        if vertex.value not in self.adjacency:
            self.adjacency.append(vertex)
        return vertex

    def add_edge(self, node1, node2, weight=1):
        """Arguments: 2 nodes to be connected by the edge, weight (optional)
        Returns: nothing
        Adds a new edge between two nodes in the graph
        If specified, assign a weight to the edge
        Both nodes should already be in the Graph
        User choice for making this unidirectional or bi-directinal. We are making it bidirectional.
        """
        print(self.adjacency)
        if node1 not in self.adjacency:
            print("node1 not in graph")
            raise KeyError
        if node2 not in self.adjacency:
            print("node2 not in graph")
            raise KeyError

        if node1 == node2:
            edge1 = Edge(node1,node2,weight)
            node1.edges.append(edge1)

        else:
            edge1 = Edge(node1,node2,weight)
            node1.edges.append(edge1)
            
            edge2 = Edge(node2,node1, weight)
            node2.edges.append(edge2)
        

    def get_nodes(self):
        """Arguments: none
        Returns all of the nodes in the graph as a collection (set, list, or similar)"""
        all_keys = []
        for vertex in self.adjacency:
            all_keys.append(vertex.value)
        print (all_keys)
        return all_keys

    def get_neighbors(self, node):
        """Arguments: node
        Returns a collection of edges connected to the given node, and their respective weights"""
        for edge in node.edges:
            print ("edge = "+ edge.vertex.value + "weight = " + str(edge.weight))
        return node.edges

    def size(self):
        """Arguments: none
        Returns the total number of nodes in the graph"""
        length = len(self.adjacency)
        print (self.adjacency)
        return length

class Vertex:
    """
    This is the node class but it is referred to as a vertex here then it is standalone
    """
    def __init__(self, value):
        self.value = value
        self.edges = []

class Edge:
    """
    Edges are initialized with JUST a vertex (outside of the graph) and the add_edge function links the graph-plus-vertex to some vertex that already exists in the graph.
    An edge essentially contains a weight and node at the other end of the edge.
    """
    def __init__(self, graph_vertex, vertex, weight=1):
        self.graph_vertex = graph_vertex
        self.vertex = vertex
        self.weight = weight
