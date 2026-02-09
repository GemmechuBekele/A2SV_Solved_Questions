from collections import defaultdict
def groupAnagrams(strs):
        collect = defaultdict(list)

        for s in strs:
            key = ''.join(sorted(s))
            collect[key].append(s)
        return list(collect.values())
a= groupAnagrams(['a'])
print(a)