General Information
---------------------

This software has been written to provide project scheduling using Critical Path Method. It considers a bunch of activities on arrows as an input,  converts them to a directed graph, and then finds the longest path with respect to time duration (in case of multiple longest paths, we consider the one with minimum cost) - which is the critical path. The software also accomodates different working schedules at different sites of the project and proper calendar dates instead of mere time durations. Also, the software gives the manager status report based on the date given as input.

Note that the longest path method to find the critical path is an optimized version with time complexity O(V+E). 
