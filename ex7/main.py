from ex7.loader import Loader
from ex7.queue import Queue
from ex7.file_analyser import FileAnalyser

DOSSIER = 'fichiers'

if __name__ == '__main__':
    loader = Loader()
    fileQueue = Queue(loader.list_folder(DOSSIER))
    correctFilesQueue = Queue()
    incorrectFilesQueue = Queue()

    while not fileQueue.is_empty():

        file = fileQueue.remove()
        fileContent = loader.load(DOSSIER + "\\" + file)

        fileAnalyser = FileAnalyser(fileContent)
        if fileAnalyser.analyse():
            correctFilesQueue.add(file)
        else:
            incorrectFilesQueue.add(file)

    print("Voici les fichiers qui contiennent des erreurs :")
    while not incorrectFilesQueue.is_empty():
        print(incorrectFilesQueue.remove().split(".")[0])

    print("")

    print("Voici les fichiers qui sont corrects :")
    while not correctFilesQueue.is_empty():
        print(correctFilesQueue.remove().split(".")[0])
