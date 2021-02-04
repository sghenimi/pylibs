import random as rand
anumber = rand.randint(0, 100)
print("Try to gess our random number [1, 100] in a maximum of 5 turns !")
history = []
for i in range(10):
    try:
        g = int(input())
        history.append(g)
        print(history)
        if g < anumber:
            print("too low")
        elif g > anumber:
            print("too high")
        else:
            print("Excelent!")
            break
    except:
        print("not an integer")
        history.append("NaN")
        print(history)
        continue
if (history[len(history)-1] != anumber):
    print("Game Over")
    print(f"the number was : {g}")
