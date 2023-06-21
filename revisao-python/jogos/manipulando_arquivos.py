
# Passamos 'w' para modo de escrita e 'r' para modo de leitura
# Podemos usar também o 'a' de adicionar
arquivo = open("palavras.txt", "w")
print(type(arquivo))

arquivo.write("banana\n")
arquivo.write("melancia\n")

# Lembrar sempre de feixar o arquivo
arquivo.close()

arquivo = open("palavras.txt", "a")

arquivo.write("morango\n")

arquivo.write("maça\n")
arquivo.close()


