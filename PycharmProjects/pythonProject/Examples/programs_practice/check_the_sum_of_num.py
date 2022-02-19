num = 12345
#print(num/10)
# print(num%10)
# print(num//10)
result = 0
while num != 0:
    mod = num % 10
    print(mod)
    result += mod
    num = num // 10
print(result)

# print(7//10)
# print(7%10)