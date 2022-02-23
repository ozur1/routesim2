from simulator.node import Node
import json


class Distance_Vector_Node(Node):
    def __init__(self, id):
        super().__init__(id)
        self.neighbor_costs = {}
        self.distance_vector = [{}, 0]
        self.neighbor_distance_vectors = {}

        """
        neighbor_costs = dict, key = node id, value = int cost of link
        distance_vector =  tuple, [0] = dict, key = node id, value = (cost, path list of node ids), [1] = seq number
        neighbor_distance_vectors = dict, key = neighbor node id, value = that neighbor's distance vector
        """

        # we have this node's id and a list of its neighbors
        # additional info needed:
        # 1. cost of link to each directly attached neighbor
        # 2. this node's distance vector: estimated cost of least-cost path from this node to every other node
        # 3. the distance vector of each of this node's directly attached neighbors

        # Your distance vectors should include the full routing path for each destination (similar to the AS_PATH in
        # BGP). In other words, each entry in the DV should also include a list (or set) of nodes that are involved
        # in the path. This will allow nodes to avoid choosing routes that would form loops and this will prevent
        # count to infinity.

        # you should add a sequence number (or just a timestamp) to DVs,
        # so that you always keep the one that was sent latest, not necessarily received latest.

    # Return a string
    def __str__(self):
        return "Rewrite this function to define your node dump printout"

    # Fill in this function
    def link_has_been_updated(self, neighbor, latency):
        # latency = -1 if delete a link
        if latency == -1:
            del self.neighbor_costs[neighbor]
        else:
            self.neighbor_costs[neighbor] = latency

        new_dv, need_to_send = self.Bellman_Ford()

        if need_to_send:
            self.distance_vector = new_dv
            self.send_to_neighbors(json.dumps((self.id, new_dv)))
        return

    # Fill in this function
    def process_incoming_routing_message(self, m):
        """
        step 1: parse message
        message will contain node ID of sender, and that node's distance vector
        step 2: check if sender is in self.neighbor_distance_vectors
        if it is: check seq number
        if message dv seq number <= self.neighbor_distance_vectors[sender] seq num, ignore
        else: update seq number, call Bellman Ford, send out table if self.distance_vector changed
        if sender is not in self.neighbor_distance_vectors, add it it,
            call Bellman Ford, send out table if self.distance_vector changed
        """
        id, vector = json.loads(m)
        if id not in self.neighbor_distance_vectors:
            return
        elif vector[1] >= self.neighbor_distance_vectors[id][1]:
            self.neighbor_distance_vectors[id] = vector
            new_dv, need_to_send = self.Bellman_Ford()

            if need_to_send:
                self.distance_vector = new_dv
                self.send_to_neighbors(json.dumps(self.id, new_dv))
        return


    # Return a neighbor, -1 if no path to destination
    def get_next_hop(self, destination):
        dv = self.distance_vector[0]
        if destination in dv:
            return dv[destination][1][0]
        else:
            return -1

    def Bellman_Ford(self):
        # initialize new distance vector with incremented sequence number
        new_distance_vector = {}
        new_seq_num = self.distance_vector[1]
        new_seq_num += 1

        # place all immediate neighbors and respective costs into new distance vector
        for n in self.neighbor_costs:
            new_distance_vector[n] = (self.neighbor_costs[n], [n])

        # iterate through neighbor distance vectors
        for key in self.neighbor_distance_vectors:
            neighbor_dv = self.neighbor_distance_vectors[key]
            cost_to_neighbor = self.neighbor_costs[key]
            # for each key (node) in neighbor distance vector
            for node in neighbor_dv[0]:
                # if node is me, ignore
                if node == self.id:
                    continue
                # if node already in my distance vector, check if need to update cost / path
                if node in new_distance_vector:
                    if neighbor_dv[0][node][0] + cost_to_neighbor < new_distance_vector[node][0]:
                        new_cost = neighbor_dv[0][node][0] + cost_to_neighbor
                        new_path = [key] + neighbor_dv[0][node][1]
                        new_distance_vector[node] = (new_cost, new_path)
                    else:
                        new_cost = new_distance_vector[node][0]
                        new_path = new_distance_vector[node][1]
                        new_distance_vector[node] = (new_cost, new_path)
                # if new node, add it to distance vector with new cost and path
                else:
                    new_cost = cost_to_neighbor + neighbor_dv[0][node][0]
                    new_path = [key] + neighbor_dv[0][node][1]
                    new_distance_vector[node] = (new_cost, new_path)

        # if the new distance vector is different than original, than a change has been made and need to send new table
        # to neighbors, so True is returned alongside new distance vector
        if new_distance_vector == self.distance_vector[0]:
            return [new_distance_vector, new_seq_num], False
        else:
            return [new_distance_vector, new_seq_num], True
