import sys

def convertir_moneda():
    if len(sys.argv) != 5:
        print("Uso: python conversiones.py <sol_peruano_tasa> <peso_argentino_tasa> <dolar_americano_tasa> <valor_clp>")
        sys.exit(1)

    try:
        sol_tasa = float(sys.argv[1]) # Tasa para Sol peruano
        peso_arg_tasa = float(sys.argv[2]) # Tasa para Peso Argentino
        dolar_tasa = float(sys.argv[3]) # Tasa para Dólar Americano
        valor_clp = int(sys.argv[4]) # Valor en peso chileno a convertir

        soles = valor_clp * sol_tasa
        pesos_argentinos = valor_clp * peso_arg_tasa
        dolares = valor_clp * dolar_tasa

        print(f"Los {valor_clp} pesos equivalen a:")
        print(f"{soles:.1f} Soles")
        print(f"{pesos_argentinos:.1f} Pesos Argentinos")
        print(f"{dolares:.1f} Dólares")

    except ValueError:
        print("Error: Asegúrate de que todas las tasas y el valor sean números válidos.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

if __name__ == "__main__":
    convertir_moneda()