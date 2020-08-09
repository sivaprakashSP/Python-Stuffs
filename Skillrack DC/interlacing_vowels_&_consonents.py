word = input().strip()
vowels,consonents=[],[]
for letter in word:
    if letter in "AEIOUaeiou":
        vowels.append(letter)
    else:
        consonents.append(letter)
consonents=consonents[::-1]
'''
print(vowels)
print(consonents)
'''
maxlen=max(len(vowels),len(consonents))
for index in range(0,maxlen):
    if index<len(vowels):
        print(vowels[index],end="")
    if index<len(consonents):
        print(consonents[index],end="")