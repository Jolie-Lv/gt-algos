# Floyd-Warshall algorithm for detecting all shortest pairs in a graph. It
# returns all of the shortest pairs for each vertex. Also detects negative
# weight cycles. Runs in O(N^3).

INF = float('inf')

def floyd_warshall(graph):
  # Copy the graph over. This has the shortest paths between each vertex when
  # there's no intermediate vertices.
  d = graph

  # Add intermediate vertices from 0...K. Look for the shortest path between
  # two vertices if a vertex k is included in the shortest path.
  for k in range(len(graph)):
    # Iterate through all source vertices.
    for i in range(len(graph)):
      # Iterate through all destination vertices.
      for j in range(len(graph)):
        # The current distance between two nodes is either the previously
        # caluclated distance, or the distance including the new vertex k.
        d[i][j] = min(d[i][j], d[i][k] + d[k][j])
  return d


if __name__ == '__main__':
  #         s,   a,   b,   c,   d,   e
  graph = [[0,   INF, 5,   INF, INF, INF],
           [INF, 0,   INF, -6,  4,   INF],
           [INF, 3,   0,   8,   INF, INF],
           [INF, INF, 2,   0,   INF, 5  ],
           [INF, 3,   INF, INF, 0,   INF],
           [INF, INF, INF, INF, INF, 0  ]]

  d = floyd_warshall(graph)

  # Print shortest path.
  for row in d:
    val = ''
    for col in row:
      val += ' ' * (col >= 0 and col != INF) + str(col) + '\t'
    print(val)
