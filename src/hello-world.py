import sys

# if we pass an argument we print it, if not we just print hello world
if len(sys.argv) > 1:
    print(f"hello-world {sys.argv[1]}")
else:
    print(f"hello-world")

