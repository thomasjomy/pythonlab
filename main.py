# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from sentence import Sentence

s = Sentence('"The time has come," the Walrus said,')
list(s)
for word in s:
    print(word)

