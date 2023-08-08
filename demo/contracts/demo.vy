greeting: public(string)

@public
def __init__(_greeting: string):
    self.greeting = _greeting

@public
def setGreeting(_greeting: string):
    self.greeting = _greeting

@public
@view
def getGreeting() -> string:
    return self.greeting
