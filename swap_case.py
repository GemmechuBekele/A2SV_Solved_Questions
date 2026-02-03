def swap_case(s):
    swap_str = ""
    for sub_str in s:
        if sub_str.isupper():
            swap_str += sub_str.lower()
        else:
            swap_str += sub_str.upper()
        
    return swap_str