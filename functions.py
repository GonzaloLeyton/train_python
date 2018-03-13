from collections import defaultdict

def dijkstra(graph, start, maxD=float("inf")):
    tdist = defaultdict(lambda: float("inf"))
    tdist[start] = 0

    preceding_node = {}
    unvisited = graph.nodes.copy()

    while unvisited:
      current = unvisited.intersection(tdist.keys())
      if not current: break
      min_node = min(current, key=tdist.get)
      unvisited.remove(min_node)

      for edge in graph.edges[min_node]:
        d = tdist[min_node] + graph.distance(min_node, edge)
        if (tdist[edge] > d and maxD >= d) or (tdist[edge] == 0 and edge == start and maxD >= d):
          tdist[edge] = d
          preceding_node[edge] = min_node

    return tdist, preceding_node

def min_path(graph, start, end, maxD=float("inf")):
    tdist, preceding_node = dijkstra(graph, start, maxD)

    dist = tdist[end]
    backpath = [end]
    try:
      while end != start:
        end = preceding_node[end]
        backpath.append(end)
      path = list(reversed(backpath))
    except KeyError:
      path = None

    if dist == float("inf"):
      return "NO SUCH ROUTE", []
    return dist, path

def distance_route(graph, *args):
  pivot = args[0]
  total = 0
  try:
    for item in args[1:]:
      total += graph.distance(pivot, item)
      pivot = item
    return total
  except:
    return "NO SUCH ROUTE"

def dist_to(graph, *args): return min_path(graph, *args)[0]
def path_to(graph, *args): return min_path(graph, *args)[1]
def distance(graph, *args): return distance_route(graph, *args)
