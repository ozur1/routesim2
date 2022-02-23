class Graph:
    """
    node_ids = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
    g.graph = {'a': {'a': ('seq_aa', 0), 'b': ('seq_ab', 2), 'c': ('seq_ab', 6), 'd': ('seq_ad', 0), 'e': ('seq_ae', 0),
                 'f': ('seq_af', 0), 'g': ('seq_ag', 0), 'h': ('seq_ah', 0), 'i': ('seq_ai', 0)},
                'b': {'a': ('seq_ba', 2), 'b': ('seq_bb', 0), 'c': ('seq_bc', 0), 'd': ('seq_bd', 5), 'e': ('seq_be', 0),
                 'f': ('seq_bf', 0), 'g': ('seq_bg', 0), 'h': ('seq_bh', 0), 'i': ('seq_bi', 0)},
                'c': {'a': ('seq_ca', 6), 'b': ('seq_cb', 0), 'c': ('seq_cc', 0), 'd': ('seq_cd', 8), 'e': ('seq_ce', 0),
                 'f': ('seq_cf', 0), 'g': ('seq_cg', 0), 'h': ('seq_ch', 0), 'i': ('seq_ci', 0)},
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

    let source node be 'a'
    """

    def __init__(self):
        self.node_ids = []
        self.graph = {}

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

        # for id in self.node_ids:
        #     self.printPath(parent, id)
        #     print('\n')

        return dist, parent

    def getPath(self, parent_dict, node_id, path):
        if parent_dict[node_id] == -1:
            path.insert(0, node_id)
        else:
            path.insert(0, node_id)
            self.getPath(parent_dict, parent_dict[node_id], path)
        return path


g = Graph()
g.node_ids = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
g.graph = {'a': {'a': ('seq_aa', 0), 'b': ('seq_ab', 2), 'c': ('seq_ab', 6), 'd': ('seq_ad', 0), 'e': ('seq_ae', 0),
                 'f': ('seq_af', 0), 'g': ('seq_ag', 0), 'h': ('seq_ah', 0), 'i': ('seq_ai', 0)},

           'b': {'a': ('seq_ba', 2), 'b': ('seq_bb', 0), 'c': ('seq_bc', 0), 'd': ('seq_bd', 5), 'e': ('seq_be', 0),
                 'f': ('seq_bf', 0), 'g': ('seq_bg', 0), 'h': ('seq_bh', 0), 'i': ('seq_bi', 0)},

           'c': {'a': ('seq_ca', 6), 'b': ('seq_cb', 0), 'c': ('seq_cc', 0), 'd': ('seq_cd', 8), 'e': ('seq_ce', 0),
                 'f': ('seq_cf', 0), 'g': ('seq_cg', 0), 'h': ('seq_ch', 0), 'i': ('seq_ci', 0)},

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

dist, parent = g.dijkstra(g.graph, 'a')
print(dist)
print(parent)

path = g.getPath(parent, 'g', [])
print(path)
if len(path) < 2:
    print("no next hop")
else:
    print("next_hop:", path[1])
