'''
This is the factorial program with method
'''

def factro(n):
    answer=n
    while n>1:
        answer=answer*(n-1)
        # j=n-1
        # print(answer)
        n-=1   
    print(answer)   

n = int(input("Pls enter the no. to find the factorial: "))

fac = factro(n)