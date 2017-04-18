import networkx as nx
import numpy as np
from matplotlib import  pyplot as plt
from math import inf
import datetime
from collections import Counter

class ActivityGraph(object):

    def __int__(self):
        self.Graph = None
        self.topological_order = None
        self.time = None
        self.costIncurred = None
        self.predecessor = None
        self.startDate = None

    def ReadEdgeList(self, fileName):
        self.Graph = nx.read_edgelist(fileName, nodetype = str, data=[('time',float), ('cost', float), ('waw', int),], create_using=nx.DiGraph())
        for (u,v) in self.Graph.edges(data=False):
            self.Graph[u][v]['time'] *= 30
        self.topological_order = nx.topological_sort(self.Graph)

    def DrawGraph(self):
        nx.draw_networkx(G=self.Graph, with_labels=True, arrows=True)
        plt.draw()
        plt.show()

    '''def GetAttribute(self, attribute):
        print(nx.get_node_attributes(self.Graph, attribute))'''

    def FindAllSimplePaths(self):
        return nx.all_simple_paths(self.Graph, source='1', target='24')

    def FindDistCost(self, source, destination, parameter='time'):
        datestart = input("Enter start date (mmm dd yyyy format): ")
        self.startDate= datetime.datetime.strptime(datestart, '%b %d %Y')
        nodeList = self.Graph.nodes(data=False)
        dist = {}
        cost = {}
        neighbor = {}
        for u in nodeList:
            dist[u]= -100
            cost[u] = inf
        dist[source] = 0
        cost[source] = 0
        for u in self.topological_order:
            adj_nodes = [x for x in nodeList if self.Graph.has_edge(u, x) == True]
            if dist[u] < inf:
                presentDate = self.startDate + datetime.timedelta(days = dist[u])
            else:
                presenDate = None
            for v in adj_nodes:
                if presentDate is not None and self.Graph[u][v]['waw']==0 :
                    eDate = presentDate + datetime.timedelta(days = self.Graph[u][v][parameter])
                    daysCounter = Counter()
                    for i in range((eDate - presentDate).days+1):
                        daysCounter[(presentDate + datetime.timedelta(i)).strftime('%a')] += 1                    
                    holidays = daysCounter['Sun'] + daysCounter['Sat']
                else:
                    holidays = 0
                if dist[v] < dist[u] + self.Graph[u][v][parameter] + holidays:
                    dist[v] = dist[u] + self.Graph[u][v][parameter] + holidays
                    neighbor[v] = u
                    cost[v] = cost[u] + self.Graph[u][v]['cost']
                elif dist[v] == dist[u] + self.Graph[u][v][parameter] + holidays and cost[v] > cost[u] + self.Graph[u][v]['cost']:
                    '''we are considering minimum cost for same length path'''
                    neighbor[v] = u
                    cost[v] = cost[u] + self.Graph[u][v]['cost']
        self.time = dist
        self.costIncurred = cost
        self.predecessor = neighbor

    def FindCriticalPath(self, source, destination):
        criticalPath = []
        criticalPathLength = -1
        criticalPathLength = self.time[destination]
        n = destination
        #criticalPath.append(n)
        while n != source:
            criticalPath.append((self.predecessor[n],n))
            n = self.predecessor[n]
        criticalPath.reverse()
        criticalPathCost = self.costIncurred[destination]
        nonCriticalEdges = list(set(self.Graph.edges(data=False))-set(criticalPath))
        plt.figure(figsize=(20,20))
        pos = nx.spectral_layout(self.Graph)
        nx.draw_networkx_nodes(self.Graph, pos, cmap=plt.get_cmap('jet'), font_size = 4)
        nx.draw_networkx_edges(self.Graph, pos, edgelist=criticalPath, edge_color='r', arrows=True, font_size = 1)
        nx.draw_networkx_edges(self.Graph, pos, edgelist=nonCriticalEdges, arrows=True)
        nx.draw_networkx_labels(self.Graph, pos)
        edge_labels=dict([((u,v,),str(d['time'])+","+str(d['cost']))
                 for u,v,d in self.Graph.edges(data=True)])
        nx.draw_networkx_edge_labels(self.Graph, pos, edge_labels = edge_labels)
        plt.axis('off')
        plt.show()
        return criticalPathLength, criticalPathCost, criticalPath

    def FindStatusReport(self, source, timeElapsed):
        workingNodes=[]
        completedPaths=[]
        colors=[]
        for u in self.Graph.nodes():
            if self.time[u]>=timeElapsed and self.time[self.predecessor[u]]<timeElapsed:
                workingNodes.append(u)
                colors.append('green')
            elif self.time[u]<timeElapsed:
                completedPaths.extend([(a,b) for (a,b) in self.Graph.edges([u]) if self.Graph[a][b]['time']+self.time[u]<=timeElapsed])
                colors.append('cyan')
            else:
                colors.append('red')
        print(completedPaths)
        incompeleteEdges = list(set(self.Graph.edges(data=False))-set(completedPaths))
        pos = nx.spectral_layout(self.Graph) 
        nx.draw_networkx_nodes(self.Graph, pos, cmap=plt.get_cmap('jet'), node_color=colors)        
        nx.draw_networkx_labels(self.Graph, pos)
        nx.draw_networkx_edges(self.Graph, pos, edgelist=completedPaths, edge_color='b', arrows=True)
        nx.draw_networkx_edges(self.Graph, pos, edgelist=incompeleteEdges , arrows=True)
        edge_labels=dict([((u,v,),str(d['time'])+","+str(d['cost']))
                 for u,v,d in self.Graph.edges(data=True)])
        nx.draw_networkx_edge_labels(self.Graph, pos, edge_labels = edge_labels)
        plt.axis('off')
        plt.show()
        return workingNodes
        
        
