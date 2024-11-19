sample = [] #All words being used (could be supe duper massive)
analyze = [] #Insertion.txt words to be analyzed

#Word stuff --------
conjunctions = []
nouns = []
verbs = []
adjectives = []
adverbs = []

def loadText(ty): #reads files and converts to lists
    x = []
    with open(ty,"r") as file:
        content = file.read()
        words = content.split(",")
        
        for i in words:
            x.append(i)
            sample.append(i)
            print(i)

    return x

def merge(txt, arr): #updates files in WordStorage
    msg = ""
    for i in arr:
        msg = msg+i+"," #data is stored like this in WordStorage
    
    with open(txt,"w") as file:
        file.write(msg)

print("Loading conjunctions")
conjunctions = loadText(r'Brute-Gen-main\WordStorage\conjunctions.txt')
print("Loading nouns")
nouns = loadText(r'Brute-Gen-main\WordStorage\nouns.txt')
print("Loading verbs")
verbs = loadText(r'Brute-Gen-main\WordStorage\verbs.txt')
print("Loading adjectives")
adjectives = loadText(r'Brute-Gen-main\WordStorage\adjectives.txt')
print("Loading adverbs")
adverbs = loadText(r'Brute-Gen-main\WordStorage\adverbs.txt')

print("Loading insertion")
#Gathers all the data from Insertion.txt and puts it all into one list.
try:
    with open('Brute-Gen-main\Insertion.txt','r') as file:
        content = file.read()
        
        content = content.replace("\n"," ")
        content = content.replace(".","")
        content = content.replace(",","")
        content = content.replace(":","")
        content = content.replace(";","")
        content = content.replace("#","")
        content = content.replace("$","")
        
        words = content.split(" ")
        
    for i in words:
        chk = False
        for x in analyze:
            if x == i:
                chk = True
        
        if chk == False:
            analyze.append(i)
except:
    print("Issue with reading insertion.txt")

print("Putting it all together")
trash = []
for i in analyze: #gets rid of words that are already stored
    chk = False
    for x in sample:
        if i == x:
            chk = True
    if chk == True:
        trash.append(i)
        
for i in trash:
    for x in analyze:
        if i == x:
            analyze.remove(x)

print("-----------------------")

for i in analyze: #Sorting data
    print("Is \""+ i+"\" a conjucate, noun, verb, adjective, or adverb?")
    print("c/n/v/ad/av")
    ans = input()
    
    if ans == "c":
        conjunctions.append(i)
    elif ans == "n":
        nouns.append(i)
    elif ans == "v":
        verbs.append(i)
    elif ans == "ad":
        adjectives.append(i)
    elif ans == "av":
        adverbs.append(i)

print("All data succesfully saved.")

print("Storing changes")
merge(r'Brute-Gen-main\WordStorage\conjunctions.txt',conjunctions)
merge(r'Brute-Gen-main\WordStorage\nouns.txt',nouns)
merge(r'Brute-Gen-main\WordStorage\verbs.txt',verbs)
merge(r'Brute-Gen-main\WordStorage\adjectives.txt',adjectives)
merge(r'Brute-Gen-main\WordStorage\adverbs.txt',adverbs)
