import sys

person = sys.argv[1] if (len(sys.argv) > 1) else "world"
lang = sys.argv[2] if (len(sys.argv) > 2) else "en"
hello_str = "hello,"

print(hello_str, person)
