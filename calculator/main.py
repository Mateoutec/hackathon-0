# calculator/main.py

def calcular(operacion):
    """
    Evalúa una operación matemática escrita como string.
    """
    try:
        resultado = eval(operacion)
        return resultado
    except ZeroDivisionError:
        return "Error: División por cero."
    except Exception as e:
        return f"Error en la operación: {e}"

def main():
    print("=== Calculadora de Línea de Comandos ===")
    print("Escribe operaciones como '2 + 2' y presiona Enter")
    print("Presiona 'c' para limpiar y 'q' para salir")

    while True:
        entrada = input(">>> ")

        if entrada.lower() == 'q':
            print("Saliendo de la calculadora. ¡Hasta luego!")
            break
        elif entrada.lower() == 'c':
            print("Operación borrada.")
            continue
        else:
            resultado = calcular(entrada)
            print("Resultado:", resultado)

if __name__ == "__main__":
    main()

