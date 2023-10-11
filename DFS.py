total_vertex = int(input("enter the number of vertices: "))
graph = {}
flag = True

for i in range(total_vertex):
    vertex = input("enter vertex value: ")
    graph[vertex] = [] 
    while flag:
        child = input(f'enter the child for {vertex} (or enter "-1" to stop): ')
        if child != '-1':
            graph[vertex].append(child)
        else:
            flag = False
    flag = True

print(graph)
