import re

text = "The quick brown fox"
pattern = "quick"

# match = re.match(pattern, text)
match = re.search(pattern, text)
if match:
    print("Match found : : : : : ", match.group())
else:
    print("No match", match)

print(re.findall(pattern, text))

matches = re.finditer(pattern, text)
for match in matches:
    print(match.group(), match.start(), match.end())
