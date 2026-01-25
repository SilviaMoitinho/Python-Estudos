from lib.interface import *

def arquivoExiste(nome):
    try:
        a = open(nome, 'rt') #tentar abrir o aqruivo modo read and text
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
    

def criarArquivo(nome):
    try:
        a = open(nome, 'wt+') # Abra o arquivo e caso nao exista(+), write and text
        a.close()
    except:
        print('Houve um erro na criaçao do arquivo')
    else:
        print(f'Arquivo {nome} criado com sucesso')


def lerArquivo(nome):
    try:
        a = open(nome, 'rt') #modo ler
    except:
        print('Erro ao ler o arquivo')
    else:
        cabeçalho('Pessoas Cadastradas')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30} {dado[1]:>3} anos')
        #print(a.read()) # Para ler o arquivo inteiro
    finally:
        a.close()


def cadastrar(arq, nome='desconhecido', idade=0):
    try:
        a = open(arq, 'at') #A de append, inserir algo no arquivo
    except:
        print('Houve um erro na abertura do arquivo')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um erro na hora de escrever os dados')
        else:
            print(f'Novo registro de {nome} adicionado.')
            a.close()
