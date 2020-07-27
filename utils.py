from models import Pessoas


#insere dados na tabela pessoa
def insere_pessoas():
    pessoa = Pessoas(nome='selma', idade=47)
    print(pessoa)
    Pessoas.save(pessoa)


#realiza consulta na tabela Pessoas
def consulta_pessoas():
    pessoa = Pessoas.query.all()
    for i in pessoa:
        print(i.nome, i.idade)


#altera dados na tabela Pessoa
def alterar_pessoa():
    pessoa = Pessoas.query.filter_by(nome='rafael').first()
    pessoa.nome = 'Felipe'
    Pessoas.save(pessoa)


#deleta dados na tablea Pessoas
def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Felipe').first()
    Pessoas.delete(pessoa)


if __name__ == '__main__':
    #insere_pessoas()
    #alterar_pessoa()
    exclui_pessoa()
    consulta_pessoas()
