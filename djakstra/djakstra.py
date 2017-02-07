#!/usr/bin/python

def djakstra(graph,start,end):

    Q = set() #vertex set
    dist = dict() #distance from start
    prev = dict() #previous vertex
    adj = dict() #adjacency list
    result = set()
    
    for i in range(1,len(graph)):
        adj[str(graph[i][0])] = []
        for j in range(1,len(graph[0])):
            if graph[i][j] != None:
                adj[str(graph[i][0])].append(graph[0][j])

    #initializing
    for i in range(1,len(graph[0])):
        dist[graph[0][i]] = "inf" #set distance of all vertices to infinity
        prev[graph[0][i]] = None  #leave previous vertex field undefined
        Q.add(graph[0][i]) #add vertex to the Set

    dist[start] = 0; #set distance of start vertex to 0

    while(len(Q) != 0):
        u = minimum(dist, Q)
        #print "u="+u
        try:
            Q.remove(u)
        except:
            pass
        for i in range(0,len(adj[u])):
            #print adj[u]
            v = adj[u][i]
            #print (u+","+v)
            if(u != "old" and dist[u] != "inf"):
                alt = dist[u] + int(length(graph,u,v))
                if (dist[v] == "inf") or (alt < dist[v]):
                    #print "v="+v
                    dist[v] = alt
                    prev[v] = u
        u = "old" 
    print path(prev,start,end)
    return 

def path(prev,start,end):
    paths = []
    while end != start:
        paths.append(end)
        end = prev[end]
    paths.append(end)
    return paths[::-1]
        

def length(graph, u, v): #returns length of edge
    found = False
    for i in range(1,len(graph)):
        if graph[i][0] == u :
            for j in range(1,len(graph)):
                if graph[0][j] == v:
                    if graph[i][j] != None:
                        result = int(graph[i][j])
                        found = True
                        break
    if found == True:
        return result
    else:
        raise ValueError("Edge not found("+u+","+v+")")

def minimum(dic, keys): #returns minimum of values of given dictionary with given set of keys
    a = []
    for i in keys:
        a.append(dic[i])
    return (dic.keys()[dic.values().index(min(a))])

def Main():
    graph = [["","v1","v2","v3","v4","v5"],["v1",None,3,None,None,2],["v2",3,None,4,1,None],["v3",None,4,None,1,None],["v4",None,1,1,None,3],["v5",2,None,None,3,None]]
    djakstra(graph,"v1","v3");
    return

if __name__ == "__main__":
    Main()
