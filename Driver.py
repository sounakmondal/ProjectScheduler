import Graph
import networkx as nx

if __name__ == '__main__':
    g = Graph.ActivityGraph()
    g.ReadEdgeList('HydroElectric.txt')
    # g.GetAttribute('label')
    # g.DrawGraph()
    g.FindDistCost('a','n' )
    CPL, CPC, CP = g.FindCriticalPath('a','n')
    print(CP)
    print(CPL)
    print(CPC)
    print(g.FindStatusReport('a', 340))
