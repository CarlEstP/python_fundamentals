def buscar_nombre(lista_nombres):
    nombre_a_buscar = input("Ingrese el nombre a buscar en la lista: ").strip()
    # nombre_a_buscar = "Silviaa"
        
    if nombre_a_buscar in lista_nombres:
      print(f'El nombre "{nombre_a_buscar}" fue encontrado en la lista.')
    else:
      print(f'El nombre "{nombre_a_buscar}" no fue encontrado en la lista.')

# Ejemplo de uso
lista_nombres = ["Jaime", "Silvia", "Ana"]
buscar_nombre(lista_nombres)