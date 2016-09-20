graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}


def dfs_paths(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        print("===========");
        print "vertex = %s" %  vertex;
        print "path = %s"  % path;
        print("===========");
        for next in graph[vertex] - set(path):
            print "next = %s" % (next) ;
            if next == goal:
                #yield path + [next]
                print "+++++++"
                print path + [next]
            else:
                print "-------"
                print stack;
                stack.append((next, path + [next]))
                print stack;

x = dfs_paths(graph, 'A', 'F')
#for i in x:
   #print i

