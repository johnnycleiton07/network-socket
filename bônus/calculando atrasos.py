'''
Um programa para calcular ATRASO DE TRANSMISSÃO E PROPAGAÇÃO
- É preciso especificar da unidade de medida de cada valor dado (GB, MB, bits, Km...)
- E fazer a conversão dos dados, caso necessário
'''

def menu():
	print ("CALCULOS DE ATRASO: \n Digite 1 para ATRASO DE TRANSMISSÃO \n Digite 2 para ATRASO DE PROPAGAÇÃO \n")
	
	opcao = int(input("Entre com a sua escolha: "))

	if (opcao == 1):
		print ("\n======================")
		print ("ATRASO DE TRANSMISSÃO")
		transmissao()

	elif (opcao == 2):
		print ("\n=====================")
		print ("ATRASO DE PROPAGAÇÃO")
		propagacao()

	else:
		print ("ENTRADA INVÁLIDA!")

#_______________________________________________ATRASO DE TRANSMISSÃO________________________________________________________#

def transmissao():
	print (" L = tamanho do pacote em bits \n R = taxa de transmissão em bits/seg\n========================")
	print ("\nDigite o valor [ENTER] e em seguida especifique qual a medida de internet: \nOPÇÕES: bits - Byte - Kb - KB - Mb - MB - Gb - GB\n")

	l = float(input("L = "))
	medL = (input("Medida: "))

	r = float(input("R = "))
	medR = (input("Medida: "))

	if (medL != "bits") and (medL != "Byte") and (medL != "KB") and (medL != "MB") and (medL != "GB") and (medL != "Kb") and (medL != "Mb") and (medL != "Gb"):
		print ("Unidade de medida de internet inválida para o tamanho do pacote(L)!")

	elif (medR != "bits") and (medR != "Byte") and (medR != "KB") and (medR != "MB") and (medR != "GB") and (medR != "Kb") and (medR != "Mb") and (medR != "Gb"):
		print ("Unidade de medida de internet inválida para a taxa de transmissão(R)!")

	else:
		conversaoT(medL, medR, l, r)



