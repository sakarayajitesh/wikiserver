import wikipedia

result = wikipedia.search("sunfeast")
print(str(result))
print(wikipedia.summary(result[0]))
