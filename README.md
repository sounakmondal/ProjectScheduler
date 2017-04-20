General Information
---------------------

This software has been written to provide project scheduling using Critical Path Method. It considers a bunch of activities on arrows as an input,  converts them to a directed graph, and then finds the longest path with respect to time duration (in case of multiple longest paths, we consider the one with minimum cost) - which is the critical path. The software also accomodates different working schedules at different sites of the project and proper calendar dates instead of mere time durations. Also, the software gives the manager status report based on the date given as input.

Note that the longest path method to find the critical path is an optimized version with time complexity O(V+E). 


Details
---------

The software tries to optimally find the critical path based on the property that the critical path in the AOE graph of the activities is the longest path in the directed acyclic graph based on activity duration. This can be done in O(V+E) time complexity using dynamic programming. Note that in case of multiple critical paths, the software adopts the one with minimum cost.

Here is the generic algorithm to find the longest path in a Directed Acyclic Graph:

1) Initialize dist[] = {NINF, NINF, ….} and dist[s] = 0 where s is the source vertex. Here NINF means negative infinite.
2) Create a toplogical order of all vertices.
3) Do following for every vertex u in topological order.
………..Do following for every adjacent vertex v of u
………………if (dist[v] < dist[u] + weight(u, v))
………………………dist[v] = dist[u] + weight(u, v)
4) dist[d] is the longest path length where t is the destination
5) Maintaining an ancestor list of all nodes and traversing from destination d to source d gives the longest path (in reverse).

Note that the duration also takes into account the number of days per week corresponding site personnel work.

The software also supports a system delivering status report at various time durations from project start which shows us the completed activities and nodes along with the nodes expecting completion. This can easily be deduced from the dynamic programming table built during critical path finding.

Instructions
-------------

Download all files in the repo, put them in a common directory and run Driver.py using Python 3.5.1 or higher.
