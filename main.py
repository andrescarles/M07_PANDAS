from ejercicioA import funcion1,funcion2,funcion3
import matplotlib.pyplot as plt

#funcion para imprimir graficos.
def funcion4():
    #bucles para ir haciendo graficos de cada DataFrame.
    for a in funcion1():
        a.unstack()['total_cases'].plot.bar(rot=0)
        print(plt.show())
    #Dejo comentada la funcion 2 y 3.
    """
    for a in funcion2():
        a.unstack()['total_deaths'].plot.bar(rot=0)
        print(plt.show())
    for a in funcion3():
        a.unstack()['reproduction_rate'].plot.bar(rot=0)
        print(plt.show())"""

#LLamadas a las funciones
#print(funcion1())
#print(funcion2())
#print(funcion3())
funcion4()
