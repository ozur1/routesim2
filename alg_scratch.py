# Distance Vector Example
seq_num = 0  # arbitrary
# Graph
nodes = ['a', 'b', 'c', 'd', 'e']
edged = [('a', 'b', 1), ('a', 'c', 5), ('b', 'c', 3), ('c', 'd', 4), ('d', 'e', 2), ('b', 'e', 9)]

# Local node
reference_node = 'c'
neighbor_costs = {'a': 5, 'b': 3, 'd': 4}

distance_vector_c = ({'a': (5, ['a']),
                      'b': (3, ['b']),
                      'd': (4, ['d'])},
                     seq_num)

neighbor_distance_vector_c = {}

# incoming message from node b
distance_vector_b = ({'a': (1, ['a']),
                      'c': (3, ['c']),
                      'e': (9, ['e'])},
                     seq_num)

# if distance_vector_b not in neighbor_distance_vector_c or
# seq_num in distance_vector_b > the seq number for 'b' in neighbor_distance_vector_c, good to go

# add to my neighbors' distance vectors dict
neighbor_distance_vector_c['b'] = distance_vector_b

"""
cost_bc = neighbor_costs['b'] = 3
for key_value pair in distance_vector_b:
    node 'a': 
    min(distance_vector_c['a'][0], distance_vector_b['a'][0] + cost_bc) = min(5, 4) = 4
    update distance_vector_c['a'][0] = 4, insert 'b' into path -> distance_vector_c['a'][1] = ['b', 'a']
    
    node 'c': id matched my reference id, disregard
    
    node 'e': no match in my distance vector, add it
    distance_vector_c['e'] = (distance_vector_b['e']+cost_bc=9+3=12, ['b', 'e'])
"""

distance_vector_c = ({'a': (4, ['b', 'a']),
                      'b': (3, ['b']),
                      'd': (4, ['d']),
                      'e': (12, ['b', 'e'])},
                     seq_num)

neighbor_distance_vector_c = {'b': ({'a': (1, ['a']),
                                     'c': (3, ['c']),
                                     'e': (9, ['e'])},
                                    seq_num)}

# incoming message from node d
distance_vector_d = ({'c': (4, ['c']),
                      'e': (2, ['e'])},
                     seq_num)

neighbor_distance_vector_c = {'b': ({'a': (1, ['a']),
                                     'c': (3, ['c']),
                                     'e': (9, ['e'])},
                                    seq_num),
                              'd': ({'c': (4, ['c']),
                                     'e': (2, ['e'])},
                                    seq_num)}

"""
cost_cd = 4
for key_value pair in distance_vector_d:
    node 'c': id matched my reference id, disregard
    
    node 'e'
    min(distance_vector_c['e'][0], distance_vector_d['e'][0]+cost_cd) = min(12, 2+4) = 6
    update distance_vector_c['e'][0] = 6, distance_vector_c['e'][1] = ['d', distance_vector_d['e'][1]] = ['d', 'e']
"""

distance_vector_c = ({'a': (4, ['b', 'a']),
                      'b': (3, ['b']),
                      'd': (4, ['d']),
                      'e': (6, ['d', 'e'])},
                     seq_num)







graph = {'a': {'a': ('0', 0), 'b': ('1', 5), 'c': ('0', 6), 'd': ('0', 0), 'e': ('0', 0),
               'f': ('0', 0), 'g': ('0', 0), 'h': ('0', 0), 'i': ('0', 0)},
         'b': {'a': ('1', 5), 'b': ('0', 0), 'c': ('0', 0), 'd': ('0', 5), 'e': ('0', 0),
               'f': ('0', 0), 'g': ('0', 0), 'h': ('0', 0), 'i': ('0', 0)},
         'c': {'a': ('0', 6), 'b': ('0', 0), 'c': ('0', 0), 'd': ('0', 8), 'e': ('0', 0),
               'f': ('0', 0), 'g': ('0', 0), 'h': ('0', 0), 'i': ('0', 0)},
         'd': {'a': ('seq_da', 0), 'b': ('seq_db', 0), 'c': ('seq_dc', 8), 'd': ('seq_dd', 0), 'e': ('seq_de', 10),
               'f': ('seq_df', 15), 'g': ('seq_dg', 0), 'h': ('seq_dh', 0), 'i': ('seq_di', 0)},
         'e': {'a': ('seq_ea', 0), 'b': ('seq_eb', 0), 'c': ('seq_dc', 0), 'd': ('seq_ed', 10), 'e': ('seq_ee', 0),
               'f': ('seq_ef', 6), 'g': ('seq_eg', 2), 'h': ('seq_eh', 0), 'i': ('seq_ei', 0)},
         'f': {'a': ('seq_fa', 0), 'b': ('seq_fb', 0), 'c': ('seq_fc', 0), 'd': ('seq_fd', 15), 'e': ('seq_fe', 6),
               'f': ('seq_ff', 0), 'g': ('seq_fg', 6), 'h': ('seq_fh', 0), 'i': ('seq_fi', 0)},
         'g': {'a': ('seq_ga', 0), 'b': ('seq_gb', 0), 'c': ('seq_gc', 0), 'd': ('seq_gd', 0), 'e': ('seq_ge', 2),
               'f': ('seq_gf', 6), 'g': ('seq_gg', 0), 'h': ('seq_gh', 0), 'i': ('seq_gi', 0)},
         'h': {'a': ('seq_ha', 0), 'b': ('seq_hb', 0), 'c': ('seq_hc', 0), 'd': ('seq_hd', 0), 'e': ('seq_he', 0),
               'f': ('seq_hf', 0), 'g': ('seq_hg', 0), 'h': ('seq_hh', 0), 'i': ('seq_hi', 10)},
         'i': {'a': ('seq_ia', 0), 'b': ('seq_ib', 0), 'c': ('seq_ic', 0), 'd': ('seq_id', 0), 'e': ('seq_ie', 0),
               'f': ('seq_if', 0), 'g': ('seq_ig', 0), 'h': ('seq_ih', 10), 'i': ('seq_ii', 0)}
         }

# update cost between a and b from 2 to 5
# access seq_ab (0), and ++ that in message
# send message:
"""
{
source: 'a'
destination: 'b'
cost: 5
seq_num: 1
};

{
source: 'b'
destination: 'a'
cost: 5
seq_num: 1
};
"""
