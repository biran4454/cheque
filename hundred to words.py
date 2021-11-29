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

tenAppend = 0
oneAppend = 0

if (amount % 100) // 10 >= 1:
    tenAppend = int((amount % 100) // 10)
if amount % 10 >= 1:
    oneAppend = int(amount % 10)
if tenAppend > 0:
    if tenAppend == 1 and oneAppend > 0:
        sentence.append(extra[oneAppend])
    else:
        sentence.append(tens[tenAppend])
if oneAppend > 0 and tenAppend != 1:
    sentence.append(digits[oneAppend])
if amount == 0:
    print("Zero")
else:
    print(" ".join(sentence))
