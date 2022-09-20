
def validate_pin(pin):
    tof = True
    lenght = len(pin)
    tof = pin.isdigit()
    if tof == False:
        return False
    else:
        if lenght == 4 or lenght == 6:
            return True
        else:
            return False

