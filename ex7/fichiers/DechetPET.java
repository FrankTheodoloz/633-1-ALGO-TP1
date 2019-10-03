package domaine;

/**
 * Vous ne devriez pas avoir besoin de modifier cette classe
 */
public class DechetPET extends Dechet {
    
    public DechetPET(String nom) {
        super(nom);
        categorie = DechetCategorie.PET;
    }
}