import os

class FileMngr:

    def __init__(self):
        self.dir = ""
        self.folder = ""
        self.flag = False

    def createFolder(self, folder, dir):
        self.dir = dir
        self.folder = folder
        print('dentro do create folder')
        path = self.dir +'\\'+ self.folder

        if self.flag == False:
            try:
                os.mkdir(path)
                self.flag = True #CRIAR UM LOG DAS PASTAS CRIADAS EM CADA EXECUÇÃO
                print('pasta criada')
                return path
            except OSError as error:
                print(error)
            except Exception as e:
                print(e)