try:
    f = open('FileNotFoundError.py')
    print(f.read())
except FileNotFoundError:
    print("Sorry file doesnt exist")