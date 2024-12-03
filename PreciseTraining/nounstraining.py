import coreFunctions
nouns = coreFunctions.loadText(r'Brute-Gen-main\WordStorage\nouns.txt')
txt = (r'Brute-Gen-main\PreciseTraining\PreciseStorage\PreciseNoun.txt')

preciseNouns = []

precThrowaway = []
with open(txt,"r") as file: #Removes the $ designations
    fart = file.read()
    
    fart = fart.replace("$person","")
    fart = fart.replace("$job","")
    fart = fart.replace("$place","")
    fart = fart.replace("$obj","")
    fart = fart.replace("$activity","")
    
    fart = fart.split(",")

    for i in fart:
        for x in nouns:
            if x == i:
                precThrowaway.append(i)
    
    for i in precThrowaway:
        for x in nouns:
            if x == i:
                nouns.remove(x)

for i in nouns: # Questionaire
    print("Is \""+i+"\" a person, a job/title, a place, an object, or an activity?")
    print("pr/j/pl/o/a")
    ans = input()
    
    if i != "":
        if ans == "pr":
            preciseNouns.append(i+"$person")
        elif ans == "j":
            preciseNouns.append(i+"$job")
        elif ans == "pl":
            preciseNouns.append(i+"$place")
        elif ans == "o":
            preciseNouns.append(i+"$obj")
        elif ans == "a":
            preciseNouns.append(i+"$activity")

coreFunctions.updateTxt(txt, preciseNouns)
print("Save complete")
