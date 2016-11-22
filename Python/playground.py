#Hola mundo
print("Hello world")

#Listas
print("-------------------------------------")
fruits=["Apple","Orange","Watermelon"]
print(fruits[0])
print(fruits[1])
print(fruits[2])
print(fruits[-1])
print(fruits[-2])
print(fruits[-3])


#Slicing de listas
print("-------------------------------------")
numbers=[0,1,2,3,4,5,6,7,8,9]
from_2_to_6=numbers[2:7]
print(from_2_to_6)

greater_than_4=numbers[5:]
print(greater_than_4)
print(numbers[::2])
print(numbers[1::2])

#Diccionarios
print("-------------------------------------")
fighter={"name":"Naruto","last_name":"Uzumaki","technique":"Rasengan"}
print(fighter["name"])
print(fighter.get("nombre")) #Result: None == Null

#Funciones
print("-------------------------------------")
def print_fruits(fruits_list):
	for fruit in fruits_list:
		print(fruit)

print_fruits(fruits)
