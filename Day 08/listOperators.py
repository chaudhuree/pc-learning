# list operators

even=[2,4,6,8,10]
odd=[1,3,5,7,9]
both=even+odd

print(f"even: {even} \nodd: {odd} \nboth: {both}")

# in operator in list

flavours=['vanilla','chocolate','strawberry','mango','butterscotch']

response=input('which flavour do you want??')

while response.lower() not in flavours:
    response=input('i do not know about this flavour.please enter againg :')

print(f"ok, {response} icecreame coming up")