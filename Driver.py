import Graph
import networkx as nx

if __name__ == '__main__':
    g = Graph.ActivityGraph()
    g.ReadEdgeList('SampleGraph.txt')
    # g.GetAttribute('label')
    # g.DrawGraph()
    g.FindDistCost(1,5)
    CPL, CPC, CP = g.FindCriticalPath(1,5)
    print(CP)
    print(CPL)
    print(CPC)
    print(g.FindStatusReport(1, 10))
