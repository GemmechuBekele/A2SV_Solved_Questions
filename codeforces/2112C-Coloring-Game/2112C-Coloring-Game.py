import sys

def solve() -> None:
    it = iter(sys.stdin.read().strip().split())
    t = int(next(it))
    out_lines = []
    for _ in range(t):
        n = int(next(it))
        a = [int(next(it)) for _ in range(n)]
        total = 0
        a_n = a[-1] 
        for k in range(2, n):
            ak = a[k]
            b = max(ak, a_n - ak)  
            j = k - 1
            cnt = 0

            for i in range(k - 1):
                while j > i and a[i] + a[j] > b:
                    j -= 1
                cnt += (k - 1) - max(i, j)
            total += cnt
        out_lines.append(str(total))
    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    solve()