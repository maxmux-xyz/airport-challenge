# input = [
#   ["SJC", "DFW"],
#   ["LAX", "SFO"],
#   ["ATL", "SJC"],
#   ["EWR", "ATL"],
#   ["SFO", "EWR"]
# ] 
# every node has at most 1 incoming and at most 1 outgoing edge
# ^lift this restriction

# output:
# ["LAX", "SFO", "EWR", "ATL", "SJC", "DFW"]

# part 2:
input = [
    ["SJC", "DFW"],
    ["LAX", "SFO"],
    ["ATL", "SJC"],
    ["EWR", "ATL"],
    ["SFO", "EWR"],
    ["ATL", "DFW"],
    ["YYZ", "EWR"],
    ["ATL", "MIA"]
 ]
# input = [
#     ["SJC", "DFW"],
#     ["LAX", "SFO"],
#     ["ATL", "SJC"],
#     ["ATL", "TEST1"],
#     ["ATL", "TEST2"],
#     ["TEST1", "TEST3"],
#     ["EWR", "ATL"],
#     ["SFO", "EWR"],
#     ["ATL", "DFW"],
#     ["YYZ", "EWR"],
#     ["ATL", "MIA"]
#  ]

# possible trips:
# * ["LAX", "SFO", "EWR", "ATL", "SJC", "DFW"] *
# ["LAX", "SFO", "EWR", "ATL", "DFW"]
# ["YYZ", "EWR", "ATL", "MIA"]

class Airport:
    def __init__(self, name, t) -> None:
        self.name = name
        # this is a list of airports
        self.t = t

def build_airport_graph(routes):
    airports = {}
    froms = []
    tos = []
    for route in routes:
        # Build the graph
        f, t = route[0], route[1]
        if airports.get(t) is None:
            airports[t] = Airport(t, [])
        if airports.get(f) is None:
            airports[f] = Airport(f, [])
        
        airports[f].t.append(airports[t])

        # froms & tos
        froms.append(f)
        tos.append(t)
    return airports, froms, tos

def find_starting_points(froms, tos):
    starting_airports = []
    for f in froms:
        if f not in tos:
            starting_airports.append(f)
    
    if len(starting_airports) == 0:
        print("we have a problem")
    
    return starting_airports

def compute_routes(starting_airports, airports):
    candidate_routes = {}
    for starting_airport in starting_airports:

        # BFS queue of routes
        queue = [
            [airports[starting_airport]]
        ]

        while len(queue) > 0:
            currentRoute = queue[0]
            for airport in currentRoute[-1].t:
                # terminus
                if len(airport.t) == 0:
                    new_final_route = currentRoute + [airport]
                    if candidate_routes.get(len(new_final_route)) is None:
                        candidate_routes[len(new_final_route)] = [new_final_route]
                    else:
                        candidate_routes[len(new_final_route)].append(new_final_route)
                        # candidate_routes.append(new_final_route)
                else:
                    # for new_airport in airport.t:
                    new_route_to_explore = currentRoute + [airport]
                    queue.append(new_route_to_explore)

            queue = queue[1:]

    return candidate_routes

def findRoute(routes):
    airports, froms, tos = build_airport_graph(routes)
    starting_airports = find_starting_points(froms, tos)

    candidate_routes = compute_routes(starting_airports, airports)
    print(candidate_routes[max(candidate_routes.keys())])
    print([a.name for a in candidate_routes[max(candidate_routes.keys())][0]])

    # for route in candidate_routes:
    #     print(len(route))
    #     print([a.name for a in route])
    #     print()
    




    # # This finds the longest route
    # candidateRoutes = {}
    # for starting_airport in starting_airports:
    #     output = []
    #     visited_airports = [airports[starting_airport]]
    #     airports_to_visit = [airports[starting_airport].name]

    #     while len(visited_airports) > 0:
    #         current_airport = visited_airports[0]
    #         output.append(current_airport.name)

    #         for a in current_airport.t:
    #             if a.name not in airports_to_visit:
    #                 if len(a.t) == 0:
    #                     # Next airport is terminus, save that route
    #                     newRoute = output + [a.name]
    #                     if candidateRoutes.get(len(newRoute)) is None:
    #                         candidateRoutes[len(newRoute)] = [newRoute]
    #                     else:
    #                         candidateRoutes[len(newRoute)].append(newRoute)
    #                 else:
    #                     airports_to_visit.append(a.name)
    #                     visited_airports.append(a)

    #         visited_airports = visited_airports[1:]
        
    #     if candidateRoutes.get(len(output)) is None:
    #         candidateRoutes[len(output)] = [output]
    #     else:
    #         candidateRoutes[len(output)].append(output)

    # return candidateRoutes[max(candidateRoutes.keys())]


# Challenge 2
# Challenge 1
# class Airport:
#     def __init__(self, name, f, t) -> None:
#         self.name = name
#         self.f = f
#         self.t = t


# def findRoute(routes):
#     airports = {}
#     froms = []
#     tos = []
#     for route in routes:
#         # ["SJC", "DFW"]

#         # Build the graph
#         f, t = route[0], route[1]
#         if airports.get(f) is None:
#             airports[f] = Airport(f, "", "")
#         if airports.get(t) is None:
#             airports[t] = Airport(t, "", "")
        
#         airports[f].t = airports[t]
#         airports[t].f = airports[f]

#         # froms & tos
#         froms.append(f)
#         tos.append(t)

#     # Decide starting point
#     # take the airport in tos that is not in from list
#     starting_airport = ""
#     for f in froms:
#         if f not in tos:
#             starting_airport = f
#             break
    
#     if starting_airport == "":
#         print("we have a problem")

#     current_airport = airports.get(starting_airport)
#     if current_airport is None:
#         print("We have another problem")

#     output = []
#     while True:
#         output.append(current_airport.name)
#         if current_airport.t == "":
#             break
#         current_airport = current_airport.t
    
#     return output



o = findRoute(input)
print(o)


