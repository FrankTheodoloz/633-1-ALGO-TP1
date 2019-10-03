package domaine;

/**
 * Vous ne devriez pas avoir besoin de modifier cette classe
 */
public class DechetVerre extends Dechet {
    
    public DechetVerre(String nom) {
        super(nom);
        categorie = DechetCategorie.VERRE;
    }
}