
results = []
with open('greeting57.txt') as inputfile:
    for line in inputfile:
        results.append(line.strip().split(' '))

results_int = []
for element in range(len(results)):
    #print ("On %d line of the text file" %element)
    new = []
    for i in range(len(results[element])):
        #print ("On %d value of the row %d of the file" %(i, element))
        dummy = results[element][i]
        if dummy != "":
            new.append(int(dummy))
        else:
            new.append("")
    if new[0] == "":
        continue
    results_int.append(new)

print results_int