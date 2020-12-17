from solutions.disjoint_set import DisjointSet

# make groups of connected nodes
# result is the no of groups
def dfs(i, group, adjacency_map, groups):
    if i in groups:
        return
    if i in adjacency_map:
        groups[i] = group
        dfs(adjacency_map[i], group, adjacency_map, groups)


def tree(n, adjacency_list):
    table = {}
    d = DisjointSet()
    for i in range(1, n+1):
        d.add(i)
    
    for x, y in adjacency_list:
        d.union(x, y)

    components = {}
    for i in range(1, n+1):
        parent = d.find(i)
        if not parent in components:
            components[parent] = True
        
    return len(components) - 1

def main():
    with open('rosalind_tree.txt') as f:
        n = int(f.readline())
        lines = f.readlines()
        adjacency_list = [map(int, line.split(' ')) for line in lines]

        print tree(n, adjacency_list)

main()
