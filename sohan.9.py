num = int(input('enter a number:'))
reversed = 0
x = num
while num > 0:
   reversed = (reversed * 10) + num%10
   num = num // 10
print(reversed)
if x == reversed:
    print("palindrome number")
else:
    print(" not a palindrome number")
