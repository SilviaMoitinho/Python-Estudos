n = input('Digite algo: ')
print ('O tipo primitivo desse valor é: ', type(n))
print ('So tem espaçoes?', n.isspace())
print ('E um numero?', n.isnumeric())
print ('E alfabetico? ', n.isalpha())
print ('E alfanumerico? ', n.isalnum())
print ('Esta em maiuculas? ', n.isupper())
print ('Esta em minusculas? ', n.islower())
print ('Esta capitalizada? ', n.istitle()) #A primeira letra maiuscula