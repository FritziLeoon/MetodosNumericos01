def encontrar_piso_minimo(n_pisos, objetos):
    bajo = 1  # El piso más bajo
    alto = n_pisos  # El piso más alto
    intentos = 0  # Contador de intentos

    while bajo <= alto:
        medio = (bajo + alto) // 2  # Divide el rango en dos mitades
        intentos += 1

        # Simula la caída del objeto desde el piso medio
        if caida_objeto(medio) == "se_rompe":
            alto = medio - 1  # El objeto se rompe, busca en el rango inferior
        else:
            bajo = medio + 1  # El objeto sigue intacto, busca en el rango superior

    return bajo, intentos

# Función para simular la caída del objeto desde un piso dado
def caida_objeto(piso):
    # Aquí debes implementar la lógica de tu simulación
    # Devuelve "se_rompe" si el objeto se rompe y "se_mantiene_intacto" si no
    # Esto depende de la resistencia del objeto y el piso desde el que cae
    pass

# Ejemplo de uso
n_pisos = 100
objetos = 2
piso_minimo, intentos_realizados = encontrar_piso_minimo(n_pisos, objetos)
print(f"El piso mínimo desde el cual los objetos se rompen es {piso_minimo}.")
print(f"Se realizaron {intentos_realizados} intentos para encontrarlo.")
