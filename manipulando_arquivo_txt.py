## Vamos abrir um arquivo para Leitura ##
arq1 = open('arquivos/arquivo.txt','r')


# \ de windows
# / de linux


## Ler o arquivo

print(arq1.read())

## Retorna ao inicio do arquivo com a funcao seek

arq1.seek(0)

print(arq1.read())

## Fechar o arquivo

arq1.close()


## Abrir um arquivo para opcao de gravação opção de gração e leitura

arq2 = open('arquivos/arquivo.txt','w+')
arq2.write('tem novo conteudo\n')
arq2.write('tem novo conteudo escrito novamente\n')


## Voltar o cursor para cima 

arq2.seek(0)

## Ler o arquivo

print(arq2.read())

## Fechar o arquivo
arq2.close()

## Inserir dados sem sobrescrever, vamos usar a funcão "APPEND a+"

arq3 = open('arquivos/arquivo.txt','a+')

arq3.write("Nova Escrita sem Excluir")

## Trazer o cursor para a linha 0

arq3.seek(0)

print(arq3.read())

arq3.close()

## Utilizando contexto de manipulação de Aquivos.
## Pode ser qualquer tipo.
## É uma boa pratica e mantem o codigo organizado e performado.
## WITH open vai gerar um nome de contexto para o arquivo
## Segue exemplo abaixo:

with open('arquivos/arquivo.txt','w+') as f:
    f.write('Nova Linha\n')
    f.write("Novamente Linha\n")
    f.seek(0)
    print(f.read())
    f.close()

# Criando um novo arquivo do 0

with open('arquivos/arquivo1.txt','w+') as f:
    f.write('Teste Linha\n')
    f.write('Teste Linha\n')
    f.seek(0)
    print(f.read())
    f.close()   
