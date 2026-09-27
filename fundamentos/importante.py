"""
"Todos os dados em um programa Python são representados por objetos ou pela relação entre objetos."
 Tudo em Python é um objeto.
 Alguns tipos de objetos em python:
 int (Números inteiros)
 str (string, texto)
 float (Números com pontos)
 bool (True or False)

 Objetos do tipo sequência: texto, listas e tuplas.
 Objetos do tipo set (conjunto).
 Objetos do tipo mapping (dicionário).
 Objetos do tipo array NumPy.

 Objetos do tipo 'Sequência':
 Os objetos do tipo sequência são estruturas de dados capazes de armazenar mais de um valor.
 Essas estruturas de dados representam sequências finitas indexadas por números não negativos. 
 Ex: 
"""
# x in s = True caso um item de s seja igual a x, senão False;
frase = 'Bommm Dia'
print('B' in frase)
# s + t = Concatenação (junta) de s e t;
print('s' + 't')
# n * s = n * Adiciona s a si mesmo n vezes;
print(4 * 's')
# s[i] = Acessa o valor guardado na posição i da sequência / o primeiro valor = 0;
print(frase[0])
# s[i:j] = Acessa os valores da posição i até j / O valor j não está incluído;
print(frase[0:4])
# s[i:j:k] = Acessa os valores da posição i até j, com passo k = O valor j não está incluído;
print(frase[0:8:2])
# len(s) = Comprimento de s / Função built-in usada para saber o tamanho da sequência;
print(len(frase))
# min(s) = Menor valor de s / Função built-in usada para saber o menor valor da sequência;
print(min(frase))
# max(s) = Maior valor de s / Função built-in usada para saber o maior valor da sequência;
print(max(frase))
# s.count(x) = Número total de ocorrência de x em s / Conta quantas vezes x foi encontrado;
print(frase.count('m'))
# lower() = deixar minuscula;
print(frase.lower())
# upper() = deixar maiuscula;
print(frase.upper())
# replace()  = substituir um caractere por outro;
print(frase.replace('m', 'n'))
# split() = usada para "cortar" um texto e transformá-lo em uma lista;
palavras = frase.split()
print(f"palavras = {palavras}")
print('também: ')
palavras = frase.split()
print(f"palavras = {palavras}")
print(f"Tamanho de palavras = {len(palavras)}")
print('exemplificando: ')
texto = """Operadores de String
Python oferece operadores para processar texto (ou seja, valores de string).
Assim como os números, as strings podem ser comparadas usando operadores de comparação:
==, !=, <, > e assim por diante.
O operador ==, por exemplo, retorna True se as strings nos dois lados do operador 
tiverem o mesmo valor (Perkovic, p. 23, 2016).
"""
print(f"Tamanho do texto = {len(texto)}")
texto = texto.lower()
texto = texto.replace(",", "").replace(".", "").replace("(", "").replace(")", "").replace("\n", " ")
lista_palavras = texto.split()
print(f"Tamanho da lista de palavras = {len(lista_palavras)}")

total = lista_palavras.count("string") + lista_palavras.count("strings")

print(f"Quantidade de vezes que string ou strings aparecem = {total}")

print(' ')
print('Ex:')
#ex:
texto = "Aprendendo Python na disciplina de linguagem de programação."

print(f"Tamanho do texto = {len(texto)}")
print(f"Python in texto = {'Python' in texto}")
print(f"Quantidade de y no texto = {texto.count('y')}")
print(f"As 5 primeiras letras são: {texto[0:6]}")
print(' ')
print('Listas:')
"""
Listas
Lista é uma estrutura de dados do tipo sequencial
que possui como principal característica ser mutável.
Ou seja, novos valores podem ser adicionados ou removidos da sequência.
Em Python, as listas podem ser construídas de várias maneiras:
1. Usando um par de colchetes para denotar uma lista vazia: lista1 = []
2. Usando um par de colchetes e elementos separados por vírgulas: lista2 = ['a', 'b', 'c']
3. Usando uma "list comprehension": [x for x in iterable]
4. Usando o construtor de tipo: lista()
# index, que retorna a posição de um valor na sequência.
"""
vogais = ['a', 'e', 'i' , 'o' , 'u']

for vogal in vogais:
    print(f'Posição = {vogais.index(vogal)}, valor = {vogal}')
    
print(' ')

vogais = []
print(f"Tipo do objeto vogais = {type(vogais)}") # type para ver o tipo da função

