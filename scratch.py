graph = {'a': {'a': ('seq_aa', 0), 'b': ('seq_ab', 2), 'c': ('seq_ab', 6), 'd': ('seq_ad', 0), 'e': ('seq_ae', 0),
               'f': ('seq_af', 0), 'g': ('seq_ag', 0)},
         'b': {'a': ('seq_ba', 2), 'b': ('seq_bb', 0), 'c': ('seq_bc', 0), 'd': ('seq_bd', 5), 'e': ('seq_be', 0),
               'f': ('seq_bf', 0), 'g': ('seq_bg', 0)},
         'c': {'a': ('seq_ca', 6), 'b': ('seq_cb', 0), 'c': ('seq_cc', 0), 'd': ('seq_cd', 8), 'e': ('seq_ce', 0),
               'f': ('seq_cf', 0), 'g': ('seq_cg', 0)},
         'd': {'a': ('seq_da', 0), 'b': ('seq_db', 0), 'c': ('seq_dc', 8), 'd': ('seq_dd', 0), 'e': ('seq_de', 10),
               'f': ('seq_df', 15), 'g': ('seq_dg', 0)},
         'e': {'a': ('seq_ea', 0), 'b': ('seq_eb', 0), 'c': ('seq_dc', 0), 'd': ('seq_ed', 10), 'e': ('seq_ee', 0),
               'f': ('seq_ef', 6), 'g': ('seq_eg', 2)},
         'f': {'a': ('seq_fa', 0), 'b': ('seq_fb', 0), 'c': ('seq_fc', 0), 'd': ('seq_fd', 15), 'e': ('seq_fe', 6),
               'f': ('seq_ff', 0), 'g': ('seq_fg', 6)},
         'g': {'a': ('seq_ga', 0), 'b': ('seq_gb', 0), 'c': ('seq_gc', 0), 'd': ('seq_gd', 0), 'e': ('seq_ge', 2),
               'f': ('seq_gf', 6), 'g': ('seq_gg', 0)}}

print(graph['f']['a'][1])
