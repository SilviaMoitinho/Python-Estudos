n = input('Digite algo: ')
#print (n.isnumeric()) # O isnumeric vai nos retornar verdeiro ou falso, se o que estiver dentro de n for um numero retorna verdadeiro
                        #se o que estiver dentro do n nao for um numero, retorna falso, mesmo estando a ler uma string
#print (n.isalpha()) # O isalpha retorna verdadeiro ou falso, mas ao contrario do isnumerico, se for caracter é verdadeiro, senao é falso
#print (n.isalnum()) # Vai dar verdadeiro para todas os numeros e caracteres alfabeticos
#print (n.isascii()) # Vai dar verdadeiro se tiver algo dentro
#print (n.isdecimal()) #Verdadeiro para valores decimais
#print (n.isdigit()) #Verdadeiro para valores inteiros
print (n.isidentifier()) #Verdadeiro para caracteres, sem espaços, apenas uma palavra ou letra, sem numeros
