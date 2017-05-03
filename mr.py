f = open("barryLyndon.txt", "r")
text = f.read()
f.close()
lines = text.split("\r\n") #convert text to lines
words = []
for element in lines:
    words += element.replace("\xe2\x80\x98", "").replace("\xe2\x80\x99", '').replace(";", "").replace(":", "").replace(",", "").replace(".", "").replace("-"," ").replace("(","").replace(")", "").lower().split(" ") #remove crap from text


def wordCount(word): #gets the frequency of one word in the book
    def h(w):
        return w == word.lower()
    a = filter(h, words)
    return len(a)

def wordsCount(wordList):
    a = filter(lambda x : True if x in wordList else False, words)
    return len(a)

def makeWordDict(a): #makes a dict of all the words and how often they occur
    def f(x):
        try:
            a[x] += 1
        except:
            a[x] = 1
    map(f, words)
    return a

def getWord(dct, num, word): #goes through dict and calculates most common word and how many times it comes up in the story
    for x in dct:
        if dct[x] > num:
            num = dct[x]
            word = x
    return [word, num]

def getFrequentWord(): #utilizes helper functions to get the most common word
    dct = makeWordDict({})
    ans = getWord(dct, 0, "")
    print "The most common word is '" + ans[0] + "' which occurs " + str(ans[1]) + " times in the book"
    return ans[0]


print "\nThe word 'lordship' is used " + str(wordCount("lordship")) + " times\n"

print "The word 'a' is used " + str(wordCount("a")) + " times\n"

print "The word 'barry' is used " + str(wordCount("barry")) + " times\n"

print "The words 'lordship', 'a' and 'barry' occur " + str(wordsCount(['a', 'barry', 'lordship'])) + " times\n"

getFrequentWord()
print '\n'
