import sys

CHARS = [chr(ord('a') + i) for i in range(26)]

def solve():

    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    it = iter(input_data)
    try:
        T_cases_str = next(it)
        T_cases = int(T_cases_str)
    except (StopIteration, ValueError):
        return
    
    output = []
    base_ord = ord('a')
    local_chars = CHARS
    
    for _ in range(T_cases):
        try:
            s = next(it)
            t = next(it)
        except StopIteration:
            break
        

        t_counts = [0] * 26
        for char in t:
            t_counts[ord(char) - base_ord] += 1
        

        s_counts = [0] * 26
        for char in s:
            s_counts[ord(char) - base_ord] += 1
            

        possible = True
        for i in range(26):
            if t_counts[i] < s_counts[i]:
                possible = False
                break
        if not possible:
            output.append("Impossible")
            continue
            

        n_s = len(s)
        n_t = len(t)
        s_codes = [ord(c) - base_ord for c in s]
        
        res = []
        p = 0
        needed = s_counts[:] 
        curr_inv = t_counts[:] 
        
        local_res_append = res.append
        local_s_codes = s_codes
        
        for _ in range(n_t):
            for char_code in range(26):
                if curr_inv[char_code] > 0:

                    if p < n_s and char_code == local_s_codes[p]:
                        local_res_append(local_chars[char_code])
                        curr_inv[char_code] -= 1
                        needed[char_code] -= 1
                        p += 1
                        break

                    elif curr_inv[char_code] > needed[char_code]:
                        local_res_append(local_chars[char_code])
                        curr_inv[char_code] -= 1
                        break
                        
        output.append("".join(res))

    if output:
        sys.stdout.write("\n".join(output) + "\n")

if __name__ == "__main__":
    solve()