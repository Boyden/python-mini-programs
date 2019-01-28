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


def get_Node(model):
    node = set({})
    for x in model:
        node.add(x)
        for y in model[x]:
            node.add(y)

    return node

def get_Graph(model, node):
    G = {}
    for x in node:
        G[x] = {}

    for x in model:
        for y in model[x]:
            G[x][y] = model[x][y][0]
            if y not in model.keys() or model[y].get(x) == None:
                G[y][x] = inf

    return G

def get_Path(path_dict, node):
    path = [node]
    while path_dict[node] != None:
        path.append(path_dict[node])
        node = path_dict[node]

    return path[::-1]

def get_Delta(model, path):
    min_delta = inf
    for index in range(len(path)-1):
        cur_node = path[index]
        next_node = path[index+1]

        info = model[cur_node].get(next_node)
        if info != None:
            if min_delta > info[2] - info[1]:
                min_delta = info[2] - info[1]
        else:
            info = model[next_node][cur_node]
            if min_delta > info[1]:
                min_delta = info[1]

    return min_delta

def update_Model(model, path, delta):
    for index in range(len(path)-1):
        cur_node = path[index]
        next_node = path[index+1]
        info = model[cur_node].get(next_node)
        if info != None:
            model[cur_node][next_node][1] += delta
        else:
            model[next_node][cur_node][1] -= delta

    return model

def update_Graph(model, graph):
    for x in model:
        for y in model[x]:
            info = model[x][y]
            if info[1] == info[2]:
                graph[x][y] = inf
                graph[y][x] = -info[0]
    
    return graph

model = {
            's':{'1':[2, 0, 5], '2':[1, 0, 4]},
            '1':{'2':[3, 0, 1], '3':[3, 0, 4]},
            '2':{'3':[3, 0, 2], '4':[1, 0, 4]},
            '3':{'t':[1, 0, 5]},
            '4':{'3':[1, 0, 1], 't':[3, 0, 4]}
        }
node = get_Node(model)
G = get_Graph(model, node)


while True:
    try:
        result = bellman_ford(G, 's')
    except:
        break
    path = get_Path(result[1], 't')
    print(path)
    delta = get_Delta(model, path)
    print(delta)
    model = update_Model(model, path, delta)
    G = update_Graph(model, G)
    
    s_len = len(model['s'])
    count = 0 
    for elem in model['s']:
        if model['s'][elem][1] == model['s'][elem][2]:
            count += 1

    if count == s_len:
        break

print(model)


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
