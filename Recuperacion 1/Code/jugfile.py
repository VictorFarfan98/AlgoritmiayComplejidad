#import dispy
from jug import TaskGenerator, iteratetask, Task, task, io
import shutil, os                                                                               
from time import sleep

beginRead = False
endRead = False
beginMerge = False
endMerge = False
beginWrite = False
endWrite = False

#@TaskGenerator
def mergeSort(alist):
    global beginMerge
    global endMerge

    beginMerge = True
    #print("Splitting -->",alist)
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
    #print("Merging -->",alist)
    endMerge = True
    #return alist

#@TaskGenerator
def leerArchivo(fileName):
    global listado
    global beginRead
    global endRead

    beginRead = True

    #print("Antes de abrir el archivo para leer -->")
    toread = open(fileName, "r")
    listado = toread.readlines()
    #print("despues de leer lineas-->", listado, "\n\n")
    
    endRead = True

@TaskGenerator
def escribirArchivo(fileName, oracion):
    global listado
    global beginWrite
    global endWrite

    beginWrite = True
    #print("Antes de sortear")
    #sorteado = self.mergeSort(self.list)
    #print("Antes de escribir -->",listado, "\n\n")
    tosave = open(fileName, "a+")
    tosave.write(oracion)
    #print("Despues de escribir  -->")
    tosave.close()
    endWrite = True
#@TaskGenerator

#python binaries located in /usr/local/bin
#print(tosort)

listado = []

try:
    shutil.rmtree("jugfile.jugdata")
except:
    pass


#print("INICIO INICIO INICIO INICIO")
#print("Antes de leer: \n\n")
leerArchivo("mergesort_input.txt")
#print("Despues de leer: ", listado, "\n\n")
mergeSort(listado)
#print("Despues de hacer sort:" , listado, "\n\n")
for s in listado:
    escribirArchivo("save.txt", s)
#print("Despues de escribir el archivo: \n\n")


comprobacion = open("save.txt", "r")
for line in comprobacion.readlines():
    print(line[:-1])