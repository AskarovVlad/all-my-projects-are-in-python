joke_message = "%s приспособление для поиска стульев, но %s лучше с этим справляется, хотя %s всё же король"
print(joke_message.find("%"))
print(joke_message.rfind("ь"))
bodypart: str = 'коленко:'
bodypart1 = "лодыжка:"
bodypart2 = "мизинчик"
print(joke_message % (bodypart, bodypart1, bodypart2))
print(10 * bodypart2)
print('%s приспособление для поиска стульев, но %s лучше с этим справляется, хотя %s всё же король' % (bodypart, bodypart1, bodypart2))

print(bodypart.rfind("о"))
print(bodypart1.replace("лодыжка", "нога"))
bodypart1 = bodypart1.replace("лодыжка", "нога")
print('%s приспособление для поиска стульев, но %s лучше с этим справляется, хотя %s всё же король' % (bodypart, bodypart1, bodypart2))
x = joke_message.split(" ")
print(x)
y = " ".join(x)
print(y)
print(bodypart.count("о"))
