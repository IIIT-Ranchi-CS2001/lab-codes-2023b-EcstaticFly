import matplotlib.pyplot as plt
import random 

def check_numbers(list):
    composite_no=[]
    prime_no=[]
    for num in list:
        p=True
        if num==0 or num==1:
            continue
        for i in range(2,num):
            if num%i==0:
                composite_no.append(num)
                p=False
                break
        if p==True:
            prime_no.append(num)
    return prime_no,composite_no            
                


k=int(input())
while k<10:
    print("Enter no. greater than 10")
    k=int(input())
n=int(input())


random_numbers = [random.randint(0, n) for _ in range(k)]
print(random_numbers)
print(" ")
prime_numbers, composite_numbers=check_numbers(random_numbers)
print(f"Prime no. List is {prime_numbers}")
print(f"Composite no. List is {composite_numbers}")

prime_numbers_square=[x**2 for x in prime_numbers]
composite_numbers_square=[x**2 for x in composite_numbers]

print(prime_numbers_square)
print(composite_numbers_square)

figure,axs=plt.subplots(1,2)

if prime_numbers:
    axs[0].scatter(prime_numbers,prime_numbers_square)
    axs[0].set_title("Prime Number VS Square of Prime Number")
    axs[0].set_xlabel("Prime Number")
    axs[0].set_ylabel("Square of Prime Number")

if composite_numbers:
    axs[1].scatter(composite_numbers,composite_numbers_square)
    axs[1].set_title("Composite Number VS Square of Composite Number")
    axs[1].set_xlabel("Composite Number")
    axs[1].set_ylabel("Square of Composite Number")

plt.show()