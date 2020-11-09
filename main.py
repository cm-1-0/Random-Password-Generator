import random

q1 = input("Would you like a key for the program?: ")
l1 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
      "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
      "!", "@", "#", "$", "%", "^", "&", "*", "-", "_",
      "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
if q1 == "Yes":
    for i in range(20):
        k1 = random.choice(l1)
        print(k1)
if q1 == "No":
    print("Goodbye")
