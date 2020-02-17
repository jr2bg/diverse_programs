# AC SOBRE UNA GEOMETRÍA DE UNA CURVAS DE PEANO QUE USA LA REGLA 110
# 111 -> 0
# 110 -> 1
# 101 -> 1
# 100 -> 0
# 011 -> 1
# 010 -> 1
# 001 -> 1
# 000 -> 0

import turtle

def transitionFunctionRule110(ngbhood):
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

def productionsHilbertCurve(chr):
    if chr == "A":
        return "−BF+AFA+FB−"
    elif chr == "B":
        return "+AF−BFB−FA+"
    return chr

def PeanoCurve(n_iter):
    ''' size_m es el tamaño de la matriz, debe ser un múltiplo de 3'''
    chain = "A"
    n_chain = ""
    for i in range(n_iter - 1):
        for chr in chain:
            n_chain += productionsHilbertCurve(chr)
        chain = n_chain
        n_chain = ""
        #print(chain)
    return chain

if __name__ == "__main__":
    turtle.hideturtle()
    turtle.speed(0)
    turtle.setheading(90)
    turtle.tracer(0,0)

    turtle.color('green', 'yellow')

    chain = PeanoCurve(6)

    for chr in chain:
        if chr == "F":
            turtle.forward(5)
        elif chr == "−":
            turtle.left(90)
        elif chr == "+":
            turtle.right(90)
    turtle.update()
    turtle.done()
