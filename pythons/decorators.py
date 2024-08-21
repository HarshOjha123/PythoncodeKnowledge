#defining decorator
def dec(fnc):
    def abc(): #wrapper function
        fnc()
        print("hi all")
    return abc
def xyz(): #actual function
    print("my name is ")
x=dec(xyz)
xyz()