package domaine;

/**
 * Superclass de tous les Dechets. 
 * Vous ne devriez pas avoir besoin de modifier cette classe.
 */
public abstract class Dechet {
    protected DechetCategorie categorie; 
    protected String nom;
    
    protected Dechet(String nom) {
        this.nom = nom;
    }
    
    public DechetCategorie getCategorie() {
        return categorie;
    };
    
    @Override
    public String toString() {
        return nom;
    }
    @Override
    public boolean equals(Object o) {
        Dechet d = (Dechet)o;
        return d.nom.equals(nom) && d.categorie.equals(categorie);
    }
    }
}
