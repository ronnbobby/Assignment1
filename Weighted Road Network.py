# Weighted Road Network using Adjacency List

# Number of locations
n = int(input("Enter number of locations: "))

# Create adjacency list
graph = {}

# Accept location names
for i in range(n):
    location = input(f"Enter location {i + 1}: ")
    graph[location] = []

# Number of roads
m = int(input("Enter number of roads: "))

# Store roads separately to calculate unique road weight
roads = []

# Accept roads
for i in range(m):
    print(f"\nEnter details for road {i + 1}:")
    location1 = input("Enter first location: ")
    location2 = input("Enter second location: ")
    distance = float(input("Enter distance: "))

    # Add road to adjacency list
    graph[location1].append((location2, distance))
    graph[location2].append((location1, distance))

    # Store each road only once
    roads.append((location1, location2, distance))


# Display adjacency list
print("\n--- Weighted Road Network ---")
for location in graph:
    print(location, "->", graph[location])


# Display all roads with distances
print("\n--- All Roads ---")
for location1, location2, distance in roads:
    print(f"{location1} <-> {location2} : {distance} km")


# Find total weight of all unique roads
total_weight = sum(distance for _, _, distance in roads)

print("\nTotal weight of all unique roads:", total_weight, "km")