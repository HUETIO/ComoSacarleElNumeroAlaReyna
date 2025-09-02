import sys

# Diccionario de emojis -> código Python
mapping = {
    "👋": '"Hola"',   
    "👋": '"Hola"',   
    "🐍": '"Este"',     
    "🌎": '"Mundo"',  
    "➕": "hacer / haces / Hacemos",         
    "😀": '"Hagamos la prueba"',      
    "😄": '"Chica Linda / Chico Lindo"',      
    "😁": '"Que quieres hacer hoy"',      
    "😆": '"Me gusta tu propuesta"',      
    "😅": '"Esto no lo pueden Saber"',      
    "🤣": '"Y no te rias que es enserio"',      
    "😂": '"Eso es gracioso"',      
    "🙃": '"Ahora mismo estoy durmiendo"',      
    "😉": '"Cual es tu"',      
    "🙈": '"Numero de Telefono"',      
    "🥺": '"Por favor"',      
    "👅": '"Lengua / Oral / Sexo"',      
    "👀": '"¿Como Estas?"',      
    "😏": '"Atrevida / Atrevido"',      
    "🙂‍": '"Claro lo verificare me hace sentir raro / rara"',      
    "😌": '"Claro que si solo para ti"',      
    "🤐": '"Silencio no lo pueden saber / a solas"',      
    }

def translate(emoji_code: str) -> str:
    """Convierte la cadena de emojis a código Python."""
    tokens = emoji_code.split()
    translated = " ".join(mapping.get(tok, tok) for tok in tokens)
    return translated

def run_file(filename: str):
    """Lee un archivo .emoji y ejecuta cada línea."""
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            py_code = translate(line)
            print(f"[DEBUG] {line} -> {py_code}")
            eval(py_code)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python emoji_interpreter.py programa.emoji")
    else:
        run_file(sys.argv[1])
