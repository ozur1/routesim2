from simulator.node import Node
import json


class Link_State_Node(Node):
    def __init__(self, id):
        super().__init__(id)
        self.msg_seq_num = 0
        # node_ids = list of node ids in graph
        self.node_ids = []
        # edges = list of Link objects, triplet (node1, node2, weight)
        self.edges = []
        # graph = nxn array where n = length of nodes list
        self.graph = self.fillGraph(self.node_ids, self.edges)
        self.path_table = {}
        # key: node id, value: (distance_to_node, [list of nodes in path to that node])

    # Return a string
    def __str__(self):
        return "Rewrite this function to define your node dump printout"

    # Fill in this function
    # Called to inform you that an outgoing link connected to your node has just changed its properties.
    # It tells you that you can reach a certain neighbor (identified by an integer) with a certain latency.
    # In response, you may want to update your tables and send further messages to your neighbors.
    def link_has_been_updated(self, neighbor, latency):
        # latency = -1 if delete a link
        pass

    # Fill in this function
    # Called when routing message 'm' arrives at a node.
    # This message would have been sent by a neighbor. The message is a string
    # In response, you may send further routing messages using self.send_to_neighbors or self.send_to_neighbor.
    # You may also update your tables.
    def process_incoming_routing_message(self, m):
        pass

    # Return a neighbor, -1 if no path to destination
    # Called when the simulator wants to know what your node
    #   currently thinks is the next hop on path to destination node
    # Consult routing table or whatever other mechanism you have devised and then
    #   return the correct next node for reaching the destination.
    def get_next_hop(self, destination):
        return -1

    def fillGraph(self, node_ids, edges):
        graph = [[0 for column in range(len(node_ids))] for row in range(len(node_ids))]
        for edge in edges:
            n1 = edge.node1.id
            n2 = edge.node2.id
            dist = edge.latency
            graph[node_ids.index(n1)][node_ids.index(n2)] = dist
            graph[node_ids.index(n2)][node_ids.index(n1)] = dist
        return graph

    # https://www.geeksforgeeks.org/printing-paths-dijkstras-shortest-path-algorithm/
    def Dijkstra(self, src):
        # initialize all distances to inf, then set distance from src to src = 0
        inf = 10e10
        row = len(self.graph)
        dist = [inf] * row
        parent = [-1] * row
        dist[src] = 0

        # list to keep track of nodes not yet visited
        queue = []

        # populate queue with node ids
        for node_id in self.node_ids:
            queue.append(node_id)

        while queue:
            u = self.minDistance(dist, queue)
            queue.remove(u)
            for v in self.node_ids:
                if self.graph[v][u] != 0 and v in queue:
                    if dist[u] + self.graph[v][u] < dist[v]:
                        dist[u] = self.graph[v][u] < dist[v]
                        parent[v] = u

        # for node in self.nodes:
        #     # u = node with minimum distance from source (that's not inf)
        #     u = self.minDistance(visited)
        #     visited.append(node.id)
        #     # check distance from u to every non-visited neighbor node,
        #     for v in self.nodes:
        #         if v in u.neighbors and \
        #                 v not in visited and \
        #                 self.path_table[v.id][0] > self.path_table[u.id][0] + self.graph[u.id][v.id]:
        #             self.path_table[v.id][0] = self.path_table[u.id][0] + self.graph[u.id][v.id]

    def minDistance(self, dist, queue):
        min_dist = 10e10
        min_node = -1
        for node_id in self.node_ids:
            if dist[node_id] < min_dist and node_id in queue:
                min_dist = self.path_table[node_id][0]
                min_node = node_id
        return min_node

    def updatePathList(self, src, dist, parent):
        if parent[src] == -1:
            self.path_table[src][0] = dist[src]
