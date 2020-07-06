
'''
Kevin and Stuart want to play the 'The Minion Game'.

Game Rules

Both players are given the same string,
.
Both players have to make substrings using the letters of the string

.
Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels.
The game ends when both players have made all possible substrings.

Scoring
A player gets +1 point for each occurrence of the substring in the string

.

For Example:
String
= BANANA
Kevin's vowel beginning word = ANA
Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points. 
'''

# issue with program is that it takes lot of run-time when input string is very large







from timeit import default_timer as timer
def minion_game(string):
    start = timer()
    kevin = 0
    stuart = 0
    word = string
    size = len(word)
    vowel= "AEIOU"
    for i in range(0,size):
        for j in range(size,0,-1):
            if(word[i:j]==''):
                continue
            new = word[i:j]
            if(new[0] in vowel):
                kevin += 1
            else:
                stuart += 1
    if (kevin > stuart):
        print("Kevin {}".format(kevin))
    else:
        print("Stuart {}".format(stuart))
    stop = timer()
    print(stop-start)
        
s = raw_input()
minion_game(s)
