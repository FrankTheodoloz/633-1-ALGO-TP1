package domaine;

/**
 * Vous ne devriez pas avoir besoin de modifier cette classe
 */
public class DechetCompost extends Dechet {
    
    public DechetCompost(String nom) {
        super(nom);
        categorie = DechetCategorie.COMPOST;
    }
}