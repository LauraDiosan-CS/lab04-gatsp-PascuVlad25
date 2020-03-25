
def calculate_route_length(current_route, network):
    route_length = network[current_route[-1]][current_route[0]]['cost']
    for index in range(len(current_route)-1):
        city1 = current_route[index]
        city2 = current_route[index+1]
        route_length += network[city1][city2]['cost']

    return route_length