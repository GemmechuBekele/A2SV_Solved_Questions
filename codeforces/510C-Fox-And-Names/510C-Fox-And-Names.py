import sys
from collections import deque

def solve():
    # Read n
    line = sys.stdin.readline()
    if not line:
        return
    n = int(line.strip())
    
    names = [sys.stdin.readline().strip() for _ in range(n)]
    
    # Initialize graph for 26 letters
    adj = [[] for _ in range(26)]
    in_degree = [0] * 26
    
    # Build edges based on adjacent pairs
    for i in range(n - 1):
        s1 = names[i]
        s2 = names[i+1]
        
        length = min(len(s1), len(s2))
        found_mismatch = False
        
        for j in range(length):
            if s1[j] != s2[j]:
                u = ord(s1[j]) - ord('a')
                v = ord(s2[j]) - ord('a')
                adj[u].append(v)
                in_degree[v] += 1
                found_mismatch = True
                break
        
        # Prefix check: if s2 is a prefix of s1 and they are different, it's impossible
        if not found_mismatch and len(s1) > len(s2):
            print("Impossible")
            return

    # Kahn's algorithm for Topological Sort
    queue = deque([i for i in range(26) if in_degree[i] == 0])
    result = []
    
    while queue:
        u = queue.popleft()
        result.append(chr(u + ord('a')))
        
        for v in adj[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)
                
    # If result doesn't contain all 26 letters, there was a cycle
    if len(result) < 26:
        print("Impossible")
    else:
        print("".join(result))

if __name__ == "__main__":
    solve()