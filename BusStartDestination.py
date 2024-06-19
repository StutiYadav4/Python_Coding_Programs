def shortest_distance_between_stops(distance, start, destination):
    if start > destination:
        start, destination = destination, start
    clockwise_distance = sum(distance[start:destination])
    counterclockwise_distance = sum(distance[destination:] + distance[:start])
    return min(clockwise_distance, counterclockwise_distance)

distance = [1, 2, 3, 4]
start = 0
destination = 1
print(shortest_distance_between_stops(distance, start, destination))  # Output: 4


