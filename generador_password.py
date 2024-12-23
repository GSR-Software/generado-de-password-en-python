import random
import string


def generate_password(length=16):
    """Genera una contraseña segura."""
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choices(characters, k=length))
    return password


def save_password(site, password):
    """Guarda la contraseña en un archivo."""
    with open("passwords.txt", "a") as file:
        file.write(f"{site}: {password}\n")
    print(f"Contraseña guardada para {site}.")


def retrieve_password(site):
    """Recupera la contraseña de un archivo."""
    try:
        with open("passwords.txt", "r") as file:
            for line in file:
                saved_site, saved_password = line.strip().split(": ", 1)
                if saved_site == site:
                    return saved_password
        return None
    except FileNotFoundError:
        print("El archivo de contraseñas no existe.")
        return None


def main():
    print("Bienvenido al gestor de contraseñas.")
    while True:
        print("\nOpciones:")
        print("1. Generar una nueva contraseña")
        print("2. Recuperar una contraseña")
        print("3. Salir")

        choice = input("Selecciona una opción: ")
        if choice == "1":
            site = input("Ingresa el nombre del sitio: ")
            length = int(input("Longitud de la contraseña (16 por defecto): ") or 16)
            password = generate_password(length)
            print(f"Tu nueva contraseña es: {password}")
            save_password(site, password)
        elif choice == "2":
            site = input("Ingresa el nombre del sitio: ")
            password = retrieve_password(site)
            if password:
                print(f"La contraseña para {site} es: {password}")
            else:
                print(f"No se encontró ninguna contraseña para {site}.")
        elif choice == "3":
            print("Saliendo del gestor de contraseñas. Adiós.")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")


if __name__ == "__main__":
    main()
