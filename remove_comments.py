class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        result = []          # final answer lines
        in_block = False     # are we inside /* ... */ ?
        buffer = ""          # current line being built

        for line in source:
            i = 0
            while i < len(line):
                # If we are inside a block comment
                if in_block:
                    # Check if block comment ends
                    if i + 1 < len(line) and line[i] == '*' and line[i+1] == '/':
                        in_block = False
                        i += 2
                    else:
                        i += 1

                # If we are NOT inside a block comment
                else:
                    # Line comment starts
                    if i + 1 < len(line) and line[i] == '/' and line[i+1] == '/':
                        break

                    # Block comment starts
                    elif i + 1 < len(line) and line[i] == '/' and line[i+1] == '*':
                        in_block = True
                        i += 2

                    # Normal character
                    else:
                        buffer += line[i]
                        i += 1

            # If line ended and we are NOT inside a block comment
            if not in_block and buffer:
                result.append(buffer)
                buffer = ""

        return result