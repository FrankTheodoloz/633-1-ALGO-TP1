package domaine;

/**
 * Vous ne devriez pas avoir besoin de modifier cette classe
 */
public class DechetPapier extends Dechet {
    
    public DechetPapier(String nom) {
        super(nom);
        categorie = DechetCategorie.PAPIER;
    }
}