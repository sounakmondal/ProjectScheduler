import Graph
import networkx as nx
import datetime

if __name__ == '__main__':
    g = Graph.ActivityGraph()
    g.ReadEdgeList('HydroElectric.txt')
    # g.GetAttribute('label')
    # g.DrawGraph()
    datestart = input("Enter start date (mmm dd yyyy format): ")
    startdate= datetime.datetime.strptime(datestart, '%b %d %Y')
    g.FindDistCost('a','n', startdate )
    CPL, CPC, CP = g.FindCriticalPath('a','n')
    print("The critical path is: ")
    print(CP)
    enddate = startdate + datetime.timedelta(days = CPL)
    print(enddate.strftime('End date: %b %d %Y'))
    print("Total cost along critical path in thousand INRs is: "+str(CPC))
    duration = input("Enter the number of days since project start: " )
    print("The nodes that are presently awaiting completion are: ")
    print(g.FindStatusReport('a', int(duration)))
