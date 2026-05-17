from collections import deque

arr = [4,2,3,0,3,1,2]
start_node = 5

visited = {start_node}
queue = deque([start_node])

while queue:
    current_node = queue.popleft()
    
    n1 = current_node + arr[current_node]
    n2 = current_node - arr[current_node]

    print(n1, n2, current_node)

    if n1 >= len(arr) or n1 < 0: print(False)
    else:
        if arr[n1] == 0: print(True)
        else:
            if n1 not in visited:
                visited.add(n1)
                queue.append(n1)
    if n2 >= len(arr) or n2 < 0: print(False)
    else:
        if arr[n2] == 0: print(True)
        else:
            if n2 not in visited:
                visited.add(n2)
                queue.append(n2)
