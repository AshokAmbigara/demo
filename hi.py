import re

s3 = "House number- 1105"
result = re.search(r"\d", s3)

if result:
    print("Digit found")
else:
    print("Digit not found.")

    #string
str1= "The quick brown fox jumps over the lazy dog."

# Write your code below and press Shift+Enter to execute
new_str1 = re.sub(r"fox", "bear", str1)

print(new_str1)

str2= "How much wood would a woodchuck chuck, if a woodchuck could chuck wood?"

matches = re.findall(r"woo", str2)

print(matches)