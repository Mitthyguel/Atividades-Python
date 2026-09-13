string = input("Digite uma String:")
if len(string) > 10:
    string = string[:10] + "...."
    print(string)
else:
    print(string)