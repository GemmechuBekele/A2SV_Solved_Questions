s = input()
def countVowels(s):
    if s == "":
        return 0

    if s[0].lower() in "aeiou":
        return 1+countVowels(s[1:])
    else:
        return countVowels(s[1:])

print(countVowels(s))