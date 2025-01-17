import os ##importa a biblioteca os para enviar comandos ao sistema operacional
import pyaes ## importa a biblioteca pyaes para utilizar comando de criptografia

## abrir o arquivo a ser descriptografado

## criada variavel file_name para armazenar o arquivo teste.txt.ransomwaretroll
file_name = 'teste.txt.ransomwaretroll'
## criada variavel file para armazenar conteúdo da variavel file_name, 'rb' comando para somente ler a variavel
file = open(file_name,'rb')
## criada variavel file_data para receber o conteudo lido na variavel file
file_data = file.read()
## fechando a variavel file
file.close()

## definir a chave de descriptografia

## criada variavel key para armazenar a chave de descriptografia
key = b'testeransomwares'
## criada variavel aes para armazenar a funçao de descriptografia com a variavel key como parametro
aes = pyaes.AESModeOfOperationCTR(key)

## Descriptografar o arquivo

## criada variavel decrypt_data para receber o arquivo a descriptografar da variavel file_data
decrypt_data = aes.decrypt(file_data)

## remover o arquivo criptografado

## chama função os.remove() com o parametro file_name que contem o nome do arquivo a ser deletado
os.remove(file_name)

## criar um novo arquivo descriptografado

## criada variavel new_file para armazenar o nome do arquivo 
new_file = 'teste.txt'
## variavel new_file recebe os dados, funcao open.() a funcao 'wb' escreve os dados
new_file = open(f'{new_file}','wb')
## funcao .write() escreve os dados descriptografados da variavel decrypt_data na variavel new_file 
new_file.write(decrypt_data)
# funcao .close() fecha a variavel new_file
new_file.close()
