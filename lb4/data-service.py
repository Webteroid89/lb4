from dataclasses import dataclass

@dataclass
class TypeOfMainAssets:
    code: int
    name: str
    nome3: str
    rimainder3: float


@dataclass
class MoveOfMainAssets:
    code: int
    name: str
    second_name: float
    tenth_name: float
    fourteenth_name: float
    twenty_fourth_name: float
    name2: str

type_array = []
type_array.append(TypeOfMainAssets(10, "Яловичина", "Кг", 25.5))
type_array.append(TypeOfMainAssets(20, "Свинина", "Кг", 26.5))
type_array.append(TypeOfMainAssets(30, "Сало", "Кг", 15.0))

move_array = []
move_array.append(MoveOfMainAssets(10, "Яловичина", 25.5, 23.5, 30.8, 23.7, "серпень"))
move_array.append(MoveOfMainAssets(20, "Свинина", 25.0, 25.5, 25.5, 25.7,"серпень"))
move_array.append(MoveOfMainAssets(30, "Сало", 14.4, 14.5, 14.5, 14.5,"серпень"))
move_array.append(MoveOfMainAssets(10, "Яловичина", 23.5, 24.0, 24.0, 24.5,"вересень"))
move_array.append(MoveOfMainAssets(20, "Свинина", 25.5, 26.0, 26.3, 26.5,"вересень"))
move_array.append(MoveOfMainAssets(30, "Сало", 14.5, 14.6, 14.8, 15.0,"вересень"))
move_array.append(MoveOfMainAssets(10, "Яловичина", 25.0, 25.0, 25.5, 25.5,"жовтень")) 
move_array.append(MoveOfMainAssets(20, "Свинина", 26.6, 26.8, 27.0, 27.4,"жовтень"))
move_array.append(MoveOfMainAssets(30, "Сало", 15.5, 15.5, 15.6, 16.0,"жовтень"))

def printMoveOfMainAssets(moveOfMainAssets):
    '''printMoveOfMainAssets function prints
    "Ринкові ціни на продукти по місяцях"
    with names and values'''
    
    print("Назва товару: {name}, Код товару:{code}, На 2 число місяца:{second_name}, На 10 число місяца:{tenth_name}, На 14 число місяца:{fourteenth_name} На 24 число місяца:{twenty_fourth_name}, Місяць:{name2}"
            .format(name=moveOfMainAssets.name, code=moveOfMainAssets.code, second_name=moveOfMainAssets.second_name,
             tenth_name=moveOfMainAssets.tenth_name, fourteenth_name=moveOfMainAssets.fourteenth_name, twenty_fourth_name=moveOfMainAssets.twenty_fourth_name, name2=moveOfMainAssets.name2))

for data in move_array:
    printMoveOfMainAssets(data)

def printTypeOfMainAssets(typeOfMainAssets):
    '''printTypeOfMainAssets function prints
    "Роздрібна ціна, грн"
    with names and values'''

    print("Код: {code}, Назва товару: {name}, Одиниця виміру: {nome3}, Роздрібна ціна: {rimainder3}"
            .format(code=typeOfMainAssets.code, name=typeOfMainAssets.name, nome3=typeOfMainAssets.nome3, rimainder3=typeOfMainAssets.rimainder3))

for data in type_array:
    printTypeOfMainAssets(data)

