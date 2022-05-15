from unittest import result

v1 = 'hi there'
v2 = "hi there"
v3 = "i said \"hi there\""
v4 = '''i said "hi there"'''
v5 = "i said i can't do that"
v6 = 'i said "hi there'
print(v1)
print(v2)
print(v3)
print(v4)
print(v5)
print(v6)

# string concatenation
v1 = 'hi there'
v2 = "how are you?"
result = v1+' '+v2
print(result)

result2 = v1+' '+v2+' '+'i am fine'
result3 = v1*3
# result4=v1+3 can not add str with int
print(result2)
print(result3)
# print(result4)
