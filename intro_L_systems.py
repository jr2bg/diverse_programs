# Program for L-systems
# https://en.wikipedia.org/wiki/L-system
#
# Dependencies
# python 3.6

import turtle


# chr a character
def productions_algae(chr):
    ''' Función que devuelve la producción asociada al caracter, como lo
    especificado por Lindenmayer
    '''
    if chr == "A":
        return "AB"

    elif chr == "B":
        return "A"

    return chr

def productions_koch_curve(chr):
    ''' Producciones para la curva de Koch
    '''
    if chr == "F":
        return "F+F-F-F+F"
    return chr


def productions_fractal_plant(chr):

    if chr == "X":
        return "F+[[X]-X]-F[-FX]+X"
    elif chr == "F":
        return "FF"

    return  chr



def computation(cadena, productions = productions_algae):
    ''' Computación para una cadena de acuerdo a alguna regla de producción,
    por default, la regla será la de crecimiento de algas
    '''
    s = ""
    for chr in cadena:
        s += productions(chr)
    return s


if __name__ == "__main__":
    turtle.shape("turtle")
    turtle.speed(10)
    turtle.setheading(90)
    turtle.penup()
    turtle.setpos(-00,-150)
    turtle.pendown()
    turtle.color('green', 'yellow')
    print(turtle.pos())
    #cadena = "A"
    # posiciones de la tortugaaaaa
    t_positions = []
    t_directions = []
    cadena = "X"#"F"
    for i in range(5):
        cadena = computation(cadena, productions_fractal_plant)

    # print(cadena)
    # for chr in cadena:
    #     if chr == "F":
    #         turtle.forward(5)
    #     elif chr == "+":
    #         turtle.left(90)
    #     elif chr == "-":
    #         turtle.right(90)

    for chr in cadena:
        if chr == "F":
            turtle.forward(5)
        elif chr == "-":
            turtle.left(25)
        elif chr == "+":
            turtle.right(25)
        elif chr == "[":
            t_positions.append(turtle.pos())
            t_directions.append(turtle.heading())
        elif chr == "]":
            turtle.penup()
            turtle.setpos(t_positions.pop())
            turtle.setheading(t_directions.pop())
            turtle.pendown()

    turtle.done()
