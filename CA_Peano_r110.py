# AC SOBRE UNA GEOMETRÍA DE UNA CURVAS DE PEANO QUE USA LA REGLA 110
# 111 -> 0
# 110 -> 1
# 101 -> 1
# 100 -> 0
# 011 -> 1
# 010 -> 1
# 001 -> 1
# 000 -> 0

def transitionFunction(ngbhood):
    ''' ngbhood es una lista de longitud 3, cada entrada es True o False'''
    if ngbhood[0] == True and ngbhood[1] == True and ngbhood[2] == True:
        return False
    elif ngbhood[0] == True and ngbhood[1] == True and ngbhood[2] == False:
        return True
    elif ngbhood[0] == True and ngbhood[1] == False and ngbhood[2] == True:
        return True
    elif ngbhood[0] == True and ngbhood[1] == False and ngbhood[2] == False:
        return False
    elif ngbhood[0] == False and ngbhood[1] == True and ngbhood[2] == True:
        return True
    elif ngbhood[0] == False and ngbhood[1] == True and ngbhood[2] == False:
        return True
    elif ngbhood[0] == False and ngbhood[1] == False and ngbhood[2] == True:
        return True
    elif ngbhood[0] == False and ngbhood[1] == False and ngbhood[2] == False:
        return False
