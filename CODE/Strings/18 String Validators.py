if __name__ == '__main__':
    s = input()
    print(any(string.isalnum() for string in s))#si toso los caracteres son alfanumericos
    print(any(string.isalpha() for string in s))#si todos los caracteres son alfabeticos
    print(any(string.isdigit() for string in s))#si todos los caracteres son numeros
    print(any(string.islower() for string in s)) #si todas las letras estan en minusculas
    print(any(string.isupper() for string in s))#si todas las letras estan en mayusculas
