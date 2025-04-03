"""
CONVERSOR DE BASES NUMÉRICAS

Este programa convierte números entre diferentes bases (2, 8, 10, 16) mostrando el proceso paso a paso.
Incluye representación de bases con subíndices y soporte para dígitos hexadecimales (A-F).
"""

# Diccionario para convertir dígitos a subíndices
SUBSCRIPT = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")  # Para bases numéricas (ej: 3F₁₆)
SUPERSCRIPT = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")  # Para exponentes (ej: 16²)

# Mapeo de dígitos hexadecimales (valores y letras)
HEX_DIGITS = {
    10: "A",
    11: "B",
    12: "C",
    13: "D",
    14: "E",
    15: "F",
    "A": 10,
    "B": 11,
    "C": 12,
    "D": 13,
    "E": 14,
    "F": 15,
}


def convert_from_base_10_to_base(n, base):
    """
    Convierte un número de base 10 a otra base (2, 8, 16).

    Args:
        n (int): Número en base 10 a convertir
        base (int): Base objetivo (2, 8 o 16)

    Returns:
        list: Lista con los dígitos del número convertido (en orden correcto)

    Proceso:
        1. Divide sucesivamente el número por la base objetivo
        2. Almacena los restos de cada división
        3. Para base 16, convierte restos >9 a letras A-F
    """
    list_out = []

    # Caso base: número menor que la base objetivo
    if n < base:
        return [str(n)] if n < 10 else [HEX_DIGITS[n]]
    else:
        remainder = n  # Inicializa el resto
        max_width = len(str(n))  # Para alinear visualmente los cálculos

        while n // base > 0:
            # Realiza división y muestra el proceso
            print(
                f"{n:>{max_width}} // {base} = {(n := n // base):>{max_width}} => Resto: {(remainder := remainder % base):>2}"
            )

            # Almacena el resto (convertido a letra si es hexadecimal)
            if (base == 16 and remainder < 10) or base != 16:
                list_out.insert(0, remainder)
            elif base == 16 and remainder >= 10:
                list_out.insert(0, HEX_DIGITS[remainder])

            remainder = n  # Actualiza el resto para la siguiente división

            # Maneja el último cociente
            if n < base and (base != 16 or (base == 16 and n < 10)):
                list_out.insert(0, n)
            elif (n < base and base == 16) and n >= 10:
                list_out.insert(0, HEX_DIGITS[n])

        return list_out


def convert_to_base_10(n, base):
    """
    Convierte un número de base 2, 8 o 16 a base 10.

    Args:
        n (str): Número como cadena (ej: "3FF")
        base (int): Base original (2, 8 o 16)

    Returns:
        tuple: (lista de pasos como cadenas, resultado numérico)

    Proceso:
        1. Convierte cada dígito a su valor decimal
        2. Aplica la fórmula: d0*base^0 + d1*base^1 + ...
        3. Genera representación visual de cada término
    """
    digits = []

    # Convierte cada dígito a su valor numérico
    for dig in n.upper():
        if dig in HEX_DIGITS:
            digits.append(HEX_DIGITS[dig])
        else:
            digits.append(int(dig))

    steps = []
    result = 0

    # Calcula desde el dígito menos significativo
    for i, dig in enumerate(reversed(digits)):
        result += dig * base**i
        # Formato: dígito·base^posición (ej: 15·16²)
        steps.insert(0, f"{dig}·{base}{str(i).translate(SUPERSCRIPT)}")

    return (steps, result)


# Programa principal
def main():
    """Función principal que maneja la interfaz de usuario."""
    print("CONVERSOR DE BASES")

    while True:
        print("\n" + "=" * 30)
        number = input("Ingrese el número que desea convetir (-1 para salir): ")

        if number == "-1":
            print("Saliendo del programa...")
            break

        base_in = int(input("Ingrese la base del número que desea convertir: "))
        base_out = int(input("Ingrese la base a la que desea convetir: "))
        list_out_power = []

        print()  # Salto de línea

        # Validación de bases soportadas
        if base_in not in [2, 8, 10, 16] or base_out not in [2, 8, 10, 16]:
            print("Error: Bases soportadas son 2, 8, 10 y 16")

        elif base_in == base_out:
            print("El número ya está en la base deseada.")

        # Conversión desde base 10 a otra base
        elif base_in == 10:
            num = int(number)
            result_function = convert_from_base_10_to_base(num, base_out)

            result = "".join(map(str, result_function))

            # Convertir la base a subíndice
            base_sub_in = str(base_in).translate(SUBSCRIPT)
            base_sub_out = str(base_out).translate(SUBSCRIPT)

            # Formateo con subíndices
            print(f"\nResultado: {number}{base_sub_in} => {result}{base_sub_out}")

        # Conversión a base 10 desde otras bases
        elif base_in in [2, 8, 16]:
            list_out_power, result_function = convert_to_base_10(number, base_in)

            # Convertir la base a subíndice
            base_sub_in = str(base_in).translate(SUBSCRIPT)
            base_sub_out_10 = "10".translate(SUBSCRIPT)

            print(f"{' + '.join(list_out_power)} = {result_function}")

            # Si la base objetivo no es 10, hace segunda conversión
            if base_out != 10:
                print(
                    f"\nResultado parcial: {number.upper()}{base_sub_in} => {result_function}{base_sub_out_10}\n"
                )

                result_digits = convert_from_base_10_to_base(result_function, base_out)
                result_2 = "".join(map(str, result_digits))

                # Convertir la base a subíndice
                base_sub_out = str(base_out).translate(SUBSCRIPT)
                print(
                    f"\nResultado final: {number.upper()}{base_sub_in} => {result_2}{base_sub_out}"
                )
            else:
                print(
                    f"\nResultado: {number.upper()}{base_sub_in} => {result_function}{base_sub_out_10}"
                )
        else:
            print("Base incorrecta")


# Para ejecutar directamente el script
if __name__ == "__main__":
    main()
# Fin del programa
