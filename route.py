import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
import requests
from math import radians, sin, cos, sqrt, atan2
import mysql.connector
from geopy.distance import geodesic
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '@MYsql23!',
    'database': 'Food',
}
connection = mysql.connector.connect(
    host=db_config['host'],
    user=db_config['user'],
    password=db_config['password'],
    database=db_config['database']
)

def get_coordinates(city_name):
    url = f"https://nominatim.openstreetmap.org/search?q={city_name}&format=json&limit=1"
    try:
        response = requests.get(url, verify=False)
        data = response.json()
        if data:
            latitude, longitude = float(data[0]['lat']), float(data[0]['lon'])
            return latitude, longitude
        else:
            print(f"Unable to get coordinates for {city_name}")
            return None
    except Exception as e:
        print(f"Error: {e}")
        return None

def haversine_distance(coord1, coord2):
    # Haversine formula to calculate distance between two coordinates
    R = 6378.14  # Earth radius in kilometers

    lat1, lon1 = radians(coord1[0]), radians(coord1[1])
    lat2, lon2 = radians(coord2[0]), radians(coord2[1])

    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c  # Distance in kilometers
    return distance
def route_op():
    ngo_name = input("Enter your NGO name: ")
    ngo_state = input("Enter your State: ")
    ngo = input("Enter your City: ")
    donor = pd.read_sql(f"Select * from Donor where State='{ngo_state}'", con=connection)
    loc1 = donor[['NameOfRestaurant', 'City']]

    # Input the names of the cities
    # Get the coordinates using the requests library
    coordinates1 = get_coordinates(ngo)
    G = nx.Graph()

    for _, i in loc1.iterrows():  # Using iterrows to iterate over rows
        coordinates2 = get_coordinates(["City"])
        if coordinates1 and coordinates2:
            # Calculate and print the distance between the two locations
            distance = geodesic(coordinates1, coordinates2).km
            print(f"The distance between {i['NameOfRestaurant']} and {ngo_name} is approximately {distance:.2f} kilometers.")

            # Build a graph with weighted edges based on the calculated distance
            G.add_nodes_from([i['NameOfRestaurant'], ngo_name])
            G.add_edge(i['NameOfRestaurant'], ngo_name, weight=distance)

            for _, j in loc1.iterrows():
                if i['NameOfRestaurant'] != j['NameOfRestaurant']:
                    coordinates3 = get_coordinates(j['City'])
                    distance = geodesic(coordinates2, coordinates3).km
                    print(f"The distance between {j['NameOfRestaurant']} and {i['NameOfRestaurant']} is approximately {distance:.2f} kilometers.")

                    # Build a graph with weighted edges based on the calculated distance
                    G.add_nodes_from([j['NameOfRestaurant'], i['NameOfRestaurant']])
                    G.add_edge(i['NameOfRestaurant'], j['NameOfRestaurant'], weight=distance)

    # Visualize the graph
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=700, node_color='skyblue', font_size=8, font_color='black')
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.show()

    mst = nx.minimum_spanning_tree(G)

    # Visualize the optimized routes
    pos_mst = nx.spring_layout(mst)
    nx.draw(mst, pos_mst, with_labels=True, font_weight='bold', node_size=700, node_color='skyblue', font_size=8,
            font_color='black')
    labels_mst = nx.get_edge_attributes(mst, 'weight')
    nx.draw_networkx_edge_labels(mst, pos_mst, edge_labels=labels_mst)
    plt.show()
    print(mst)

    shortest_paths = nx.shortest_path(mst, source=ngo_name)

    # Print the optimized routes
    print("Optimized Routes:")
    for target, path in shortest_paths.items():
        if target != ngo_name:
            print(f"From {ngo_name} to {target}: {' -> '.join(path)}")


