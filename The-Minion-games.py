def minion_game(string):

    s = string.upper()
    vowel = ['A', 'E', 'I', 'O', 'U']
    Kevin_score = 0
    Stuart_score = 0

    for i in range(len(s)):
        if s[i] in vowel:
            Kevin_score = Kevin_score + (len(s) - i)
        if s[i] not in vowel:
            Stuart_score = Stuart_score + (len(s) - i)

    if Kevin_score > Stuart_score:
        print("Kevin", Kevin_score)
    elif Kevin_score < Stuart_score:
        print("Stuart", Stuart_score)
    else:
        print("Draw")
