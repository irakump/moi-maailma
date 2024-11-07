def laske(luku):
    for i in range(2, luku):
        jakojaannos = luku % i
        if jakojaannos == 0:
            return False
    return True


