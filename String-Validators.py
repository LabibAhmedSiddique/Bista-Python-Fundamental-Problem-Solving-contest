s = input()


def StringChecker(str):
    for i in range(len(str)):
        if (str[i].isalnum()):
            return True
        # break
    return False


def StringChecker2(str):
    for i in range(len(str)):
        if (str[i].isalpha()):
            return True
        # break
    return False


def StringChecker4(str):
    for i in range(len(str)):
        if (str[i].isdigit()):
            return True
        # break
    return False


def StringChecker5(str):
    for i in range(len(str)):
        if (str[i].islower()):
            return True
        # break
    return False


def StringChecker6(str):
    for i in range(len(str)):
        if (str[i].isupper()):
            return True
        # break
    return False


print(StringChecker(s))
print(StringChecker2(s))
# print(StringChecker3(s))
print(StringChecker4(s))
print(StringChecker5(s))
print(StringChecker6(s))
