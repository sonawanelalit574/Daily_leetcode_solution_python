
class Solution:
    def palindromePath(self, n: int, edges: list[list[int]], s: str, queries: list[str]) -> list[bool]:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        LOG = n.bit_length()
        parent = [[0] * n for _ in range(LOG)]
        depth = [0] * n
        tin = [0] * n
        tout = [0] * n
        timer = 0

        # Iterative DFS: Euler entry/exit times and parents
        stack = [(0, -1, 0)]
        while stack:
            u, p, state = stack.pop()

            if state == 0:
                parent[0][u] = u if p == -1 else p
                tin[u] = timer
                timer += 1

                stack.append((u, p, 1))
                for v in reversed(adj[u]):
                    if v != p:
                        depth[v] = depth[u] + 1
                        stack.append((v, u, 0))
            else:
                tout[u] = timer

        # Binary lifting for LCA
        for k in range(1, LOG):
            prev = parent[k - 1]
            curr = parent[k]
            for u in range(n):
                curr[u] = prev[prev[u]]

        def lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u

            diff = depth[u] - depth[v]
            while diff:
                k = diff.bit_length() - 1
                u = parent[k][u]
                diff -= 1 << k

            if u == v:
                return u

            for k in range(LOG - 1, -1, -1):
                if parent[k][u] != parent[k][v]:
                    u = parent[k][u]
                    v = parent[k][v]

            return parent[0][u]

        chars = [1 << (ord(c) - 97) for c in s]

        # Root-to-node XOR masks, maintained using subtree range updates.
        # Euler positions are 0-indexed; Fenwick positions are 1-indexed.
        bit = [0] * (n + 2)

        def add(i, delta):
            i += 1
            while i <= n + 1:
                bit[i] ^= delta
                i += i & -i

        def point_query(i):
            i += 1
            result = 0
            while i:
                result ^= bit[i]
                i -= i & -i
            return result

        # Initialize root-to-node prefix XOR using DFS order.
        prefix_mask = [0] * n
        order = [0] * n
        order[tin[0]] = 0

        for u in range(n):
            if u == 0:
                prefix_mask[u] = chars[u]
            else:
                prefix_mask[u] = prefix_mask[parent[0][u]] ^ chars[u]
            order[tin[u]] = u

        # Difference Fenwick: each node's initial prefix mask is
        # stored at its Euler position.
        for u in range(n):
            add(tin[u], prefix_mask[u])
            add(tin[u] + 1, prefix_mask[u])

        answer = []

        for q in queries:
            parts = q.split()

            if parts[0] == "update":
                u = int(parts[1])
                new_mask = 1 << (ord(parts[2]) - 97)
                delta = chars[u] ^ new_mask

                if delta:
                    chars[u] = new_mask

                    # All root paths through u change by delta.
                    add(tin[u], delta)
                    add(tout[u], delta)

            else:
                u, v = int(parts[1]), int(parts[2])
                w = lca(u, v)

                # Prefix masks are queried in O(log n).
                pu = point_query(tin[u])
                pv = point_query(tin[v])

                # Path XOR = prefix(u) XOR prefix(v) XOR char(LCA)
                mask = pu ^ pv ^ chars[w]
                answer.append((mask & (mask - 1)) == 0)

        return answer
