import sys
import string 

def count_words_and_chars(filepath):
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            texto = file.read()

        caracteres_distintos = len(set(texto)) 

        texto_lower = texto.lower()

        translator = str.maketrans('', '', string.punctuation)
        texto_sin_puntuacion = texto_lower.translate(translator)

        palabras = texto_sin_puntuacion.split() 
        
        palabras_distintas = len(set(palabras))

        print(f"El número de caracteres distintos es: {caracteres_distintos}")
        print(f"El número de palabras distintas es: {palabras_distintas}")

    except FileNotFoundError:
        print(f"Error: El archivo '{filepath}' no fue encontrado.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python word_count.py <nombre_del_archivo_texto>")
        sys.exit(1)
    
    file_name = sys.argv[1] 
    count_words_and_chars(file_name)