package domaine;

/**
 * Vous ne devriez pas avoir besoin de modifier cette classe
 */
public class DechetMetal extends Dechet {
    
    public DechetMetal(String nom) {
        super(nom);
        categorie = DechetCategorie.METAL;
    }
}