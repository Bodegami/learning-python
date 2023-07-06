
class ContaCorrente:

    def __init__(self, codigo):
        self.codigo = codigo
        self.saldo = 0

    def deposita(self, valor):
        self.saldo += valor

    def __str__(self):
        return f"[>>codigo {self.codigo} Saldo {self.saldo}<<]"


guilherme = ('Guilherme', 37, 1981)
daniela = ('Daniela', 31, 1987)

usuarios = [guilherme, daniela] # Lista -> mutavel

print(usuarios)

[print(usuario) for usuario in usuarios]

usuarios.append(('Paulo', 39, 1979))

print(usuarios)

conta_gui = ContaCorrente(15)
conta_gui.deposita(500)
conta_dani = ContaCorrente(234876)
conta_dani.deposita(1000)


contas = (conta_gui, conta_dani) # Tupla -> imutavel
[print(conta) for conta in contas]
contas[0].deposita(500) # A Tupla é imutavel, mas os objetos que a compoem não, o que permite alterar os atributos
[print(conta) for conta in contas]
