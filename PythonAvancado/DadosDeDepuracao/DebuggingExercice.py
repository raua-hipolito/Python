import random


DIGITS_MAP = {
    0: "zero",
    1: "um",
    2: "dois",
    3: "três",
    4: "quatro",
    5: "cinco",
    6: "seis",
    7: "sete",
    8: "oito",
    9: "nove",
}


def generate_int_description(integer):
    """Transforma dígitos de um número em texto PT-BR"""
    # nun_digits = []
    # digits = list(str(integer))
    # for digit in digits:
    #     nun_digits.append(int(digit))
    nun_digits = [int(digit) for digit in str(integer)]
    print(nun_digits)
    description = f"{DIGITS_MAP.get(nun_digits[0])}"
    for digit in nun_digits[1:]:
        description += f" {DIGITS_MAP.get(digit)}"

    return description


def main():
    integer = random.randint(10000, 99999)

    description = generate_int_description(integer)

    print(f"Descrição do número {integer}: '{description}'")


if __name__ == "__main__":
    main()
