from simulator.node import Node
import json


class Link_State_Node(Node):
    def __init__(self, id):
        super().__init__(id)
        #self.msg_seq_num = 0
        # node_ids = list of node ids in graph
        self.node_ids = set()
        # edges = list of Link objects, triplet (node1, node2, weight)
        # self.edges = []
        # graph = nxn array where n = length of nodes list
        self.graph = {}
        # self.graph = self.fillGraph(self.node_ids, self.edges)
        # self.path_table = {}
        # key: node id, value: (distance_to_node, [list of nodes in path to that node])

    # def fillGraph(self, node_ids, edges):
    #     graph = [[0 for column in range(len(node_ids))] for row in range(len(node_ids))]
    #     for edge in edges:
    #         n1 = edge.node1.id
    #         n2 = edge.node2.id
    #         dist = edge.latency
    #         graph[node_ids.index(n1)][node_ids.index(n2)] = dist
    #         graph[node_ids.index(n2)][node_ids.index(n1)] = dist
    #     return graph

    # Return a string
    def __str__(self):
        return "Node id num "+ str(self.id) + " has a graph of shape: " + str(self.graph)

    # Fill in this function
    # Called to inform you that an outgoing link connected to your node has just changed its properties.
    # It tells you that you can reach a certain neighbor (identified by an integer) with a certain latency.
    # In response, you may want to update your tables and send further messages to your neighbors.
    def link_has_been_updated(self, neighbor, latency):
        # latency = -1 if delete a link
        
        if latency == -1 and neighbor in self.neighbors:
            self.remove_all(self.id, neighbor)
            self.neighbors.remove(neighbor)
        else:
            self.neighbors.append(neighbor)
            self.node_ids.add(neighbor)
            self.add_all(self.id, neighbor, latency)
        print(self)
        outdict = {}
        outdict["node1"] = self.id
        outdict["node2"] = neighbor
        outdict["latency"] = latency
        outdict["seq_num"] = self.graph[self.id][neighbor][0]
        outdict["src"] = self.id
        self.graph[self.id][neighbor][0] += 1
        print("Sending message " + str(outdict) + " to neighbors " + str(self.neighbors))
        self.send_to_neighbors(json.dumps(outdict))
        return

    def remove_all(self, node1, node2):
        if node1 in self.graph and node2 in self.graph[node1]:
            self.graph[node1][node2][1] = 0
        if node2 in self.graph and node1 in self.graph[node2]:
            self.graph[node2][node1][1] = 0
        return

    def add_all(self, node1, node2, latency):
        if not node1 in self.graph or not node2 in self.graph[node1]:
            self.graph[node1] = {node2:[0, latency]}
        else:
            self.graph[node1][node2][1] = latency
        if not node2 in self.graph or not node1 in self.graph[node2]:
            self.graph[node2] = {node1:[0, latency]}
        else:
            self.graph[node2][node1][1] = latency
        return
    


    # Fill in this function
    # Called when routing message 'm' arrives at a node.
    # This message would have been sent by a neighbor. The message is a string
    # In response, you may send further routing messages using self.send_to_neighbors or self.send_to_neighbor.
    # You may also update your tables.
    def process_incoming_routing_message(self, m):
        # parse through message and if it's a link change then update tables and send out messages
        indict = json.loads(m)
        #print(indict["node1"])
        if not indict["node1"] in self.graph or not indict["node2"] in self.graph[indict["node1"]]:
            self.graph[indict["node1"]] = {indict["node2"]:[0, indict["latency"]]}
        if not indict["node2"] in self.graph or not indict["node1"] in self.graph[indict["node2"]]:
            self.graph[indict["node2"]] = {indict["node1"]:[0, indict["latency"]]}
        if indict["seq_num"] > self.graph[indict["node1"]][indict["node2"]][0]:
            self.graph[indict["node1"]][indict["node2"]][0] = indict["seq_num"] + 1
            if indict["latency"] == -1:
                self.remove_all(indict["node1"], indict["node2"])
            else:
                self.add_all(indict["node1"], indict["node2"], indict["latency"])
            for neighbor in self.neighbors:
                source = indict["src"]
                indict["src"] = self.id
                if neighbor != source:
                    self.send_to_neighbor(neighbor, json.dumps(indict))
        return



    # Return a neighbor, -1 if no path to destination
    # Called when the simulator wants to know what your node
    #   currently thinks is the next hop on path to destination node
    # Consult routing table or whatever other mechanism you have devised and then
    #   return the correct next node for reaching the destination.
    def get_next_hop(self, destination):
        dist, parent = self.dijkstra(self.graph, self.id)
        path = self.getPath(parent, destination, [])
        if len(path) < 2:
            return -1
        else:
            return path[1]

    # Dijkstra's algorithm adapted from https://www.geeksforgeeks.org/printing-paths-dijkstras-shortest-path-algorithm/
    def minDistance(self, dist, queue):
        minimum = float("Inf")
        min_node_id = ''
        for node_id in self.node_ids:
            if dist[node_id] < minimum and node_id in queue:
                minimum = dist[node_id]
                min_node_id = node_id
        return min_node_id

    def dijkstra(self, graph, src):
        dist = {}
        parent = {}

        for node_id in self.node_ids:
            dist[node_id] = float("Inf")
            parent[node_id] = -1

        dist[src] = 0

        queue = []
        for node_id in self.node_ids:
            queue.append(node_id)
        print("Queue is:")
        print(queue)
        while queue:
            u = self.minDistance(dist, queue)
            if u == '':
                break
            queue.remove(u)
            for v in self.node_ids:
                if graph[u][v][1] != 0 and v in queue:
                    if dist[u] + graph[u][v][1] < dist[v]:
                        dist[v] = dist[u] + graph[u][v][1]
                        parent[v] = u

        return dist, parent

    def getPath(self, parent_dict, node_id, path):
        if parent_dict[node_id] == -1:
            path.insert(0, node_id)
        else:
            path.insert(0, node_id)
            self.getPath(parent_dict, parent_dict[node_id], path)
        return path
