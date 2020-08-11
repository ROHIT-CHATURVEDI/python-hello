var = "We Win"
print(var)
print(var[0])
print(var[1])
print(var[2])
print(var[3])
print(var[4])
print(var[5])

print("\n")
vat = "parrot"
print(vat[0])
print(vat[1])
print(vat[2])
print(vat[3])
print(vat[4])
print(vat[5])

print("\n\n")


print(vat . index("p")) # index value = 0 or -6
print(vat . index("a")) # index value = 1 or -5
print(vat . index("r")) # index value = 2 or -4
print(vat . index("r")) # index value = 3 or -3
print(vat . index("o")) # index value = 4 or -2
print(vat . index("t")) # index value = 5 or -1

print("\n\n")
# parrot                                           # We can also find negative value by :-
print(vat[0 - 6]) ## index value = 0 or -6 = p         p = 0 - 6
print(vat[1 - 6]) ## index value = 1 or -5 = a         a = 1 - 6
print(vat[2 - 6]) ## index value = 2 or -4 = r         a = 2 - 6
print(vat[3 - 6]) ## index value = 3 or -3 = r         r = 3 - 6
print(vat[4 - 6]) ## index value = 4 or -2 = o         o = 4 - 6
print(vat[5 - 6]) ## index value = 5 or -1 = t         t = 5 - 6

print("\n","the new example :-")
nat = "Norweigian Blue"
print(nat[0 - 15])
print(nat[1 - 15])
print(nat[2 - 15])
print(nat[3 - 15])
print(nat[4 - 15])
print(nat[5 - 15])
print(nat[6 - 15])
print(nat[7 - 15])
print(nat[8 - 15])
print(nat[9 - 15])
print(nat[10 - 15])
print(nat[11 - 15])
print(nat[12 - 15])
print(nat[13 - 15])
print(nat[14 - 15])

# Performing slice or slicing .
# SYNTAX OF SLICING :- [START VALUE : UPTO VALUE BUT NOT INCLUDING])
print("\n")
print("Here we are Performing Slice or Slicing :- ")
val = "United States of America." # 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
# Here we are performing SLicing :- U n i t e d   S t a t  e  s     o  f     A  m  e  r  i  c  a
print(val[0:7]) # Result  = United .
print(val[7:14]) # Result = States.
print(val[14:16]) # Result = of .
print(val[17:24]) # Result = America .

print("\n")
# Here we can also write full word .
print(val[ : 24])
# And can also write like this :-
print(val[ 0 : ])
# We can also ADD SLICING VALU1ES :-
print(val[ : 7] + val[ 7 : 14 ] + val[ 14 : 16 ] + val[ 17 :])
# Here in one more way , we can print full value/word :-
print(val[:])

print("\n\n")
# Here we can also use Negative values to print or perform slicing or slice.
print("Here we are Printing or Performing using Negative Values :- " , "\n")
print(val[0 - 25 :]) # result = United States of America.
print(val[ 0 - 25 : 6 - 25]) # result  =  United .
print(val[7 - 25 : 13 - 25 ]) # result = States .
print(val[14 -25 : 16 - 25]) # result = of .
print(val[17 - 25 : 24 -25]) # result = America .

# We can also , do in this way :-
 # val = "United States of America."
 # we can find value of index :- syntax = print(variable_name.index("enter string whose value you want"))
print(val [ 0 - 25 : 6 - 25 ] + " " + val [ 7 - 25 : 13 - 25] + " " +  val [ 14 -25 : 16 - 25] +" " + val [17 - 25 : 24 -25])
print(val.index("."))

# Now we are using a New Concept known as :- STEP in method in slice.
print("\n")
print("Now we are using a new method known as 'STEP in' method in slice :- " , "\n")
sal = "1,2,3,4,5,6,7,8,9 ."
print(sal[0::2]) # Result = 123456789 .
print("rohit"[0::2])
print("rohit".index("r"))
print("rohit".index("o"))
print("rohit".index("h"))
print("rohit".index("i"))
print("rohit".index("t"))

print("\n\n")
parrot = "Norweigian Blue"
print(parrot[0::1]) # Result = Norweigian Blue .
print(parrot[0::2]) # Result = Nrega le .
print(parrot[0::3]) # Result = Nwgnl .
print(parrot[0:10:2]) # Result = Nrega .
print(parrot[0:15:4]) # Result = Neal . or we can write it as :- print(parrot[0::4])
print(parrot[0::5]) # Result = Ni
print(parrot[0::6]) # Result = Ngl
print(parrot[0::7]) # Result = Nie

print("\n\n")
print("1,2,3,4,5,6,7,8"[0::2])
van = "1,23,45,56,76,54,56,78"
print(van.index("78"))
print(van[0-22:]) # Result = 1,23,45,56,76,54,56,78 or we write it as :- print(van[0:])


