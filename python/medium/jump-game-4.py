from collections import deque

class Solution:
    def minJumps(self, arr: List[int]) -> int:
        sv = {}
        counter = 0

        for i, num in enumerate(arr):
            if num not in sv:
                sv[num] = []
            sv[num].append(i)
        start_node = 0
        visited = {start_node}
        queue = deque([(start_node, 0)])

        if len(arr) == 1: return 0

        while queue:
            current_node, s = queue.popleft()
            n1 = current_node + 1
            n2 = current_node - 1

            if 0 <= n1 < len(arr):
                if n1 == len(arr) - 1: return s + 1
                else:
                    if n1 not in visited:
                        visited.add(n1)
                        queue.append((n1, s + 1))
            if 0 <= n2 < len(arr):
                if n2 == len(arr) - 1: return s + 1
                else:
                    if n2 not in visited:
                        visited.add(n2)
                        queue.append((n2, s + 1))

            if arr[current_node] in sv:
                n3 = sv[arr[current_node]]
                del sv[arr[current_node]]
                for idx in n3:
                    if 0 <= idx < len(arr):
                        if idx == len(arr) - 1: return s + 1
                        else:
                            if idx not in visited:
                                visited.add(idx)
                                queue.append((idx, s + 1))
            else: continue
