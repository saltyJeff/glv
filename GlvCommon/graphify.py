from graphviz import dot, Digraph
from webbrowser import open
from GlvCommon.FuncThread import threadPool
from functools import partial
import urllib.parse
def makeGraph(name: str = 'Glv Graph') -> Digraph:
    graph = Digraph(name=name, comment='Glv Graph')
    graph.graph_attr['rankdir'] = 'LR'
    for thread in threadPool.values():
        for func in thread.funcs:
            graph.node(func.uuid, func.name+func.constArgStr+func.inputArgStr)
            for listener in func.output.listeners:
                graph.edge(func.uuid, listener.func.uuid)
    graph.browser = partial(vis, graph) # hack around having no graphviz
    return graph

def vis(self: Digraph):
    print('Opening Graph')
    quoteStr = urllib.parse.quote(self.source)
    open(f'https://dreampuf.github.io/GraphvizOnline/#{quoteStr}')

