from funciones_agente.obtener_clima import obtener_clima
from funciones_agente.obtener_precio_accion import obtener_precio_accion
from utils.sanitizar import sanitizar_entrada

def main():
    """
    Chatbot que responde preguntas sobre el clima y el precio de acciones.
    """
    print("¡Bienvenido al chatbot! ¿En qué puedo ayudarte? (Escribe 'salir' para terminar)")
    while True:
        consulta = input(">> ")
        consulta = sanitizar_entrada(consulta)

        if "clima" in consulta:
            ciudad = consulta.replace("clima en ", "").strip()
            if ciudad:
                print(obtener_clima(ciudad))
            else:
                print("Por favor, especifica una ciudad. Ejemplo: 'clima en Madrid'.")
        elif "precio de" in consulta:
            ticker = consulta.replace("precio de ", "").strip().upper()
            if ticker:
                print(obtener_precio_accion(ticker))
            else:
                print("Por favor, especifica un símbolo de acción. Ejemplo: 'precio de AAPL'.")
        elif consulta in ["salir", "adios", "adiós"]:
            print("¡Hasta luego!")
            break
        else:
            print("Lo siento, no entiendo tu consulta. Prueba con algo como 'clima en París' o 'precio de AAPL'.")

if __name__ == "__main__":
    main()
