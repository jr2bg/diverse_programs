# Dada una fórmula phi, una variable x y un término t
# este programa determinará si t es sustituible por x en phi
# Por utilidad, tanto phi como t se tomarán como listas y x como una cadena

def isTerm(t):
    ''' solo depende de si la cadena empieza con t para determinar si es término'''
    if t.startswith("t"):
        return True
    return False

def isAtomic(phi):
    ''' función que determina si la fórmula phi es atómica o no'''
    if len(phi) == 3 and phi[0] == "=":
        # formula para "igualdad"
        for element in phi[1:]:
            if not isTerm(element):
                return False
            return True

    elif isNAryRelation(phi[0]):
        #fórmula de relación
        for element in phi[1:]:
            if not isTerm(element):
                return False
        return True
    else:
        return False

def isFree(v, phi):
    if isAtomic(phi) and v in phi:
        return True
    elif phi[0] == "(" and phi[-1] == ")":
        if len(phi) == 4 and phi[1] == "NEG" and isFree(v,phi[2]):
            return True
        elif len(phi) == 5 and phi[2] == "VEE" and (isFree(v, phi[1]) or isFree(v,phi[3])):
            return True
        elif phi[1] == "FORALL" and isVariable(phi[2]) and phi[3] == ")" and phi[4] == "(" and isFree(v,phi[5]):
            return True
    else:
        return False

def isSubstitutable(phi, x, t):
    if isAtomic(t):
        return True
    elif len(phi) == 7 and phi[0]=="(" and phi[-1]==")" and phi[1]== "FORALL" and
                        isVariable(phi[2]) and phi[3]== ")" and phi[4] =="(" and
                        not isFree(x, phi):
        return True
    else:
        if len(phi) == 4 and phi[0] == "(" and phi[-1] == ")" and phi[1] == "NEG" and isSubstitutable(phi[2], x, t):
            return True
        elif len(phi) == 5 and phi[2] == "VEE" and isSubstitutable(phi[1],x,t) and isSubstitutable(phi[3],x,t):
            return True
        elif len(phi) == 7 and phi[0]=="(" and phi[-1]==")" and phi[1]== "FORALL" and
                            isSubstitutable(phi[5],x,t) and (y not in t):
            return True
        return False
