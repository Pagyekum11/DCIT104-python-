# Agyekum Paul
# 10976491
# The sum of prime numbers for a given number.

lower = int(input("enter lower range: "))
upper = int(input("enter upper range: "))
sum = 0
prime = 0
for num in range(lower, upper + 1):
    if num > 1:
        for i in range(2, num):
          if (num % i) == 0:
            break

        else:
            print(num)
            sum = sum + num
            prime = prime + num

print("sum of prime numbers", sum)
print("average of prime", sum/num)




