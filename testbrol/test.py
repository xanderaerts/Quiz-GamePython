f = open("../EindProjectPython2021/questions.txt")

for i,line in enumerate(f):
    if i == 0:
        lijn2 = line
    elif i == 3:
        lijn3 = line


print(f"lijn2 = {lijn2} en lijn3 = {lijn3}")

f.close()