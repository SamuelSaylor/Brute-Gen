txt = ""

conjunctions = []
nouns = []
verbs = []
adjectives = []
adverbs = []

def loadText(ty):
    x = []
    with open(ty,"r") as file:
        content = file.read()
        words = content.split(",")
        
        for i in words:
            x.append(i)

    return x

print("Loading conjunctions")
conjunctions = loadText(r'WordStorage\conjunctions.txt')
print("Loading nouns")
nouns = loadText(r'WordStorage\nouns.txt')
print("Loading verbs")
verbs = loadText(r'WordStorage\verbs.txt')
print("Loading adjectives")
adjectives = loadText(r'WordStorage\adjectives.txt')
print("Loading adverbs")
adverbs = loadText(r'WordStorage\adverbs.txt')

print("Reading insertion")
#Reading new File
try:
    with open('Insertion.txt','r') as file:
        content = file.read()
        lines = content.split("\n")
        
    for line in lines:
        txt = txt+" "+line
except:
    print("Issue with reading insertion.txt")