vogais.append('a')
vogais.append('e')
vogais.append('i') #adiciona valor = .append()
vogais.append('o')
vogais.append('u')
# enumerate()que é usada para percorrer um objeto iterável retornando a posição e o valor.
for p, x in enumerate(vogais):
    print(f"Posição = {p}, valor = {x}") #p = contador manual, p = posição x = valor

#Veja, na entrada 6 (In [6]), que repetimos o exemplo com algumas alterações, 
#a primeira das quais foi criar uma lista vazia na linha 3. Observe que, mesmo estando vazia, 
#ao imprimirmos o tipo do objeto, o resultado é "class list",
#pois o colchete é a sintaxe para a construção de listas. 
#Outra novidade foi usar a função append(), que adiciona um novo valor ao final da lista.
#Na sintaxe usamos vogais.append(valor), notação que significa que 
#a função append() é do objeto lista. Também substituímos o contador manual ("p") pela 
#função enumerate(), que é usada para percorrer um objeto iterável retornando a posição e o valor. 
#Por isso, na estrutura de repetição precisamos usar as variáves p e x. A primeira guarda a posição
# e a segunda guarda o valor.
#Usamos o nome x propositalmente para que você perceba que o nome da variável é de livre escolha.
print(' ')
frutas = ['maçã', 'banana', 'uva', 'mamão', 'maçã']
notas = [8.7, 5.2, 10, 3.5]

print('maçã' in frutas) # True
print('abacate' in frutas) # False
print("abacate" not in frutas) # True
print(min(frutas)) # banana
print(max(notas)) # 10
print(frutas.count("maça")) # 2
print(frutas + notas) # Concatenar as duas listas
print(2 * frutas) # Multiplicar a lista 'frutas' 
print('ex2')
lista = ['Python', 30.61, "Java", 51 , ['a', 'b', 20], "maça"]

print(f"Tamanho da lista = {len(lista)}")

for i, item in enumerate(lista):
    print(f"Posição = {i},\t valor = {item} -----------------> tipo individual = {type(item)}")

print("\nExemplos de slices:\n")

print("lista[1] = ", lista[1])
print("lista[0:2] = ", lista[0:2])
print("lista[:2] = ", lista[:2])
print("lista[3:5] = ", lista[3:5])
print("lista[3:6] = ", lista[3:6])
print("lista[3:] = ", lista[3:])
print("lista[-2] = ", lista[-2])
print("lista[-1] = ", lista[-1])
print("lista[4][1] = ", lista[4][1])

print(' ')
"""List comprehension (Compreensões de lista)
A list comprehension, também chamada de listcomp,
é uma forma pythônica de criar uma lista com base em um objeto iterável."""
linguagens = ["Python", "Java", "JavaScript", "C", "C#", "C++", "Swift", "Go", "Kotlin"]
#linguagens = '''Python Java JavaScript C C# C++ Swift Go Kotlin'''.split()
# Essa sintaxe produz o mesmo resultado que a linha 1

print("Antes da listcomp = ", linguagens)

linguagens = [item.lower() for item in linguagens]
# variável chamada "item" que representará cada valor da lista original.
print("\nDepois da listcomp = ", linguagens)

#Agora vamos usar a listcomp para construir uma lista que contém somente as
#linguagens que possuem "Java" no texto. Veja o código a seguir.
print(' ')
linguagens = '''Python Java JavaScript C C# C++ Swift Go Kotlin'''.split()

linguagens = '''Python Java JavaScript C C# C++ Swift Go Kotlin'''.split()
linguagens_java = []

for item in linguagens:
    if "Java" in item:
        linguagens_java.append(item)

print(linguagens_java)
""" 
Funções map() e filter()
duas funções built-in
A função map() é utilizada para aplicar uma determinada função em cada item de um objeto iterável.
a função map() exige que sejam passados dois parâmetros: a função e o objeto iterável.
Observe os dois exemplos a seguir.

"""
numeros  = list(range(0, 21))

numeros_pares = list(filter(lambda x: x % 2 == 0, numeros))

print(numeros_pares)
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
"""Na entrada 14 (In [14]), a função range()
cria um objeto numérico iterável.
Então usamos o construtor list() para transformá-lo em uma lista com números,
que variam de 0 a 20. Lembre-se de que o limite superior do argumento da função range() 
não é incluído. Na linha 3, criamos uma nova lista com a função filter, que, 
com a utilização da expressão lambda,
 retorna somente os valores pares.
 função add(valor)
 podemos remover com remove(valor)"""