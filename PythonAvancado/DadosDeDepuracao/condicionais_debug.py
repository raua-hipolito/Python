# vamos utilizar como exemplo uma implementação prática do algoritmo de
# ordenação conhecido como Insertion Sort. Esse algoritmo percorre
# o array da esquerda para a direita e, a cada iteração, insere o
# elemento atual na posição correta do array.


def insertion_sort(array):
    for i in range(1, len(array)):
        current_value = array[i]
        position = i

        while position > 0 and array[position - 1] > current_value:
            array[position] = array[position - 1]
            position -= 1

        array[position] = current_value

    return array


def main():
    array = [23, 423, 1, 54, 8, 980, 45, 768, 34, 55, 88, 99, 100, 234, 567]

    sorted_array = insertion_sort(array)

    print(f"Array ordenado: {sorted_array}")


if __name__ == "__main__":
    main()

# exercício: 1) descubra o valor de current_value na linha while
# quando a soma de i e position for igual a 6 pela primeira vez
