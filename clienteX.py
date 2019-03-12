from socket import *
import sys
import json

host = 'localhost'	#IP do servidor
port = 3000			#Porta do servidor

try:
	socket = socket(AF_INET, SOCK_STREAM) #IP, TCP
	socket.connect((host, port))

	print ("FORMATOS DISPONÍVEIS: quadrado, circulo e triangulo")
	print ("TAMANHOS DISPONÍVEIS: pequeno, medio e grande\n")

	while True:
		cor = input("Digite uma cor: ")
		formato = input("Digite o formato: ")
		tamanho = input("Digite o tamanho: ")

		#Dicionário
		dados = {'cor': cor, 
				 'formato': formato, 
				 'tamanho': tamanho}

		#Convertendo para JSON
		dados_json = json.dumps(dados)
		
		socket.send(dados_json.encode(encoding='utf-8'))
		print ("Preparando para enviar...")

		resultado = socket.recv(1024) #retorna OK ou ERROR
		print ("Enviou")
		resposta = resultado.decode() #conversão de bytes
		print (resposta)
		print (" ")

except OSError as error:
	print ("error: {0}".format(error))

socket.close()

#1. cor, formato e tamanho
#2. o cliente tem que listar todas as opções do 1
#3. o servidor tem que retornar um erro caso o pedido não exista