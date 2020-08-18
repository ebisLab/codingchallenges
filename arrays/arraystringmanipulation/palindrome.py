word = "AJKMLNFDBKSTRUBJQAZWSQWERTYUIOPFUNASDFGHJKLXLKHJGFDSANUFPOIUYTREWQSWZAQJBURTSKBDFNLMKJA"
word2 = "hey"


def isPalidrom(word):
    return word == word[::-1]


print(isPalidrom(word2))
