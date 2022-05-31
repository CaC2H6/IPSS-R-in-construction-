from ast import While
from itertools import repeat
from pdb import Restart
from tkinter import W


def bold_text (string):
  return f'\033[1m{string}\033[0m'

print(bold_text("\n\n\033[93mSistema Internacional de Escores Prognósticos-Revisado (IPSS-R) - Síndrome mielodisplásica (SMD)\033[0m"))

print(bold_text('\n\nFerramenta criada por:'), 'Gabriel Caetano de Souza (Biomédico) - 2022')
print(bold_text('Lattes:'), 'http://lattes.cnpq.br/7854591047056546')
print(bold_text('\n\nBaseado em dados bibliográficos dispostos por:'), '\x1B[3mGreenberg et al.,\x1B[0m 2012.')
print(bold_text('DOI:'), '10.1182/blood-2012-03-420489')

print("\n\n\nSe você é um estudante ou profissional, aproveite a ferramenta.\n" 
    "Caso você seja um paciente, vale lembrar que toda a análise e conclusão dos dados clínicos deve ser feita apenas por um profissional habilitado.\n" 
    "\n\nFaça um bom uso!"
)
paciente = (input)(bold_text('Primeiramente, identifique o paciente: '))

print(bold_text('\n\nAgora defina o cariótipo do paciente'), f'\033[93m {paciente} \033[0m')
print(bold_text('0:'),'Ausência de metáfase')
print(bold_text('1:'), '-Y ou del(11q)')
print(bold_text('2:'), 'del(5q), del(12p), del(20q), qualquer alteração única + del(5q)')
print(bold_text('3:'), 'del(7q), +8, +19, i(17q), qualquer outra alteração única ou dupla')
print(bold_text('4:'), '-7, inv(3),t(3q), del(3q), qualquer alteração dupla que inclua -7 ou del(7q)')
print(bold_text('5:'), 'Cariótipo complexo (3 alterações)')
print(bold_text('6:'), 'Cariótipo muito complexo (4 ou mais alterações)')
print(bold_text('7:'),'Cariótipo normal')

cariotipo = int(input(bold_text('Escolha o número em qual a alteração se encaixa ao paciente: ')))

while cariotipo < 0 or cariotipo > 7:
  cariotipo = int(input(bold_text('Escolha o número em qual a alteração se encaixa ao paciente: ')))

print(bold_text('O subgrupo prognóstico do seu paciente se classifica como:'), cariotipo)
if cariotipo == 7 or cariotipo == 2:
  print ('\033[92mBom, possuindo uma expectativa de vida de em média 4,8 anos\033[0m')
elif cariotipo == 1:
  print ('\033[96mMuito bom, possuindo uma expectativa de em média 5,4 anos\033[0m')
elif cariotipo == 3:
  print ('\033[93mIntermediário, possuindo uma expectativa de em média 2,7 anos anos\033[0m')
elif cariotipo == 4 or cariotipo == 5: 
  print ('\033[91mRuim, possuindo uma expectativa de em média 1,5 anos\033[0m')
elif cariotipo == 6: 
 print ('\033[91mMuito ruim, possuindo uma expectativa de em média 0,7 anos\033[0m')
elif cariotipo == 0: 

 ausencia = int(input(bold_text('\033[95mEm casos de ausência de metáfase, não se pode concluir de maneira adequada o prognóstico do paciente. Nesse caso, o hematologista responsável deve tentar outras metodologias que ajudem no diagnóstico do devido paciente, como por exemplo, métodos de citogenética molecular, podendo ser a Técnica de Hibridização Fluorescente in Situ (FISH) ou outras similares. Caso queira continuar para a avaliação através de dados hematológicos, digite "1", caso queira encerrar o programa, tecle "0".\033[0m Caso tenha teclado o botão errado e queira repetir a avaliação do cariótipo, tecle "2".')))
 
 while ausencia < 0 or ausencia > 2:
    ausencia = int(input(bold_text('\033[95mEm casos de ausência de metáfase, não se pode concluir de maneira adequada o prognóstico do paciente. Nesse caso, o hematologista responsável deve tentar outras metodologias que ajudem no diagnóstico do devido paciente, como por exemplo, métodos de citogenética molecular, podendo ser a Técnica de Hibridização Fluorescente in Situ (FISH) ou outras similares. Caso queira continuar para a avaliação através de dados hematológicos, digite "1", caso queira encerrar o programa, tecle "0".\033[0m Caso tenha teclado o botão errado e queira repetir a avaliação do cariótipo, tecle "2".')))

