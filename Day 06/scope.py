# LEGB
# global scope
globalvar = 'global'
def globalScope():
    print('global var:', globalvar)

globalScope()

# local scope
def localScope():
    localvar = 'local'
    print('local var:', localvar)

localScope()
# enclosing scope
def enclosingScope():
    enclosingvar = 'enclosing'
    def nestedScope():
        print('enclosing var:', enclosingvar)
    nestedScope()
enclosingScope()
# loop and condition has no prior scope
if 5>4:
  notScoped='notScoped'
print('notScoped:', notScoped)

# built-in scope
name = 'chaudhuree'
print('name:', name)
print(len(name))