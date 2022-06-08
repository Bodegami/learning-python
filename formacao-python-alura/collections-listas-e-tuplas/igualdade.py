
class ContaSalario:

    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def deposita(self, valor):
        self._saldo += valor

    def __str__(self):
        return f"[>>Codigo {self._codigo} - Saldo {self._saldo}<<]"

    # Quando trabalhos com listas e precisamos utilizar operacoes de igualdade, é importande fazer a implementacao
    # atraves do metodo built-in __eq__()
    # dessa forma sobrescrevemos o metodo de igualdade para o nosso quesito de igualdade (codigo, saldo)

    # alem dos quesitos que utilizamos para definir a igualdade,
    # é importante validar se o parametro recebido é do mesmo tipo.
    # Da forma que implementamos abaixo, ele valida se é do tipo ou filho de ContaSalario,
    # caso verdadeiro ele verifica a igualdade
    def __eq__(self, other):
        #if type(other) != ContaSalario:
        if not isinstance(other, ContaSalario):
            return False

        return self._codigo == other._codigo and self._saldo == other._saldo


class ContaMultiploSalario(ContaSalario):
    pass


conta1 = ContaSalario(37)
print(conta1)
conta2 = ContaSalario(37)
print(conta2)

# Por padrao, a implementacao de igualdade só retorna verdadeiro caso
# as referências ou variaveis apontem para o mesmo objeto
print(conta1 == conta2)
contas = [conta1]
print(conta2 in contas)

# Os operadores de diferente (!=) e in também utilizam o __eq__ para verificar a igualdade
print(conta1 != conta2)
print(conta2 in [conta1])

conta3 = ContaMultiploSalario(37)
print(conta1 == conta3)

# Podemos verificar o tipo e tambem se é um instancia do tipo
# Assim como os outros metodos, o isInstance também utiliza o __eq__()

print(type(conta3))
print(isinstance(conta3, ContaSalario))



