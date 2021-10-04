"""
En una empresa de seguridad, se han asignado 2 contraseñas para el
ingreso: x5y4 y a1b2. Toda persona que ingrese debe registrar una
de las contraseñas.
Se necesita un programa que valide si la contraseña es correcta o no.
El usuario tendrá 3 posibilidades de registrarse y el programa debe
informarle si puede ingresar o no.
El programa debe funcionar para varios usuarios. Todos los datos
ingresados por el usuario deben ser validados.

TODO: add testcases and more ways to resolve it.
"""

PASSWORD = ("x5y4", "a1b2")
USUARIOS = 3


def _validar_password(password: str) -> bool:
    if password in PASSWORD:
        return True
    return False


def validar_entrada(msg, intentos: int = 3) -> bool:
    while intentos >= 1:
        print(f"Restan {intentos} intentos")
        password = input(msg)
        intentos -= 1
        if _validar_password(password):
            return True
        else:
            print("Contraseña incorrecta!")
            continue
    return False


def ingresar(usuario: int) -> str:
    valido = validar_entrada("Ingresar contraseña: ")
    print(f"Usuario: {usuario}")
    if valido:
        return "Puede ingresar!"
    else:
        return "No puede ingresar!"


def main() -> None:
    for i in range(1, USUARIOS+1):
        print(ingresar(i))


if __name__ == "__main__":
    main()