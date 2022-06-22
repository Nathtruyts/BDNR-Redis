import conectarBD as conectarDB

def inserir(nome, valor):
    myRedis = conectarDB.conectar()
    key = 'Nome:{nome}'
    value = {'valor: {valor}'}
    myRedis.set(key, '{value}')
    print('### Adicionar cupom ###')
    print('Cupom Adicionado!')
    print(myRedis.get(key))
    print('\n')

def acharCupom(nome):
    myRedis = conectarDB.conectar()
    key = 'CupomNome:{nome}'
    cupons = myRedis.get(key)
    print('### Achei o seu cupom ###')
    print(cupons)
    print('\n')

def deletarCupom(nome):
    myRedis = conectarDB.conectar()
    key = 'CupomNome:{nome}'
    myRedis.delete(key)
    print('### Deletar um cupom ###')
    print('Cupom deletado!')
    print('\n')


