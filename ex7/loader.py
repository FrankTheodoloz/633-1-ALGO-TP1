import os


class Loader:
    """
    Classe dont la responsibilité est de gérer le chargement des fichiers
    """

    def load(self, filename: str) -> str:
        """
        Fonction qui retourne la source d'un fichier au format string
        :param filename: nom du fichier
        :return: source d'un fichier
        """
        my_file = open(filename, 'r')
        return my_file.read()

    def list_folder(self, folder: str) -> list:
        """
        Fonction qui permet de lister tous les fichiers dans un dossier
        :param folder: nom du dossier
        :return: liste des noms de tous les fichiers
        """
        return sorted(os.listdir(folder))
