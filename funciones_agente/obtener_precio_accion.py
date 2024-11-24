import warnings
import sys
import os
import requests

# Redirigir la salida estándar temporalmente
class SuppressPrint:
    def __enter__(self):
        self._original_stdout = sys.stdout
        sys.stdout = open(os.devnull, 'w')

    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stdout.close()
        sys.stdout = self._original_stdout

# Suprimir el mensaje al importar yahoo_fin
with SuppressPrint():
    import yahoo_fin.stock_info as si

# Suprimir las advertencias de FutureWarning
warnings.filterwarnings("ignore", category=FutureWarning)

# Lista de acciones disponibles para consulta
acciones_disponibles = ["TSLA", "AAPL", "AMZN", "GOOG", "MSFT", "NFLX"]

def obtener_precio_accion(ticker):
    """
    Obtiene el precio de una acción en USD y lo convierte a MXN usando una API de tasas de cambio.
    """
    try:
        # Obtener el precio en USD desde Yahoo Finance
        precio_usd = si.get_live_price(ticker)
        
        # Obtener la tasa de cambio de USD a MXN
        url = "https://api.exchangerate-api.com/v4/latest/USD"
        response = requests.get(url)
        response.raise_for_status()  # Asegurarse de que la solicitud fue exitosa
        data = response.json()
        tasa_cambio = data['rates']['MXN']
        
        # Convertir el precio a MXN y redondearlo
        precio_mxn = round(precio_usd * tasa_cambio, 2)
        
        # Devolver el precio en MXN como string con "MXN" agregado
        return f"{precio_mxn} MXN"
    except requests.RequestException as e:
        print(f"Error al obtener la tasa de cambio: {e}")
    except Exception as e:
        print(f"No se pudo obtener el precio de la acción {ticker}. Detalles: {e}")
    return None

def main():
    """
    Función principal del chatbot para interactuar con el usuario.
    """
    print("¡Bienvenido al chatbot! ¿En qué puedo ayudarte? (Escribe 'salir' para terminar)")
    print(f"Acciones disponibles para consultar: {', '.join(acciones_disponibles)}")
    
    while True:
        # Leer la consulta del usuario
        consulta = input(">> ").lower()
        
        if consulta == "salir":
            print("¡Hasta luego!")
            break
        
        elif "precio de" in consulta:
            # Extraer el símbolo de la acción desde la consulta
            ticker = consulta.replace("precio de ", "").strip().upper()
            
            if ticker in acciones_disponibles:
                # Obtener y mostrar el precio de la acción
                precio_mxn = obtener_precio_accion(ticker)
                if precio_mxn is not None:
                    print(f"El precio actual de {ticker} es {precio_mxn}.")
                else:
                    print(f"No se pudo obtener el precio de {ticker}.")
            else:
                print(f"La acción {ticker} no está disponible en nuestra lista.")
        else:
            print("No entiendo tu consulta. Por favor, intenta de nuevo.")

if __name__ == "__main__":
    main()
