graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}

visit = set()

visited = [] 
queue = []     

def bfs(visited, graph, node):
  visited.append(node)
  queue.append(node)

  while queue:
    m = queue.pop(0) 
    print (m, end = " ") 

    for n in graph[m]:
      if n not in visited:
        visited.append(n)
        queue.append(n)

def dfs(visit, graph, node):  
    if node not in visit:
        print (node,end=" ")
        visit.add(node)
        for n in graph[node]:
            dfs(visit, graph, n)

print("BFS is:")
bfs(visited, graph, '5') 
print('\n')
print("DFS is:")
dfs(visit, graph, '5')
