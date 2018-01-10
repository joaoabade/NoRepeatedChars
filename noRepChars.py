########################################
#### AVOID REPEATED CHARS WORDS  	####
####	       WITH PYTHON	   		####
########################################


# Constantes 


## Comienza la logica del programa

print ">>>>>>>>Empieza lectura de fichero>>>>>>>>>>>" 

infile = open('dict.txt', 'r')
outfile = open('betterdict.txt','a')


line = infile.readline()

while line != '':
	print(line)
	length = len(line) - 1
	index = 0	
	validWord = True
	
	## Comprobacion de caracteres repetidos
	while (index < length) and (validWord == True):
		char = line[index] 
		for j in range(index + 1, length):
			if char == line [j]:
				validWord = False				
				print("Caracter repetido, skip word: " + line)				
				break
		
		index += 1	
						
	if validWord == True:
		outfile.write(line)
	
	## Nueva palabra 		
	line = infile.readline()
	 			

	
infile.close()
outfile.close()