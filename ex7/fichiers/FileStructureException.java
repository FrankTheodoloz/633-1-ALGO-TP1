package exceptions;

/**
 * Erreur devant être lancée si le fichier contient des données incorrectes.
 * Vous ne devriez pas avoir besoin de modifier cette classe
 */
public class FileStructureException extends Exception {
    public FileStructureException(String msg) { super(msg); }
}