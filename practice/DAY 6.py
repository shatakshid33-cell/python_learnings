#print numbers from 50 to 2 using while loop
i = 50
while i >= 2:
    #print(i)
    i -= 1 

x=50
while x>=2:
    if x%2==0:
        print(x)
        x=x-2

num=int(input("Enter a number: "))
for i in range(1,11):
    print(num*i)

word= input("Enter a password: ")
if word=="python123":
    print('access granted')
else:
    print('access denied')


details = [('cry', 345), ('brac3', 8874), ('brac', 8474), ('brac2', 8474)]

def gene_name(details):
    set_value=0
    gene=[]

    for i,e in details:
        if e > set_value:
            set_value=e
            gene=[i]
        elif e == set_value:
            gene.append(i)
        else:
            pass

    return (gene,set_value)
print (gene_name(details))
