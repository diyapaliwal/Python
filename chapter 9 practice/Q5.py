# Repeat program 4 for a list of such words to be censored.
words = ["donkey","bad", "ganda", "stupid","idiot"]
with open("Q4_file.txt") as f:
    content = f.read()
for word in words:
    content = content.replace(word, "#" * len(word))
with open("Q4_file.txt","w") as f:
    f.write(content)