from collections import defaultdict

def dijkstra(graph, start, maxD=1e309):
    """Returns a map of nodes to distance from start and a map of nodes to
    the edge node that is closest to start."""
    # total distance from origin
    tdist = defaultdict(lambda: 1e309)
    tdist[start] = 0
    # edges that is nearest to the origin
    preceding_node = {}
    unvisited = graph.nodes.copy()

    while unvisited:
      current = unvisited.intersection(tdist.keys())
      if not current: break
      min_node = min(current, key=tdist.get)
      unvisited.remove(min_node)

      # print "min_node", min_node
      # print "edges", graph.edges[min_node]

      for edge in graph.edges[min_node]:
        d = tdist[min_node] + graph.distance(min_node, edge)
        if (tdist[edge] > d and maxD >= d) or (tdist[edge] == 0 and edge == start and maxD >= d):
          tdist[edge] = d
          preceding_node[edge] = min_node

    return tdist, preceding_node

def min_path(graph, start, end, maxD=1e309):
    """Returns the minimum distance and path from start to end."""
    tdist, preceding_node = dijkstra(graph, start, maxD)
    
    # print tdist, preceding_node

    dist = tdist[end]
    backpath = [end]
    try:
      while end != start:
        end = preceding_node[end]
        backpath.append(end)
      path = list(reversed(backpath))
    except KeyError:
      path = None

    if dist == 1e309:
      return "NO SUCH ROUTE", []

    return dist, path


def num_trips(graph, start, end, stops, mode, maxD=1e309):

  next_nodes = set(graph.edges[start])
  
  print "start", start
  print "end", end
  print "next_nodes", next_nodes

  trips = 0
  current_stops = 0
  
  for item in next_nodes:
    if item == end:
      trips += 1
      return trips
    else:
      current_stops += 1
      if current_stops > stops:
        print "max stops reached"
        return False
      
      trips += num_trips(graph, item, end, stops, mode, maxD)

  return trips



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
