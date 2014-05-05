# module fastgraph
# created by Gribouillis for the python forum at www.daniweb.com
# November 9, 2010
# Licence: public domain

    #   This module defines 3 functions (node, edge and graph) to help
    #   create a graph (a pygraphviz.AGraph instance) linking arbitrary
    #   python objects.
    #   This graph can be saved in various image formats, and in dot format.
        
import pygraphviz

def node(x):
    "helper to create graphs"
    return (x,)

def edge(x, y):
    "helper to create graphs"
    return (x, y)

def graph(items, tolabel, **kwd):
    # Create a pygraphviz AGraph instance
    #    @ items - a sequence of node(obj), or edge(obj, obj) items (obj can be any python object)
    #    @ tolabel - a function tolabel(obj) -> str which converts an object to string
    #    @ **kwd - additional keyword arguments for AGraph.__init__
    
    names = dict()
    the_graph = pygraphviz.AGraph(**kwd)
    for uple in (tuple(t) for t in items):
        for obj in uple:
            if not obj in names:
                names[obj] = "n%d" % len(names)
                the_graph.add_node(names[obj], label=tolabel(obj), shape="box")
                
            if len(uple) == 2:
                the_graph.add_edge(*(names[obj] for obj in uple))
    return the_graph
                
#
#if __name__ == "__main__":
#
#    def my_items():
#        # Example generator of graph items. Our graph contains string here
#        for x in ['AuthorA', 'Author B', 'Author C']:
#            yield node(x)
#        
#        for s in [['AuthorA', 'Author B'], ['Author B', 'Author C'], ['Author C', 'AuthorA']]:
#            yield edge(s[0], s[1])
#            #x, y = iter(s)
#            #yield edge(x, y)
#    
#    def my_label(x):
#        "Create a label for graph objects"
#        return x.upper()
#    
#    g = graph(my_items(), my_label)
#    g.draw('mygraph.png', prog='circo') # prog can be neato|dot|twopi|circo|fdp|nop

def buildNodes(authorpath):
        if len(authorpath) > 1:
            for authorname in authorpath:
                yield node(authorname)
            
            for i in range(0, len(authorpath) - 1):
                yield edge(authorpath[i], authorpath[i + 1])
    
def authorlabel(authorname):
    return authorname.upper()

class graph_network:
    
    def buildnetworkgraph(self, authorpath):
        if len(authorpath) > 1:
            networkgraph = graph(buildNodes(authorpath), authorlabel)
            networkgraph.draw('hunt_network.png', prog='circo')
                    