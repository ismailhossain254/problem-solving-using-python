number = 371
num = number
digit, sum = 0, 0
length = len(str(num))
for i in range(length):
  digit = int(num%10)
  num = num/10
  sum += pow(digit,length)
if sum==number:
  print("Its a Armstrong number")
else:
  print("Not a Armstrong number")