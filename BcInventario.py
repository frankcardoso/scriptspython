# -*- coding: utf-8 -*-
# Programa de leitura e criação de arquivo para inventário de varejo
# Autor: Frank Cardoso
# Data: 04/02/2016
# Versão: 1.0
from fileRead import readFile
from fileWrite import writeFile

print '####################################################'
print '#                                                  #'
print '#                                                  #'
print '#       BC Inventario                              #'
print '#       Programa de formatacao de arquivo txt      #'
print '#                                                  #'
print '#                                                  #'
print '####################################################'
print '\n'

#--------------------------------------------------------
import fileWrite
import fileRead
#--------------------------------------------------------

class inventario(object):

    print '\tSelecione uma opcao abaixo para iniciar o programa.'
    print '\n'
    print '\t1 - Ajustar o arquivo recebido do cliente.'
    print '\n'

    a = raw_input('\tArquivo de leitura: ')
    b = raw_input('\tArquivo de escrita: ')

    readFile(a, b)

    print '\n'
    print '\n\t2 - Ajustar o arquivo que sera enviado para o sistema de gestao.'
    print '\n'

    c = raw_input('\tArquivo de leitura: ')
    d = raw_input('\tArquivo de escrita: ')

    writeFile(c, d)

    print '\n\tSistema finalizado, muito Obrigado!'

