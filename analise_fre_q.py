#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# USAR APENAS O "LETTERS" PRETENDIDO. NO MATPLOTLIB NAO APARECEM ACENTUAÇÕES OU CARACTERES ESPECIAIS
#LETRAS = 'ẼÍÉÓÁÀ1234567890ÕÃÇABCDEFGHIJKLMNOPQRSTUVWXYZ'
LETRAS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
print("LETRAS:%s" % len(LETRAS))

def ContarLetras(texto):
    # Devolve dicionario com todas as letras e o seu valor numerico

    #USAR APENAS O LETTERCOUNT PRETENDIDO. NO MATPLOTLIB NAO APARECEM ACENTUAÇÕES OU CARACTERES ESPECIAIS
    letterCount = {'Ẽ':0,'Í':0,'É':0,'Ó': 0,'Á': 0,'À': 0,
        '1': 0,'2': 0,'3': 0,'4': 0,'5': 0,'6': 0,'7': 0,'8': 0,'9':0,'0':0,
        'Õ':0,'Ã':0,'Ç': 0,
        'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0
        }
    #abecedario normal-26
    letterCount = {
        'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0
        }


    for letter in texto.upper():
        if letter in LETRAS:
            letterCount[letter] += 1

    return letterCount

texto="""Ó Minha Felicidade
Revejo os pombos de São Marcos:
A praça está silenciosa; ali se repousa a manhã.
Indolentemente envio os meus cantos para o seio da suave frescura,
Como enxames de pombos para o azul
Depois torno a chamá;-los
Para prender mais uma rima &agrave;s suas penas.
&mdash; ó minha felicidade! ó minha felicidade!
ã
Calmo céu, céu azul-claro, céu de seda,
Planas, protector, sobre o edifício multicor
De que gosto, que digo eu?... Que receio, queá»invejo...
Como seria feliz bebendo-lhe a alma!
Alguma vez lha devolveria?
Não, não falemos disso, ó maravilha dos olhos!
&mdash; ó minha felicidade! ó minha felicidade!
ã
Severa torre, que impulso leonino
Te levantou ali, triunfante e sem custo!
Dominas a praça com o som profundo dos teus sinos...
Serias, em francês, o seu «accent aigu»!
Se, como tu, eu ficasse aqui,
Saberia a seda que me prende...
&mdash; ó minha felicidade! ó minha felicidade!
ã
Afasta-te, m&uacute;sica. Deixa primeiro as sombras engrossar
E crescer até &agrave; noite escura e tépida.
é ainda muito cedo para ti, os teus arabescos de ouro
Ainda não cintilam no seu esplendor de rosa;
Resta ainda muito dia,
Muito dia para os poetas, fantasmas e solitá;rios.
&mdash; ó minha felicidade! ó minha felicidade!
"""

#texto="aaa bb c"
letras=(ContarLetras(texto))


CHAVE=[]
QUANTIDADE=[]
LINHA=""

for k, v in letras.items():
    CHAVE.append(k)
    QUANTIDADE.append(v)
    LINHA=("%s%s"% (LINHA,k))

LINHA=LINHA[:-1]
print("Tamanho:%s %s" % (len(LINHA),LINHA))
print("qtd:%s %s" % (len(QUANTIDADE),QUANTIDADE))

import matplotlib.pyplot as plt;

plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt


y_pos = np.arange(len(CHAVE))

#44 PARA TODAS AS LETRAS. 26 PARA ALGUMAS
for i in range(26):
    print(i,CHAVE[i],QUANTIDADE[i])

plt.bar(y_pos, QUANTIDADE, align='center', alpha=0.5)
plt.xticks(y_pos, CHAVE)
plt.ylabel('Quantidade')
plt.title('Frequência de caracteres')

#MOSTRAR OU GRAVAR
#plt.show()
plt.savefig("foo.png",dpi=200)

#instrucoes para o git
#git clone https://github.com/........git
#git add *
#git config --global user.email "email"
#git commit -m "Commit message"
#git push origin master
#colocar email e depois a passe