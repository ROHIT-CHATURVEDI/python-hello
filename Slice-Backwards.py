letters = "abcdefghijklmnopqrstuvwxyz"
print(letters[25::-1]) # we can write it as :- print(letters[::-1])
print(letters.index("a"))
# Challenge by Udemy .
# 1.)  QPO
print("\n\n")
print(letters.index("q"))
print(letters.index("p"))
print(letters.index("o"))
print(letters[16:13:-1]) # Result = qpo
# 2.) EDCBA .
print("\n\n")
print(letters.index("e"))
print(letters.index("d"))
print(letters.index("c"))
print(letters.index("b"))
print(letters.index("a"))
print(letters[4::-1]) # Result = edcba or we can do is as :-
print("\n\n")
#  3.) SLICE THE LAST 8 CHARACTERS IN REVERSE ORDERS.
print(letters[25:17:-1]) # result = zyxwvuts  or we can write it as :- print(letters[:-9:-1])


