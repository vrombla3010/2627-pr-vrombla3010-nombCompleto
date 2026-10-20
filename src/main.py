"""Programa para formatear un nombre completo."""


def formatear_nombre(nombre: str, apellido1: str, apellido2: str) -> str:
    """Devuelve el nombre y los dos apellidos con el formato adecuado.

    :param nombre: Nombre de la persona, que puede ser compuesto.
    :param apellido1: Primer apellido de la persona.
    :param apellido2: Segundo apellido de la persona.
    :return: Nombre completo con cada palabra capitalizada.
    """

    nombre_formateado: str = nombre.strip().title()
    apellido1_formateado: str = apellido1.strip().title()
    apellido2_formateado: str = apellido2.strip().title()

    nombre_completo: str = (
        f"{nombre_formateado} "
        f"{apellido1_formateado} "
        f"{apellido2_formateado}"
    )

    return nombre_completo


def main() -> None:
    """Solicita los datos y muestra el nombre completo formateado."""

    nombre: str = input("Introduce tu nombre: ")
    apellido1: str = input("Introduce tu primer apellido: ")
    apellido2: str = input("Introduce tu segundo apellido: ")

    nombre_completo: str = formatear_nombre(nombre, apellido1, apellido2)
    print(nombre_completo)


if __name__ == "__main__":
    main()
