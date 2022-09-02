import sys


inp = str(input("welcome to bista git manager :"))
i = 0
list1 = []
list2 = []
pointer_back = 0
pointerStr = False
if inp == "exit":
    print("---end terminal---")
    sys.exit()
elif inp == "git init":
    while inp == "git init":

        x = list(input().split())

        if x[0] == "exit":
            print("---end terminal---")
            sys.exit()
        elif x[0] == "git":

            if x[1] == "commit":

                words = x[3:-1]
                sentence = " ".join(words)
                if pointerStr == False:
                    list1.append(sentence)
                    i = i+1
                    list2.append(i)
                else:
                    for t in range(pointer_back):
                        list1.pop()
                        list2.pop()
                        pointerStr = False
                        pointer_back = 0

                    list1.append(sentence)
                    i = i+1
                    list2.append(i)
            elif x[1] == "show" and x[2] == "all":
                pointer = (len(list2)-1)-pointer_back
                for e in range(len(list2), 0, -1):
                    if e == pointer:
                        print('*'+str(list2[e-1])+" "+str(list1[e-1]))
                    else:
                        print(str(list2[e-1])+" "+str(list1[e-1]))
            elif x[1] == "show" and x[2] == "commit":
                print(list1[-1])
            elif x[1] == "delete":
                y = int(x[len(x)-1])
                if y == int(len(list1)):
                    del list1[y-1]
                    del list2[y-1]

            elif x[1] == "jump":
                y = int(x[len(x)-1])
                p = list1.pop(y-1)
                q = list2.pop(y-1)
                list1.append(p)
                list2.append(q)

            elif x[1] == "update":

                words2 = x[3:-1]
                sentence2 = " ".join(words2)

                list1[pointer-1] = sentence2

            elif x[1] == "move" and x[2] == "back":
                pointerStr = True
                pointer_back = pointer_back+1
                print(pointer_back)
            else:
                break

        else:
            print("invalid input")
