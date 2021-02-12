# -*- coding: utf-8 -*-
"""
GENERADOR DE CLASES DESDE EL DIAGRAMA UML. 
"""
import re
def imprimeClase(fichero, clase, atributos, metodos,hshE):
    fpy = open(fichero, 'wt+')
    if(clase in hshE.keys()):
        fpy.write("class {}({}):\n".format(clase,hshE[clase]))

    else:
        fpy.write("class {}():\n".format(clase))
        fpy.write("\tdef __init__(self")
        for item in atributos[0] + atributos[1] + atributos[2]:
            fpy.write(", {}".format(item))
        fpy.write("):\n")
        for item in atributos[0] + atributos[1] + atributos[2]:
            fpy.write("\t\tself.{} =  {}\n".format(item, item))
        fpy.write("\tdef __str__(self):\n")
        fpy.write("\t\treturn '-------------------------------------------------'\n")
        fpy.write("\n")
        for item in atributos[1] + atributos[2]:
            fpy.write("\t@property\n")
            fpy.write("\tdef {}(self):_\n".format(item))
            fpy.write("\t\treturn self.__{}\n".format(item))
        fpy.write("\n")
        for item in atributos[1] + atributos[2]:
            fpy.write("\t@{}.setter\n".format(item))
            fpy.write("\tdef {}(self, {}):\n".format(item, item))
            fpy.write("\t\tself.__{} = {}\n".format(item, item))
        fpy.write("\n")
        for item in metodos:
            fpy.write("\tdef {}(self):\n".format(item))
            fpy.write("\t\tpass\n")
        fpy.close()

    
if __name__=="__main__":
    try:
        hsh = {}
        publicos = []
        protegidos = []
        privados = []
        metodos = []
        hshE = {}
        hshC = {}
        hshA = {}
        dentroClase = 0
        with open("plantillaUML.txt") as fichero:
            for linea in fichero:
                linea = linea.strip()
                if(len(linea)==0 or linea[0]=='@'):
                    continue
                elif(dentroClase == 0 and linea[:5]=='class'):                   
                    dentroClase = 1 
                    clase = linea[5:-1].strip()
                elif(dentroClase == 0):
                    m = re.search(r'\s*([A-Z]?[A-Za-z_]*)\s*(<?(?:\||o|\*)?--)\s*([A-Z]?[A-Za-z_]*)\s*', linea)
                    if(m.group(2)=='<|--'):
                        hshE.setdefault(m.group(3), []).append(m.group(1))
                    elif(m.group(2)=='*--'):
                        hshC[m.group(1)] = m.group(3)
                    elif(m.group(2)=='o--'):
                        hshA[m.group(1)] = m.group(3)
                elif(dentroClase==1 and linea[0]=='}'):                    
                    hsh[clase] = [[publicos,protegidos,privados],metodos]
                    dentroClase = 0
                    publicos = []
                    protegidos = []
                    privados = []
                    metodos = []                    
                elif(dentroClase==1 and linea[-1] == ')'):                   
                    metodos.append(linea[:linea.find('(')])                      
                elif(dentroClase == 1 and linea[0:]=='-'):                   
                    privados.append(linea[1:])                   
                elif(dentroClase == 1 and linea[0:]=='#'):                    
                    protegidos.append(linea[1:])                    
                elif(dentroClase == 1 and linea[0:]=='+'):                    
                    publicos.append(linea[1:])
                else:
                    publicos.append(linea)
                
        
        fichero.close()
        print(hsh)
        print(hshE)
        
    except Exception as e:
        print("Error: " + str(e))
