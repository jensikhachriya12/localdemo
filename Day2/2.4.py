"Take a input to test if a string is a valid pin or not."

def vaild_pin(pin):
    if(len(pin)!=4 and len(pin)!=6 and pin.isdigit()):
        return False
    return True

pin=input("enter pin:")
if vaild_pin(pin):
    print("valid pin")
else:
    print("not valid pin")

    
