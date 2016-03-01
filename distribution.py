"""
distribution.py
Author: Glen
Credit: Adam, Stack overflow

Assignment:

Write and submit a Python program (distribution.py) that computes and displays 
the distribution of characters in a given sample of text.

Output of your program should look like this:

Please enter a string of text (the bigger the better): The rain in Spain stays mainly in the plain.
The distribution of characters in "The rain in Spain stays mainly in the plain." is:
iiiiii
nnnnnn
aaaaa
sss
ttt
ee
hh
ll
pp
yy
m
r

Notice about this example:

* The text: 'The rain ... plain' is provided by the user as input to your program.
* Uppercase characters are converted to lowercase
* Spaces and punctuation marks are ignored completely.
* Characters that are more common appear first in the list.
* Where the same number of characters occur, the lines are ordered alphabetically. 
  For example, in the printout above, the letters e, h, l, p and y both occur twice 
  in the text and they are listed in the output in alphabetical order.
* Letters that do not occur in the text are not listed in the output at all.
"""
x = 0
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

#put quotes in around words
words = str(input("Please enter a string of text (the bigger the better): "))
print('The distribution of characters in "{0}" is:'.format(words))
words = words.lower()

letters = list(words)
bears = []

for i in range (0, 26):
    bears.append(letters.count(alphabet[i]))
bears2 = list(zip(bears, alphabet))
#bears2 = sorted(bears2)

final = sorted(bears2, key=lambda bears2: (-bears2[1], bears2[0]))

"""
print(final)

for z in range (25, 0, -1):
    print(bears2[z][0]*bears2[z][1])
 """
    








