#String sao imutaveis, por isso se quisermos mudar alguma coisa nela, temos de criar a funçao e atribuir a ela

frase = 'Curso em Video Python'

#FATIAMENTO
print(frase[9]) # V
print(frase[3:13]) # so em Vide
print(frase[:13]) #Curso em Vide
print(frase[6:]) #em Video Python
print(frase[3::2]) #s mVdoPto
print(frase[:14:4]) #Co e

#ANALISE
print(len(frase)) #21
print(frase.count('e')) #2
print(frase.count('e',0, 12)) #1
print(frase.find('thon')) #17
print(frase.find('a')) #-1
print('Curso' in frase) #True
print ('Filme' in frase) #False
print (frase.rfind('o')) # 19 (conta detras para a frente, diz qual o ultimo 'o' que achou)

#TRANSFORMACAO

print(frase.replace('Video', 'Filme')) #Curso em Filme Python
print(frase.upper()) #CURSO EM VIDEO PYTHON
print(frase.lower()) #curso em video python
print(frase.capitalize()) #Curso em video python
print(frase.title()) #Curso Em Video Python
print(frase.replace(' ','')) #CursoEmVideoPython (tira todos os espaços)

frase2 = '   Aprender Python   '
print(frase2.strip()) #Aprender Python
print(frase2.rstrip()) #   Aprender Python
print(frase2.lstrip()) #Aprender Python   (tem os espaços na direita)

#Divisao

dividido = frase.split() #temos de atribuir para assim a string mudar, porque eu preciso dela mudada para a proxima funçao
print(dividido) #['Curso','em','Video','Python']
print(dividido[1]) #em (dentro da lista acima o valor 1)
print(dividido[2][3]) #e (dentro do valor 2 o cartecter 3)

#Junçao

print('_'.join(dividido)) #Curso_em_Video_Python

#JUNTANDO FUNCOES

#frase.upper().count('O') #3, porque primeiro transformou em maiusculas e depois contou quanto O maiusculo tem (falta dar print)

#Fazer Print de um texto grande, é so abrir (""" texto, e no final fechar """)
print("""Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!""")
