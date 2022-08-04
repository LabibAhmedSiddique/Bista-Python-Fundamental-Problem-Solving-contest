def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        x = string[i:i+k]
        print("".join(dict.fromkeys(x)))
