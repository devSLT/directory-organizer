import os
import shutil

#Separa os diretorios
imgDiretorio = "C:/Users/tjzin/Desktop/Organizadora/img"
docsDiretorio = "C:/Users/tjzin/Desktop/Organizadora/docs"
zipDiretorio = "C:/Users/tjzin/Desktop/Organizadora/zip"
exeDiretorio = "C:/Users/tjzin/Desktop/Organizadora/exe"

# criando diretorios caso nao existam
if not os.path.isdir(imgDiretorio):
    print("Criando novo diretorio img")
    os.makedirs(imgDiretorio)
if not os.path.isdir(docsDiretorio):
    print("Criando novo diretorio docs")
    os.makedirs(docsDiretorio)
if not os.path.isdir(zipDiretorio):
    print("Criando novo diretorio zip")
    os.makedirs(zipDiretorio)
if not os.path.isdir(exeDiretorio):
    print("Criando novo diretorio exe")
    os.makedirs(exeDiretorio)


def organizar():
    
    mainDiretorio = os.listdir("C:/Users/tjzin/Downloads/meusDownloadsBaguncados")
    
    for i in mainDiretorio:
        #Verificar tipo de arquivo imagem
        if i.endswith('.png') or i.endswith('.jpg') or i.endswith('.jpeg'):
            print("----------- IMAGE -------------")
            print(i)
            
            # movendo para diretorio organizador
            shutil.move(i, imgDiretorio)
        
        #Verificando arquivo docs
        if i.endswith(".pdf") or i.endswith('.docx'):
            print("----------- DOCUMENTO ---------")
            print(i)
            
            # movendo para diretorio organizador    
            shutil.move(i, docsDiretorio)
            
        #Verificando arquivo ZIP
        if i.endswith(".zip") or i.endswith('.rar') or i.endswith('.txt'):
            print("----------- ZIP ---------")
            print(i)
            
            # movendo para diretorio organizador    
            shutil.move(i, zipDiretorio)
            
        #Verificando arquivo EXECUTAVEIS
        if i.endswith(".exe") or i.endswith('.jar'):
            print("----------- EXECUTAVEL ---------")
            print(i)
            
            # movendo para diretorio organizador    
            shutil.move(i, exeDiretorio)
        
        print("Arquivos novo diretorio")
        print("-----Imagem----")
        print(os.listdir(imgDiretorio))
        print("-----Docs----")
        print(os.listdir(docsDiretorio))
        print("-----Zip----")
        print(os.listdir(zipDiretorio))
        print("-----Exe----")
        print(os.listdir(exeDiretorio))

organizar()