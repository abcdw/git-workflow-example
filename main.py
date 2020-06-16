import sys

lang = sys.argv[2] if (len(sys.argv) > 2) else "en"
hello_str = "hello,"

def get_person_name(args):
    if len(args) > 1:
        return args[1]
    else:
        return "world"

person = get_person_name(sys.argv)
print(hello_str, person)
