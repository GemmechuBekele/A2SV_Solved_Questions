import sys

def solve():
    # Use sys.stdin.read().split() to get all numbers at once - usually the fastest way in Python
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    
    # Base case for a single node
    if n == 1:
        sys.stdout.write("0\n")
        return
    
    # Build adjacency list
    adj = [[] for _ in range(n + 1)]
    it = iter(input_data[1:])
    for u_str in it:
        u = int(u_str)
        v = int(next(it))
        adj[u].append(v)
        adj[v].append(u)
        
    def get_farthest(start_node):
        """
        An optimized BFS that avoids popleft() and while loops.
        In Python, 'for u in queue' where we append to 'queue' inside 
        the loop is significantly faster.
        """
        dist = [-1] * (n + 1)
        dist[start_node] = 0
        queue = [start_node]
        
        for u in queue:
            d_next = dist[u] + 1
            for v in adj[u]:
                if dist[v] == -1:
                    dist[v] = d_next
                    queue.append(v)
        
        # The last node added to the queue is guaranteed to be one of the farthest
        farthest_node = queue[-1]
        return farthest_node, dist[farthest_node]

    # Step 1: Find one end of the diameter
    u, _ = get_farthest(1)
    
    # Step 2: Find the diameter length from node u
    _, diameter = get_farthest(u)
    
    # Circumference = 3 * Diameter (based on pi = 3)
    sys.stdout.write(str(diameter * 3) + "\n")

if __name__ == "__main__":
    solve()