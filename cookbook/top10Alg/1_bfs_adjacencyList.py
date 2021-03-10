#page 205 from handson datastruct and algo

# algorithm
# 1. Add the vertex to start the breadth-first search to the empty queue. Mark that vertex visited.
# 2. Extract a vertex from the queue and add its neighbors to the queue if that isn't marked visited.
# 3. Repeat step 2 until the queue is empty.

from collections import deque

def bfs(graph, root):
    """This takes in a dictionary based graph structure and a root node and performs a breadth first search
    BFS adds items to a queue and performs a FIFO operation on them (process and add neighbors to the need to visit queue)

    Args:
        graph ([type]): [description]
        root ([type]): [description]
    """
    #visited vertices is initially empty
    visited_vertices = []

    #our queue (FIFO) is set with the root node as initial element
    graph_queue = deque([root])

    # add root node to the visisted vertices 
    visited_vertices.append(root)

    #set active node to root
    node = root

    while len(graph_queue) > 0:
        #we need to use deque.popleft() to get out the first element added
        node = graph_queue.popleft()
        #we need to extract all of that nodes adjacent nodes (dictionary structure)
        adj_nodes = graph[node]

        #cast into a set to rid of duplicates and the .difference method returns items that only exist in adj_nodes set---dont want to visit twice
        remaining_elements = set(adj_nodes).difference(set(visited_vertices))

        #process the remaining elements
        if len(remaining_elements) > 0:
            for element in sorted(remaining_elements):
                visited_vertices.append(element)
                graph_queue.append(element)
    
    return visited_vertices






if __name__ == "__main__":
    graph = dict()
    graph['A'] = ['B', 'C']
    graph['B'] = ['A', 'C', 'E']
    graph['C'] = ['A', 'B', 'E', 'F']
    graph['E'] = ['B', 'C']
    graph['F'] = ['C']

    print(bfs(graph, 'A'))