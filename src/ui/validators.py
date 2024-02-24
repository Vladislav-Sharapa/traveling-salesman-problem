def validator(input: str):
    if input.isdigit() and input != '0':
        return True
    elif input == "": 
        return True
    else:
        return False

    

