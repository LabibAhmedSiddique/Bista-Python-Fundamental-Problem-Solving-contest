import sys


inp = str(input("welcome to bista git manager :"))
i = 1
dicta = {}
if inp == "exit":
    print("---end terminal---")
    sys.exit()
elif inp == "git init":
    while inp == "git init":
        print("---Initialize git---")
        print()

        x = list(input().split())
        # print(x)
        if x[1] == "commit":
            words = x[3:-1]

            sentence = " ".join(words)
            # print(sentence)

            dicta[i] = sentence
            # print(dicta)
            i += 1

            items = ', '.join(f'{key} {value}' for key, value in dicta.items())

            # print(items)

        elif x[1] == "show" and x[2] == "all":
            z = len(dicta)
            for z in dicta:
                print(z, dicta[z])

        elif x[1] == "show":
            z = len(dicta)

            print(z, dicta[z])

        elif x[1] == "delete":
            z = int(x[len(x)-1])
            if z in dicta:
                del dicta[z]
        elif x[1] == "update":
            z = i-1
            print('test last idx')
            print(z)

            d1 = {z: x[3:-1]}
            dicta.update(d1)
        elif x[1] == "jump":
            di2 = {}
            z = int(x[len(x)-1])
            s = dicta[z]
            if z in dicta:
                di2 = {z: s}
