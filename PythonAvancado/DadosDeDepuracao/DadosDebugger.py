from math import factorial


def map_factorial(numbers):
    result = []

    for number in numbers:
        result.append(factorial(number))

    return result


def main():
    input_list = [1, 2, 3, 4, 5,]
    return map_factorial(input_list)


if __name__ == "__main__":
    main()


# o breakpoint é uma função que permite que o programa
# pare em um determinado ponto

# VARIABLES (variáveis)
# CALL STACK (pilha de chamadas)
# WATCH (inspeção)
# BREAKPOINTS (pontos de parada)
