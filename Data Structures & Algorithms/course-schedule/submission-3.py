class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites: return True

        adj = defaultdict(list)

        for c, pre in prerequisites:
            adj[c].append(pre)

        stack = []
        VISITED, VISITING  = 1, 2
        state = [0] * numCourses
        for c in range(numCourses):
            if state[c] == VISITED: continue

            stack = [(c, True)]
            
            while stack:
                node, entering = stack.pop()
                
                
                if entering:
                    if state[node] == VISITING: return False
                    if state[node] == VISITED: continue

                    state[node] = VISITING
                    stack.append((node, False))
                    for n in adj[node]:
                        if state[n] == VISITING: return False
                        if state[n] == VISITED: continue

                        stack.append((n, True))
                else:
                    state[node] = VISITED
                
        return True


