from socket import *
import sys
import time
import pygame
import json

host = 'localhost'
port = 3000

confirmacao = "OK"
erro = "ERROR"
branco = (255, 255, 255)
preto = (0, 0, 0)

#CONFIGURAÇÕES DO SERVIDOR
socket = socket(AF_INET, SOCK_STREAM)
socket.bind((host, port))
socket.listen(1)

print ("-")
print ("SERVIDOR PREPARADO PARA CONEXÃO...")

while True:
	conexao, cliente = socket.accept() #aceita conexão com cliente
	print ("SERVIDOR CONECTADO AO CLIENTE: ", cliente)
	
	while True:
		try:
			recebido = conexao.recv(1024)
			recebido = recebido.decode() #conversão de bytes
			
			recebidoJSON = json.loads(recebido)
			print ("Servidor recebeu:", recebidoJSON)

			tela = pygame.display.set_mode((400, 400))
			tela.fill(branco)

			if (recebidoJSON['cor'] == "branco"):
				cor = (255, 255, 255)
				tela.fill(preto)
			elif (recebidoJSON['cor'] == "cinza"):
				cor = (128, 128, 128)
			elif (recebidoJSON['cor'] == "preto"):
				cor = (0, 0, 0)
			elif (recebidoJSON['cor'] == "vermelho"):
				cor = (255, 0, 0) 
			elif (recebidoJSON['cor'] == "amarelo"):
				cor = (255, 255, 0)
			elif (recebidoJSON['cor'] == "laranja"):
				cor = (255, 100, 0)
			elif (recebidoJSON['cor']== "marrom"):
				cor = (128, 0, 0)
			elif (recebidoJSON['cor'] == "verde"):
				cor = (0, 255, 0)
			elif (recebidoJSON['cor'] == "azul"):
				cor = (0, 0, 255)
			elif (recebidoJSON['cor'] == "rosa"):
				cor = (255, 0, 255)
			elif (recebidoJSON['cor'] == "roxo"):
				cor = (128, 0, 128)
			else:
				pygame.quit()
				print ("erro: [Errno 402] Operation unavailable")
				conexao.send(str.encode(erro))
				continue

			if (recebidoJSON['formato'] == "quadrado"):
				if (recebidoJSON['tamanho'] == "pequeno"):
					pygame.draw.rect(tela, cor, [150, 150, 100, 100])

				elif (recebidoJSON['tamanho'] == "medio"):
					pygame.draw.rect(tela, cor, [100, 100, 200, 200])

				elif (recebidoJSON['tamanho'] == "grande"):
					pygame.draw.rect(tela, cor, [50, 50, 300, 300])

				else:
					pygame.quit()
					print ("erro: [Errno 402] Operation unavailable")
					conexao.send(str.encode(erro))
					continue


			elif(recebidoJSON['formato'] == "circulo"):
				if (recebidoJSON['tamanho'] == "pequeno"):
					pygame.draw.ellipse(tela, cor, [150, 150, 100, 100])

				elif (recebidoJSON['tamanho'] == "medio"):
					pygame.draw.ellipse(tela, cor, [100, 100, 200, 200])

				elif (recebidoJSON['tamanho'] == "grande"):
					pygame.draw.ellipse(tela, cor, [50, 50, 300, 300])

				else:
					pygame.quit()
					print ("erro: [Errno 402] Operation unavailable")
					conexao.send(str.encode(erro))
					continue


			elif(recebidoJSON['formato'] == "triangulo"):
				if (recebidoJSON['tamanho'] == "pequeno"):
					pygame.draw.polygon(tela, cor, [[200, 150], [110, 250], [290, 250]]) 

				elif (recebidoJSON['tamanho'] == "medio"):
					pygame.draw.polygon(tela, cor, [[200, 100], [90, 290], [310, 290]])

				elif (recebidoJSON['tamanho'] == "grande"):
					pygame.draw.polygon(tela, cor, [[200, 50], [50, 350], [350, 350]])

				else:
					pygame.quit()
					print ("erro: [Errno 402] Operation unavailable")
					conexao.send(str.encode(erro))
					continue

			else:
				pygame.quit()
				print ("erro: [Errno 402] Operation unavailable")
				conexao.send(str.encode(erro))
				continue

			pygame.init()
			pygame.display.flip()
			time.sleep(4)
				
			pygame.quit()
				
			conexao.send(str.encode(confirmacao))


		except OSError as error:
			print ("ERROR: {0}".format(error))

	conexao.close()