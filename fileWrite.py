
# Programa de leitura e criacao de arquivo para inventario
# Autor: Frank Cardoso
# Data: 28/08/2015

import traceback


def writeFile(rFile, wFile):
    arq_read = rFile
    arq_write = wFile
    f = open(arq_read, 'r')
    text = f.readlines()

    for line in text:
        ci = line[:13]
        cb = line[14:27]
        desc = line[28:41]

        if '.' in desc:
            qt = line[42:46]

            if cb[0] == '7':
                if '-' in qt:
                    texto = cb + '|0' + str(int(ci)) + '|' + desc + '|0|' + '\n'
                else:
                    texto = cb + '|0' + str(int(ci)) + '|' + desc + '|' + str(int(qt)) + '|' + '\n'

                    try:
                        temp = open(arq_write, 'a')
                        temp.writelines(texto)
                        temp.close()

                    except:
                        trace = traceback.format_exc()
                        print('Aconteceu um erro:\n', trace)
            else:
                if '-' in qt:
                    texto = ci + '|0' + str(int(cb)) + '|' + desc + '|0|' + '\n'
                else:
                    texto = ci + '|0' + str(int(cb)) + '|' + desc + '|' + str(int(qt)) + '|' + '\n'

                    try:
                        temp = open(arq_write, 'a')
                        temp.writelines(texto)
                        temp.close()

                    except:
                        trace = traceback.format_exc()
                        print ('Aconteceu um erro:\n', trace)

        else:
            if '.' in cb:
                texto = ci + '|' + desc[29:33] + '|' + desc[29:33] + '|' + '\n'

            else:
                if '.' in qt:
                    qt = line[42:56]
                    obs = line[56:60]

                    if '-' in obs:
                        texto = cb + '|' + ci + '|' + qt + '|0|' + '\n'
                    else:
                        texto = cb + '|' + ci + '|' + qt + '|' + obs + '|' + '\n'

                    try:
                        temp = open(arq_write, 'a')
                        temp.writelines(texto)
                        temp.close()

                    except:
                        trace = traceback.format_exc()
                        print ('Aconteceu um erro:\n', trace)
                else:
                    obs = line[56:70]
                    obs1 = line[71:75]
                    if '-' in obs1:
                        texto = texto = cb +'|'+ ci +'|'+ obs + '|0|' + '\n' # + descricao + '|' + obs + '|' + obs +'|'+ obs +'|'+'\n'+ quant + '|' + obs + '|' + obs +'|'+ obs1 +'|'+'\n'
                    else:
                        texto = texto = cb +'|'+ ci +'|'+ obs + '|' + obs1 + '|' + '\n' # + descricao + '|' + obs + '|' + obs +'|'+ obs +'|'+'\n'+ quant + '|' + obs + '|' + obs +'|'+ obs1 +'|'+'\n'
