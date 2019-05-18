from graphviz import dot, Digraph
from GlvCommon.FuncThread import pool
def makeGraph() -> Digraph:
    graph = Digraph(name='Glv Graph', comment='Glv Graph')

    for thread in pool.values():
        for func in thread.funcs:
            graph.node(func.uuid, func.name)
            for listener in func.output.listeners:
                graph.edge(func.uuid, listener.func.uuid)

    return graph
