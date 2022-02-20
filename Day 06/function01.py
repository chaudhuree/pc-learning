# function with default parameters
def fullName(first_name, last_name='chaudhuree'):
    return first_name + ' ' + last_name


print(fullName('sOhan'))

# ordering of parameters

# this will throw an error
# def greetings(msg='Good morning,',name):
#   print(msg,name)
# greetings('sOhan')


def greetings(name, msg='Good morning,'):
    print(msg, name)


greetings('sOhan')

# keyword arguments


def greetings_k(name, msg):
    print(msg, name)


greetings_k(name='chaudhuree', msg='bye bye!!,')
# number of argument should be matched with the number of parameters


# get total 

def get_total(price,qty,tax,discount=0):
    subtotal = price * qty*(1-discount)
    total = subtotal * (1+tax)
    return round(total,2)

print(get_total(qty=2,price=9.75,discount=0.2,tax=0.03))