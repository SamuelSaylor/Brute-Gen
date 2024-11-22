import coreFunctions
verbs = coreFunctions.loadText(r'Brute-Gen-main\WordStorage\verbs.txt')
txt = (r'Brute-Gen-main\PreciseTraining\PreciseStorage\PreciseVerb.txt')

preciseVerbs = []

precThrowaway = []
with open(txt,"r") as file: #Removes the $ designations
    fart = file.read()
    
    fart = fart.replace("$past","")
    fart = fart.replace("$present","")
    fart = fart.replace("$future","")
    
    fart = fart.split(",")

    for i in fart:
        for x in verbs:
            if x == i:
                precThrowaway.append(i)
    
    for i in precThrowaway:
        for x in verbs:
            if x == i:
                verbs.remove(x)

for i in verbs: # Questionaire
    print("Is \""+i+"\" past tense, present tense, or future tense?")
    print("pa/pr/f")
    ans = input()
    
    if i != "":
        if ans == "pa":
            preciseVerbs.append(i+"$past")
        elif ans == "pr":
            preciseVerbs.append(i+"$present")
        elif ans == "f":
            preciseVerbs.append(i+"$future")

coreFunctions.write(txt, preciseVerbs)
print("Save complete")