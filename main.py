import sys

def get_hello_str(lang):
    if lang == "ru":
        return "Добрый день"
    elif lang == "fr":
        return "Bonjour"
    else:
        return "Hello"


def get_person_name(args):
    if len(args) > 1:
        return args[1]
    else:
        return "world"

person = get_person_name(sys.argv)
lang = sys.argv[2] if (len(sys.argv) > 2) else "en"

hello_str = get_hello_str(lang) + ","

print(hello_str, person)
