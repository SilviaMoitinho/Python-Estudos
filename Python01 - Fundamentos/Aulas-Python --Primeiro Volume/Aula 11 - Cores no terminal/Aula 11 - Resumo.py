'''
codigo : \033[     m

estilo
0 - nenhum
1 - negrito
4 - sublinhado
7 - inverter

cores de texto    cores de fundo
30 - cinza ------- 47
31 - vermelho ---- 41
32 - verde ------- 42
33 - amarelo ----- 43
34 - azul -------- 44
35 - roxo -------- 45
36 - azul ciano -- 46
37 - branco ------ 40
'''

print('\033[31mOla Mundo!') # Letra em vermelho
print('\033[36;41mOla Mundo') # letra ciano e fundo vermelho
print('\033[mteste') # para voltar ao normal
print('\033[4;37;45m Ola Mundo!\033[m ') # sublinhado com letra branco e fundo roxo, terminar com o codigo para nao influenciar o seguinte
print('\033[7;37m Ola Mundo... \033[m') # fundo branco e letra preto