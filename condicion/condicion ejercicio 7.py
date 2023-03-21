
ingredientes = {
    "vegetariana": ["mozzarella", "tomate", "pimiento", "tofu"],
    "no vegetariana": ["mozzarella", "tomate", "peperoni", "jamón", "salmón"]
}


tipo_pizza = input("¿Quiere una pizza vegetariana? (sí/no): ")


if tipo_pizza.lower() == "sí":
    print("Los ingredientes disponibles para su pizza son:", ingredientes["vegetariana"])
else:
    print("Los ingredientes disponibles para su pizza son:", ingredientes["no vegetariana"])


ingrediente_elegido = input("Seleccione un ingrediente de la lista: ")


if tipo_pizza.lower() == "sí":
    print("Ha elegido una pizza vegetariana con los siguientes ingredientes:",
          ingredientes["vegetariana"][0], ",", ingredientes["vegetariana"][1], "y", ingrediente_elegido)
else:
    print("Ha elegido una pizza no vegetariana con los siguientes ingredientes:",
          ingredientes["no vegetariana"][0], ",", ingredientes["no vegetariana"][1], ",", ingrediente_elegido, "y",
          ingredientes["no vegetariana"][2]) 