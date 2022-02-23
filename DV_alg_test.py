class Node:
    def __init__(self):
        self.id = 'c'
        self.neighbor_costs = {}
        self.distance_vector = [{}, 0]
        self.neighbor_distance_vectors = {}

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


node1 = Node()
print(node1.distance_vector)
node1.neighbor_costs = {'a': 5, 'b': 3, 'd': 4}
new_dv, need_to_change = node1.Bellman_Ford()
print(new_dv, need_to_change)
if need_to_change:
    node1.distance_vector = new_dv

node1.neighbor_distance_vectors['a'] = [{'b': (1, ['b']), 'c': (5, ['c'])}, 20]
new_dv, need_to_change = node1.Bellman_Ford()
print(new_dv, need_to_change)
if need_to_change:
    node1.distance_vector = new_dv

node1.neighbor_distance_vectors['b'] = [{'a': (1, ['a']),
                                         'c': (3, ['c']),
                                         'e': (9, ['e'])},
                                        4]
new_dv, need_to_change = node1.Bellman_Ford()
print(new_dv, need_to_change)
if need_to_change:
    node1.distance_vector = new_dv

node1.neighbor_distance_vectors['d'] = [{'c': (4, ['c']),
                                         'e': (2, ['e'])},
                                        10]
new_dv, need_to_change = node1.Bellman_Ford()
print(new_dv, need_to_change)
if need_to_change:
    node1.distance_vector = new_dv
print("next_hop_e:", node1.distance_vector[0]['e'][1][0])
