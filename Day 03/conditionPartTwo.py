# more advance condition cases
# nested condition

"""
f=212
c=100
k=373
"""

units = input('enter your unit: f/c or k ->')
temp = int(input('what is the temperature of your water ->'))

if(units == "f"):
    if(temp == 212):
        print('your water is boiling')
    else:
        print('your water is not boiling, boiling temperature is 212')
if(units == "c"):
    if(temp == 100):
        print('your water is boiling')
    else:
        print('your water is not boiling, boiling temperature is 100')
if(units == "k"):
    if(temp == 373):
        print('your water is boiling')
    else:
        print('your water is not boiling, boiling temperature is 373')
