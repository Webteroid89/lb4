from dataclasses import dataclass

@dataclass
class TypeOfMainAssets:
    code: int
    name: str
    type: str
    code2:float


@dataclass
class MoveOfMainAssets:
    name: str
    name2:str
    code: int
    remainder: float
    remainder2:float
    received: float
    output: float

type_array = []
type_array.append(TypeOfMainAssets(10, "Яловичина"))
type_array.append(TypeOfMainAssets(20, "Свинина"))
type_array.append(TypeOfMainAssets(30, "Сало"))

move_array = []
move_array.append(MoveOfMainAssets("Яловичина", 25.5, 23.5, 30.8, 23.7))
move_array.append(MoveOfMainAssets("Свинина", 25.0, 25.5, 25.5, 25.7))
move_array.append(MoveOfMainAssets("Сало", 14.4, 14.5, 14.5, 14.5))
move_array.append(MoveOfMainAssets("Яловичина", 23.5, 24.0, 24.0, 24.5))
move_array.append(MoveOfMainAssets("Свинина", 25.5, 26.0, 26.3, 26.5))
move_array.append(MoveOfMainAssets("Сало", 14.5, 14.6, 14.8, 15.0))
move_array.append(MoveOfMainAssets("Яловичина", 25.0, 25.0, 25.5, 25.5))
move_array.append(MoveOfMainAssets("Свинина", 26.6, 26.8, 27.0, 27.4))
move_array.append(MoveOfMainAssets("Сало", 15.5, 15.5, 15.6, 16.0))

def printMoveOfMainAssets(moveOfMainAssets):
    '''printMoveOfMainAssets function prints
    "Ринкові ціни на продукти по місяцях"
    with names and values'''
    
    print("Назва товару: {name}, Код товару:{code}, На 2 число місяца:{remainder}, На 10 число місяца:{remainder2}, На 14 число місяца:{received} На 24 число місяца:{output}, Місяць:{name2}"
            .format(name=moveOfMainAssets.mame, name2=moveOfMainAssets.name2, code=moveOfMainAssets.code, remainder=moveOfMainAssets.remainder,
                    remainder2=moveOfMainAssets.remainder2, received=moveOfMainAssets.received, output=moveOfMainAssets.output))

for data in move_array:
    printMoveOfMainAssets(data)

def printTypeOfMainAssets(typeOfMainAssets):
    '''printTypeOfMainAssets function prints
    "Роздрібна ціна, грн"
    with names and values'''

    print("Код: {code}, Назва товару: {name}, Одиниця виміру: {name2}, Роздрібна ціна: {code2}"
            .format(code=typeOfMainAssets.code, name=typeOfMainAssets.name, type=typeOfMainAssets.type2), code2=typeOfMainAssets.code2)

for data in type_array:
    printTypeOfMainAssets(data)

