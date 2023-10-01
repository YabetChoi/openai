
numbers = [5, 7, 2, 9, 1, 10, 4, 6, 8, 3]
numbers.sort()
print(numbers[-1])


number = 5
if number % 2 == 0:
    print("짝수")
else:
    print("홀수")


for i in range(1, 11):
    if i % 2 != 0:
        print(i)

sample_dict = {'A': 10, 'B': 20, 'C': 30, 'D': 40}
for key, value in sample_dict.items():
    if value == 30:
        print(key)

name = input("What is your name? ")
print("Hello " + name)

