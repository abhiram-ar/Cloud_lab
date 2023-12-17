def get_node_names():
    num_nodes = int(input("Enter the number of nodes: "))
    node_names = []

    for i in range(num_nodes):
        node_name = input(f"Enter name for node {i+1}: ")
        node_names.append(node_name)

    return node_names

def get_user_input(node_names):
    network = {}

    for node_name in node_names:
        distances = {}

        for dest_name in node_names:
            if node_name == dest_name:
                distances[dest_name] = 0
            else:
                distance = int(input(f"Enter distance from node {node_name} to node {dest_name}: "))
                distances[dest_name] = distance

        network[node_name] = distances

    return network

def bellman_ford(network):
    nodes = list(network.keys())
    num_nodes = len(nodes)

    for _ in range(num_nodes):
        for node in nodes:
            for neighbor in nodes:
                for dest in nodes:
                    if network[node][neighbor] + network[neighbor][dest] < network[node][dest]:
                        network[node][dest] = network[node][neighbor] + network[neighbor][dest]
                        print_distance_vector_table(network, f"Update: {node} -> {dest}")

def print_distance_vector_table(network, message):
    print(f"\n{message}")
    print("\t"+"\t".join(network.keys()))
    for node in network:
        print(node+"\t"+"\t".join(str(network[node][dest]) if network[node][dest] < 1000 else '∞' for dest in network))

node_names = get_node_names()

network = get_user_input(node_names)

print_distance_vector_table(network, "Initial")

bellman_ford(network)

print_distance_vector_table(network, "Final")
