# Bellman Ford algorithm for traversing a graph with negative weights. This
# can detect a negative weight cycle. Runs in O(Nm) to find the shortest path
# between two points.

def bellman_ford(graph, source):
  # min distance to get from the source point to each vertex.
  d = {}

  # Intialize each node in the distance dictionary to be infinity.
  for node in graph:
    d[node] = float('inf')
  d[source] = 0

  # A graph can have at most V-1 edges to have a min path.
  for i in range(len(graph) - 1):
    for u in graph:
      for v in graph[u]:
        # Get the edge and its corresponding weight.
        w = graph[u][v]

        # Check to see if the source vertex + weight is lower than the current
        # weight to get to that vertex.
        if d[u] != float('inf') and d[u] + w < d[v]:
          d[v] = d[u] + w

  neg_cycle_found = False
  for u in graph:
    for v in graph[u]:
      w = graph[u][v]
      # A negative weight cycle is where taking 2 sides of a triangle is faster
      # than taking one.
      if d[u] != float('inf') and d[u] + w < d[v]:
        neg_cycle_found = True

  return d, neg_cycle_found

if __name__ == '__main__':
  graph = {
    's' : { 'b' : 5 },
    'a' : { 'd' : 4, 'c' : -6 },
    'b' : { 'a' : 3, 'c' : 8 },
    'c' : { 'b' : 2, 'e' : 5 },
    'd' : { 'a' : 3 },
    'e' : { }
  }

  d, n = bellman_ford(graph, 's')
  ordered = []
  for c in ['s', 'a', 'b', 'c', 'd', 'e']:
    ordered.append((c, d[c]))
  print(ordered)

  if n:
    print('Negative weight cycle found.')
