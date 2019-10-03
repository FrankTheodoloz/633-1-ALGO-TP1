package domaine;

/**
 * Vous ne devriez pas avoir besoin de modifier cette classe
 */
public class DechetAutre extends Dechet {
    
    public DechetAutre(String nom) {
        super(nom);
        categorie = DechetCategorie.AUTRE;
    }
}