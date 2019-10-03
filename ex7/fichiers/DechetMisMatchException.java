package exceptions;

/**
 * Erreur devant être lancée lorsqu'on essaie de classer
 * un déchet dans une catégorie qui n'est pas correcte.
 * Vous ne devriez pas avoir besoin de modifier cette classe
 */
public class DechetMisMatchException extends Exception {
    public DechetMisMatchException(String msg)) { super(msg); }
}
