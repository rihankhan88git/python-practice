print("------------------fruit list---------------------")
fruits=['apple','banana','mango','pineapple','orange']
for fruit in fruits:
    print(fruit)


print("--------------**** num list ****--------------------")
num= 111,22,3,3344,55,66,88,446,89,35,23,56,34,55,
for num in num:
    print(num)



print("--------------**** name list ****---------------------")
name= ['aman','rihan','samir','rahul','vijay','anil','sunil','sharma']
for name in name:
    print(name)



print("--------------****  RANGE list ****---------------------")
for Rlist in range(10,25):
    print(Rlist)



print("--------------**** negative RANGE list ****---------------------")
for NRlist in range(-25,25):
    print(NRlist)


print("--------------**** step range  list ****---------------------")
for rangelist in range(1,25+3,2):
    if rangelist==15:
        break
    print(rangelist)


print("--------------**** continue range  list ****---------------------")
for rangelist in range(3,36,2):
    if rangelist==15:
        continue
    print(rangelist)



