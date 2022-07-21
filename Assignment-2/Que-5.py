print("Enter a number:")
num = int(input())
factorial=1
if num>0:
    for i in range(1, num+1):
        factorial=factorial*i
    print(f'The factorial of {num} is {factorial}')
elif num>0:
    print(f'The factorial for {num} does not exist for negative number')
elif num ==0:
    print(f'The factorial for {num} is 0')
