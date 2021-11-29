amount = float(input("Please enter an amount\n>>> "))
sentence = []

digits = ["Error",
          "One",
          "Two",
          "Three",
          "Four",
          "Five",
          "Six",
          "Seven",
          "Eight",
          "Nine"]
tens = ["Error",
          "Ten",
          "Twenty",
          "Thirty",
          "Forty",
          "Fifty",
          "Sixty",
          "Seventy",
          "Eighty",
          "Ninety"]
extra = ["Error",
         "Eleven",
         "Twelve",
         "Thirteen",
         "Fourteen",
         "Fifteen",
         "Sixteen",
         "Seventeen",
         "Eighteen",
         "Nineteen"]

hundredAppend = 0
tenAppend = 0
oneAppend = 0
tenthAppend = 0
penceAppend = 0

if amount // 100 >= 1: # can't be > 0 because of glitch
    hundredAppend = int(amount // 100)
if (amount % 100) // 10 >= 1:
    tenAppend = int((amount % 100) // 10)
if amount % 10 >= 1:
    oneAppend = int(amount % 10)
if (amount % 1) // 0.1 >= 1:
    tenthAppend = int(amount % 1 * 10)
if round(amount % 0.1 * 100) >= 1 and int(amount) != amount: # sanity check to sort glitch
    penceAppend = int(round(amount % 0.1 * 100))

if hundredAppend > 0:
    sentence.append(digits[hundredAppend])
    sentence.append("hundred")
    if tenAppend > 0 or oneAppend > 0 or tenthAppend > 0 or penceAppend > 0:
        sentence.append("and")
if tenAppend > 0:
    if tenAppend == 1 and oneAppend > 0:
        sentence.append(extra[oneAppend])
    else:
        sentence.append(tens[tenAppend])
if oneAppend > 0 and tenAppend != 1:
    sentence.append(digits[oneAppend])
if hundredAppend > 0 or tenAppend > 0 or oneAppend > 0:
    sentence.append("pounds")
    if tenthAppend > 0 or penceAppend > 0:
        sentence.append("and")
if tenthAppend > 0:
    if tenthAppend == 1 and penceAppend > 0:
        sentence.append(extra[penceAppend])
    else:
        sentence.append(tens[tenthAppend])
if penceAppend > 0 and tenthAppend != 1:
    sentence.append(digits[penceAppend])
if tenthAppend > 0 or penceAppend > 0:
    sentence.append("pence")
if not amount > 0:
    print("Please enter an amount")
else:
    sentence.append("only")
    print(" ".join(sentence))
