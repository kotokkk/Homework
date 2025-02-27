"""
С помощью декораторов реализовать конвейер сборки бургера

Написать декоратор bread, который:
 - до декорируемой функции будет печатать "</------------\\>"
 - после декорируемой функции будет печатать "<\\____________/>"


Написать декоратор tomato, который:
 - до декорируемой функции будет печатать "*** помидоры ****"

Написать декоратор salad, который:
 - до декорируемой функции будет печатать "~~~~ салат ~~~~~"

Написать декоратор cheese, который:
 - до декорируемой функции будет печатать "^^^^^ сыр ^^^^^^"

Написать декоратор onion, который:
 - до декорируемой функции будет печатать "----- лук ------"

Написать функцию beef, которая:
 - печатает "### говядина ###"

Написать функцию chicken, которая:
 - печатает "|||| курица ||||"

1) Собрать с помощью декораторов гамбургер:
    - булка
    - лук
    - помидоры
    - говядина
    - булка

2) Собрать с помощью декораторов чикенбургер:
    - булка
    - сыр
    - салат
    - курица
    - булка
"""

def bread(func):
    def wrap():
        print("</------------\\>")
        func()
        print("<\\____________/>")
    return wrap



def tomato(tom):
    def wrap():
        print("*** помидоры ****")
        tom()
    return wrap

def cheese(chees):
    def wrap():
        print("^^^^^ сыр ^^^^^^")
        chees()
    return wrap



def salad(sal):
    def wrap():
        print("~~~~ салат ~~~~~")
        sal()
    return wrap


def onion(oni):
    def wrap():
        print("----- лук ------")
        oni()
    return wrap

@bread
@cheese
@salad
def chicken():
    print("|||| курица ||||")

chicken()




# @bread
# @onion
# @tomato
# def beef():
#     print("### говядина ###")

# beef()