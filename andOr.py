# valores de tipos diferentes não realizam (false)
print(10 == "10")
# forma correta
print(10 == int("10"))
print(10 == 10)

# Exemplo 2
a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)  # True
# ------------------------------------------------------------------------------------------------------------------------
# Isso ocorre porque as duas strings são diferentes, e o operador "!=" retorna
# true quando os operandos não são iguais.
print("python" != "java")


# ------------------------------------------------------------------------------------------------------------------------

# operdores && e // são representados por "and" e "or" respectivamente
# no And os dois valores precisam ser verdadeiros para retornar true
# Exemplo 1
idade = 17
print(idade < 18 and idade > 16)
# exemplo 2
meuSalario = 1000
salarioMinimo = 998
print(meuSalario > 2000 and salarioMinimo < 800)


# ------------------------------------------------------------------------------------------------------------------------
# no Or se um dos valores for verdadeiro, o resultado será verdadeiro
# Exemplo 1
idadeCriancas = 8
idadeIdoso = 65
print("Regra:", idadeCriancas > 9 or idadeIdoso >= 65)
# Exemplo 2 para retornar false
salarioMinimo = 998
meuSalario = 1000
print("Regra:", meuSalario > 2000 or salarioMinimo < 800)
