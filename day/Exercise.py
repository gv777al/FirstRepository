""" string = input("str")
num = input("num")
final_str = ''
for i in range(int(num)):
    final_str += string
print(final_str) """

''''
Given 2 ints, a and b, return True if one if them is 10 or if their sum is 10.

makes10(9, 10) → True
makes10(9, 9) → False
makes10(1, 9) → True
'''
def makes10(a, b):
  if (a == 10) or (b == 10) or a + b == 10:
    return True
  else: 
    return False

a = 9
b = 10
print(makes10)