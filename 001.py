print("Unicamp" , end = "")
print("MC102!")


# Sem 0 caractere de controle de quebra de linha 
print ("MC102" , "Unicamp" , "2022" , sep = " - " , end = " ! ")
print("Novo Texto !")

# Com o caractere de controle de quebra de linha (\n) no fim:

print("MC102" , "Unicamp" , "2022" , sep = "  - " , end = "!\n")
print("Novo Texto  !")

# Exemplo

print("Hello world") # Exemplo de função print

# Parâmetros importantes da função print
# sep: Texto usado na separação dos argumentos recebidos.
# end: Texto impresso no final da execução.
print("MC102" , "Unicamp" , sep = " - " , end = "!\n")
# MC102 - unicamp

print("jose - 99999999 - MC102 -2022")

# Exemplo 

print("josé" , "999999999" , "MC102" , "2022" , sep= " - ")

# Exemplos de tipos

print(type(10))

print(type(10.0))


print(type(True), type(False), type("True"), type("False"))

# <class 'bool'> <class 'boll'> <class 'str'> <class 'str'>


# variáveis

pi = 3.1416
print(pi)

# 3.1416

# 3 3 3

a = b = c = 3
print(a , b, c)

a, b, c = 1, 2, 3

print(a, b, c)

# 1 2 3

# Exemplo

c1 = 0
C1 = "1"
print(c1, type(c1), C1, type(C1))

# 0 <class 'int'> 1 <class 'str'>

