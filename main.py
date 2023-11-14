from collections import defaultdict

def make_undirected_graph(edge_list):
    """ Makes an undirected graph from a list of edge tuples. """
    graph = defaultdict(set)
    for e in edge_list:
        graph[e[0]].add(e[1])
        graph[e[1]].add(e[0])
    return graph


def reachable(graph, start_node):
    """
    Returns:
      the set of nodes reachable from start_node
    """
    result = set([start_node])
    frontier = set([start_node])
    while len(frontier) != 0:
        node = frontier.pop()  # Remove a node from the frontier
        for neighbor in graph[node]: # Check each neighbor of the current node
            if neighbor not in result:
                result.add(neighbor)
                frontier.add(neighbor)
    return result





def connected(graph):
    # Check if the graph is empty
    if not graph:
        return True

    # Choose any start node
    start_node = next(iter(graph))

    # Find all nodes reachable from the start node
    reachable_nodes = reachable(graph, start_node)

    # Compare the set of all nodes in the graph with the set of reachable nodes
    all_nodes = set(graph.keys())
    return reachable_nodes == all_nodes




def n_components(graph):
    """
    Returns:
      the number of connected components in an undirected graph
    """
    visited = set()
    components = 0

    for node in graph:
        if node not in visited:
            reachable_nodes = reachable(graph, node)
            visited.update(reachable_nodes)
            components += 1

    return components

