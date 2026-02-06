class Solution:
    def findDuplicate(self, paths):
        content_map = defaultdict(list)

        for path in paths:
            parts = path.split()
            root = parts[0]
            for file_info in parts[1:]:
                name, _, content = file_info.partition("(")
                content = content[:-1]  # remove trailing ')'
                content_map[content].append(f"{root}/{name}")

        return [group for group in content_map.values() if len(group) > 1]