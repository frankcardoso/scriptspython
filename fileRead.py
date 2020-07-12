'''
Created on 04/02/2016

@author: Frank Cardoso
Empresa: BC Gestao

Versao: 1.0

'''
# -*- coding: utf-8 -*-
# Programa de leitura e criacao de arquivo para inventario
# Autor: Frank Cardoso
# Data: 28/08/2015

#--------------------------------------------------------
import traceback
#--------------------------------------------------------
def readFile(r_file, w_file):
    arq_read = r_file
    arq_write = w_file
    f = open(arq_read, 'r')
    text = f.readlines()

    for line in text:
        codigo = line[:13]

        if 'U' in codigo:
            a = ''

        else:
            if line[0] == '0':
                try:
                    temp = open(arq_write, 'a')
                    temp.writelines(line[:14])
                    temp.close()

                except:
                    trace = traceback.format_exc()
                    print 'Aconteceu um erro:\n', trace

            elif line[0] == '7':
                try:
                    temp = open(arq_write, 'a')
                    temp.writelines(line[:14])
                    temp.close()

                except:
                    trace = traceback.format_exc()
                    print 'Aconteceu um erro:\n', trace
            else:
                try:
                    temp = open(arq_write, 'a')
                    temp.writelines(line[:14] + line[15:19] + ';' + '\n')
                    temp.close()

                except:
                    trace = traceback.format_exc()
                    print 'Aconteceu um erro:\n', trace
