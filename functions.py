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
  

def num_trips(graph, start, end, total_stops, mode, maxD=1e309):

  stops = 0
  trips = 0
  next_nodes = set(graph.edges[start])
  print "start", start

  print next_nodes
  for item in next_nodes:
    print "item", item
    if graph.near_to(item, end):
      print "FOUND END:", item
      trips += 1
    else:
      stops += 1
      print "stops", stops
      next2_nodes = set(graph.edges[item])
      for item2 in next2_nodes:
        print "item2", item2
        if graph.near_to(item2, end):
          print "FOUND END2:", item2
          trips += 1
        else:
          stops += 1
          print "stops", stops
          next3_nodes = set(graph.edges[item2])
          for item3 in next3_nodes:
            print "item3", item3
            if graph.near_to(item3, end):
              print "FOUND END2:", item2
              trips += 1
            else:
              stops += 1
              print "stops", stops
              next4_nodes = set(graph.edges[item3])
              for item4 in next4_nodes:
                print "item4", item4
                if graph.near_to(item4, end):
                  print "FOUND END4:", item4
                  trips += 1

  print "FINAL"
  print "stops", stops
  print "trips", trips


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
