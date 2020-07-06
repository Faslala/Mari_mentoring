''' 3. Permita que o usuário insira um texto de até 250 caracteres, e inclua um botão 
que permita exportar o texto em arquivo na extensão ".txt"'''

def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criarArquivo(nome):
    try:
        a = open(nome, "wt+")
        a.close()
    except:
        print('Houve um erro na criacao do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')

arq = "nome_arquivo.txt"
if not arquivoExiste(arq):
    criarArquivo(arq)


texto = input("Digite um texto de ate 250 caracteres:")



