def primechecker(number):
    if number < 2:
        return False
    else:
        for checker in range(2, number):
            if number % checker == 0:
                return False
        return True  
                