def conversaoT(medL, medR, l, r):
	if (medL == "GB") and (medR == "MB"):
		l = (l*1000) # MB <- GB

	elif (medL == "MB") and (medR == "GB"):
		r = (r*1000) # MB <- GB


	elif (medL == "GB") and (medR == "KB"):
		l = ((l*1000)*1000) # KB <- MB <- GB

	elif (medL == "KB") and (medR == "GB"):
		r = ((r*1000)*1000) # KB <- MB <- GB
	

	elif (medL == "GB") and (medR == "Byte"):
		l = (((l*1000)*1000)*8) # Byte <- KB <- MB <- GB

	elif (medL == "Byte") and (medR == "GB"):
		r = (((r*1000)*1000)*8) # Byte <- KB <- MB <- GB


	elif (medL == "GB") and (medR == "bits"):
		l = ((((l*1000)*1000)*1000)*8) # bits <- Byte <- KB <- MB <- GB

	elif (medL == "bits") and (medR == "GB"):
		r = ((((r*1000)*1000)*1000)*8) # bits <- Byte <- KB <- MB <- GB


	elif (medL == "GB") and (medR == "Gb"):
		l = (l * 8) # Gb <- GB

	elif (medL == "Gb") and (medR == "GB"):
		r = (r * 8) # Gb <- GB


	elif (medL == "GB") and (medR == "Mb"):
		l = ((l * 8)*1000) # Mb <- Gb <- GB

	elif (medL == "Mb") and (medR == "GB"):
		r = ((r * 8)*1000) # Mb <- Gb <- GB


	elif (medL == "GB") and (medR == "Kb"):
		l = (((l * 8)* 1000)* 1000) # Kb <- Mb <- Gb <- GB

	elif (medL == "Kb") and (medR == "GB"):
		r = (((r * 8)* 1000)* 1000) # Kb <- Mb <- Gb <- GB


	# MB

	elif (medL == "MB") and (medR == "KB"):
		l = (l*1000) # KB <- MB

	elif (medL == "KB") and (medR == "MB"):
		r = (r*1000) # KB <- MB


	elif (medL == "MB") and (medR == "Byte"):
		l = ((l*1000)*1000) # Byte <- KB <- MB

	elif (medL == "Byte") and (medR == "MB"):
		r = ((r*1000)*1000) # Byte <- KB <- MB

	
	elif (medL == "MB") and (medR == "bits"):
		l = (((l*1000)*1000)*8) # bits <- Byte <- KB <- MB

	elif (medL == "bits") and (medR == "MB"):
		r = (((r*1000)*1000)*8) # bits <- Byte <- KB <- MB


	elif (medL == "MB") and (medR == "Gb"):
		r = (r * 128) # MB <- Gb

	elif (medL == "Gb") and (medR == "GB"):
		l = (l * 128) # MB <- Gb


	elif (medL == "MB") and (medR == "Mb"):
		l = (l * 8) # Mb <- MB

	elif (medL == "Mb") and (medR == "MB"):
		r = (r * 8) # Mb <- MB


	elif (medL == "MB") and (medR == "Kb"):
		l = ((l * 8)* 1000) # Kb <- KB <- Mb <- MB

	elif (medL == "Kb") and (medR == "MB"):
		r = ((r * 8)* 1000) # Kb <- KB <- Mb <- MB


	# KB

	elif (medL == "KB") and (medR == "Byte"):
		l = (l*1000) # Byte <- KB

	elif (medL == "Byte") and (medR == "KB"):
		r = (r*1000) # Byte <- KB

	
	elif (medL == "KB") and (medR == "bits"):
		l = ((l*1000)*8) # bits <- Byte <- KB

	elif (medL == "bits") and (medR == "MB"):
		r = ((r*1000)*8) # bits <- Byte <- KB


	elif (medL == "KB") and (medR == "Gb"):
		r = ((r * 128)*1000) # KB <- Mb <- MB <- Gb

	elif (medL == "Gb") and (medR == "KB"):
		l = ((l * 128)*1000) # KB <- Mb <- MB <- Gb


	elif (medL == "KB") and (medR == "Mb"):
		l = (l * 128) # KB <- Mb

	elif (medL == "Mb") and (medR == "KB"):
		r = (r * 128) # KB <- Mb


	elif (medL == "KB") and (medR == "Kb"):
		l = (l * 8) # Kb <- KB

	elif (medL == "Kb") and (medR == "KB"):
		r = (r * 8) # Kb <- KB


	# Gbits

	elif (medL == "Gb") and (medR == "Mb"):
		l = (l * 1000) # Mb <- Gb

	elif (medL == "Mb") and (medR == "Gb"):
		r = (r * 1000) # Mb <- Gb


	elif (medL == "Gb") and (medR == "Kb"):
		l = ((l * 1000)*1000) # Kb <- Gb

	elif (medL == "Kb") and (medR == "Gb"):
		r = ((r * 1000)*1000) # Kb <- Gb


	elif (medL == "Gb") and (medR == "bits"):
		l = ((((l * 1000)* 1000)*8)*128) # bits <- Gb

	elif (medL == "bits") and (medR == "Gb"):
		r = ((((r * 1000)* 1000)*8)*128) # bits <- Gb

	# Mbits

	elif (medL == "Mb") and (medR == "Kb"):
		l = (l * 1000) # Kb <- Mb

	elif (medL == "Kb") and (medR == "Mb"):
		r = (r * 1000) # Kb <- Mb


	elif (medL == "Mb") and (medR == "bits"):
		l = ((l * 1000)*1000) # bits <- Mb

	elif (medL == "bits") and (medR == "Mb"):
		r = ((r * 1000)*1000) # bits <- Mb

	# Kbits

	elif (medL == "Kb") and (medR == "bits"):
		l = (l * 1000) # bits <- Kb

	elif (medL == "bits") and (medR == "Kb"):
		r = (r * 1000) # bits <_Kb

	else:
		pass


	print ("\nValores Convertidos [caso necessário]:")	
	print ("L: ", l)
	print ("R: ", r)

	t = l/r

	print ("\nAtraso de Transmissão = ", t, "s")


#_______________________________________________ATRASO DE PROPAGAÇÃO________________________________________________________#

def propagacao():
	print (" d = distância entre os roteadores \n s = velocidade de propagação em m/s\n========================")
	print ("\nDigite o valor [ENTER] e em seguida especifique qual a medida de comprimento: \nOPÇÕES: m - km\n")

	d = float(input("d = "))
	medD = (input("Medida: "))

	s = float(input("s = "))
	medS = (input("Medida: "))

	if (medD != "km") and (medD != "m"):
		print ("Unidade de medida de comprimento inválida para distância(d)!")

	elif (medS != "km") and (medS != "m"):
		print ("Unidade de medida de comprimento inválida para velocidade(s)!")

	else:
		conversaoP(medD, medS, d, s)

def conversaoP(medD, medS, d, s):
	if (medD == "m") and (medS == "km"):
		d = (d/1000) # km <- m

	elif (medD == "km") and (medS == "m"):
		s = (s/1000) # km <- m

	else:
		pass

	print ("\nValores Convertidos [caso necessário]:")	
	print ("d: ", d)
	print ("s: ", s)

	p = d/s

	print ("\nAtraso de Propagação = ", p, "m/s")


menu()


