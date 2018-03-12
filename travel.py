from classes import Graph
from functions import *

def main():
    g = Graph()

    g = g.from_file('./graph.txt')

    print "Nodes: ", g.nodes
    print "Edges: ", g.edges
    print "Distances: ", g.distances
    # print dijkstra(g, "A")

    print 
    print "--------------"
    print 

    # # Resolvemos primer grupo de preguntas 1-5
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
    print "num_stops", num_trips(g, "C", "C", 3, "max")


    # The number of trips starting at A and ending at C with exactly 4 stops.  In the sample data below, there are three such trips: A to C (via B,C,D); A to C (via D,C,D); and A to C (via D,E,B).

    

    # The number of different routes from C to C with a distance of less than 30.  In the sample data, the trips are: CDC, CEBC, CEBCDC, CDCEBC, CDEBC, CEBCEBC, CEBCEBCEBC.


main()
