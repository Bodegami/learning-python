
# Passamos 'w' para modo de escrita e 'r' para modo de leitura
# Podemos usar também o 'a' de adicionar

#Criando um arquivo e adicionando elementos
arquivo = open("palavras.txt", "w")
print(type(arquivo))

arquivo.write("banana\n")
arquivo.write("melancia\n")

# Lembrar sempre de feixar o arquivo
arquivo.close()

#Abrindo um arquivo e adicionando elementos
arquivo = open("palavras.txt", "a")

arquivo.write("morango\n")

arquivo.write("maça\n")
arquivo.close()

#Lendo um arquivo
arquivo = open("palavras.txt", "r")

#Só é possivel ler o arquivo uma vez
print(arquivo.read())
print(arquivo.read())

arquivo.close()

#Para ler novamente, é necessário abrir o arquivo mais uma vez
arquivo = open("palavras.txt", "r")

#Um arquivo pode ser considerado uma sequencia de linhas
#Outro ponto é que cada linha do arquivo é composta pelo conteúdo + \n
#Isso pode gerar um comportamento inesperado quando usado com o print que por padrao coloca end="\"
for linha in arquivo:
    print(linha)

arquivo.close()


arquivo = open("palavras.txt", "r")

#Mas podemos resolver esse problema, utilizando a funcao built-in do '.strip()' do python
#A funcao '.strip()' remove espacos em branco no começo e no final da String e tb remove elementos como '\n'
for linha in arquivo:
    print(linha.strip())

arquivo.close()

# Usando a sintaxe do 'with open' o python garante que caso ocorra algum erro ao tentar abrir o arquivo, esse
# erro nao vai quebrar a aplicacao. Alem disso o python cuida de fechar o arquivo e nao precisamos mais chamar
# o arquivo.close().
with open("palavras.txt", "r") as arquivo:
    for linha in arquivo:
        print(linha.strip().upper())
