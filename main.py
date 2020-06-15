import sys

person = sys.argv[1] if (len(sys.argv) > 1) else "world"
def get_hello_str(lang):
    if lang == "ru":
        return "Привет"
    elif lang == "fr":
        return "Bonjour"
    else:
        return "Hello"


lang = sys.argv[2] if (len(sys.argv) > 2) else "en"

hello_str = get_hello_str(lang) + ","

print(hello_str, person)
