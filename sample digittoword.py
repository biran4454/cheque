digitToWord = {1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 
               6:"six", 7:"seven", 8:"eight", 9:"nine", 10:"ten"} 
words = []
for n in range(1, 10, 1): 
    words.append(digitToWord[n])
print(len("".join(words)))
