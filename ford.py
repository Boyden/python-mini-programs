inf = float('inf')

# G = {
#         's': {'t': 6, 'y': 7},
#         't': {'x': 5, 'y': 8, 'z': -4},
#         'x': {'t': -2},
#         'y': {'x': -3, 'z': 9},
#         'z': {'x': 7, 's': 2}
#     }

def relax(G, u, v, D, P):
    old = D.get(v, inf) # 若D[v]不存在则返回inf
    new = D.get(u, inf) + G[u][v]
    if new < old:
        D[v], P[v] = new, u
        return True # 若有改进，则返回True

def bellman_ford(G, s):
    D, P = {s: 0}, {s: None}
    for _ in G: # 轮数等于节点数
        improved = False
        for u in G:
            for v in G[u]:
                if relax(G, u, v, D, P):
                    improved = True
        if not improved: # 如果某轮没有任何改进
            break        # 说明问题已经解决，退出循环
    else:                # 否则，说明第n轮也有改进，存在负权环
        raise ValueError('negative cycle')
    return D, P





# G = {
#             's':{'1':2, '2':1},
#             '1':{'2':3, '3':3},
#             '2':{'3':3, '4':1},
#             '3':{'t':1},
#             '4':{'3':1, 't':3}
#         }


# G = {
#             's':{'1':2, '2':1},
#             '1':{'2':3, '3':3, 's':-2},
#             '2':{'3':3, '4':1, 's':-1, '1':-3},
#             '3':{'t':1, '1':-3, '2':-3, '4':-1},
#             '4':{'3':1, 't':3, '2':-1},
#             't':{'3':-1, '4':-3}
#         }

# G = {
#             's':{'1':2, '2':1},
#             '1':{'2':3, '3':3, 's':inf},
#             '2':{'3':3, '4':1, 's':inf, '1':inf},
#             '3':{'t':1, '1':inf, '2':inf, '4':inf},
#             '4':{'3':1, 't':3, '2':inf},
#             't':{'3':inf, '4':inf}
#         }
