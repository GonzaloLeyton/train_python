from classes import Graph
from functions import dijkstra, dist_to, path_to, distance, min_path, num_trips

def main():
    g = Graph()

    g.add_node("A")
    g.add_node("B")
    g.add_node("C")
    g.add_node("D")
    g.add_node("E")

    g.add_distance("A", "B", 5)
    g.add_distance("B", "C", 4)
    g.add_distance("C", "D", 8)
    g.add_distance("D", "C", 8)
    g.add_distance("D", "E", 6)
    g.add_distance("A", "D", 5)
    g.add_distance("C", "E", 2)
    g.add_distance("E", "B", 3)
    g.add_distance("A", "E", 7)

    print "Nodes: ", g.nodes
    print "Edges: ", g.edges
    # print "Distances: ", g.distances
    # print dijkstra(g, "A")

    print 
    print "--------------"
    print 

    # Resolvemos primer grupo de preguntas 1-5
    # print "The distance of the route A-B-C", distance(g, "A", "B", "C") 
    # print "The distance of the route A-D", distance(g, "A", "D") 
    # print "The distance of the route A-D-C", distance(g, "A", "D", "C") 
    # print "The distance of the route A-E-B-C-D", distance(g, "A", "E", "B", "C", "D") 
    # print "The distance of the route A-E-D", distance(g, "A", "E", "D") 
    # print


    # # Respondemos preguntas 8 y 9
    # print "The length of the shortest route from A to C.", dist_to(g, "A", "C")
    # print "The length of the shortest route from B to B.", dist_to(g, "B", "B")
    # print "The length of the shortest route from E to A.", dist_to(g, "E", "A")
    # print



    # The number of trips starting at C and ending at C with a maximum of 3 stops.  In the sample data below, there are two such trips: C-D-C (2 stops). and C-E-B-C (3 stops)

    # print "path_to", min_path(g, "C", "C")
    print "num_stops", num_trips(g, "A", "D", 3, "max")


    # The number of trips starting at A and ending at C with exactly 4 stops.  In the sample data below, there are three such trips: A to C (via B,C,D); A to C (via D,C,D); and A to C (via D,E,B).

    

# The number of different routes from C to C with a distance of less than 30.  In the sample data, the trips are: CDC, CEBC, CEBCDC, CDCEBC, CDEBC, CEBCEBC, CEBCEBCEBC.



main()
