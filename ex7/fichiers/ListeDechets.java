package metier;

import domaine.Dechet;
import domaine.DechetCategorie;
import exceptions.DechetMisMatchException;
import java.util.ArrayList;
import java.util.HashMap;
import javax.swing.table.AbstractTableModel;

/**
 * Classe métier stockant les instances de Dechet dans la bonne catégorie. 
 * 
 * Toutes les méthodes de cette classe sont potentiellement à compléter.
 * Vous pouvez créer des méthodes supplémentaires si nécessaire.
 * 
 * @author ____VOTRE_NOM____  !!! à compléter !!!
 * @param <T>
 */
public class ListeDechets<T extends Dechet> extends AbstractTableModel {
    /** 
     * Structure de données que vous devez impérativement utiliser 
     **/
    private HashMap<DechetCategorie,ArrayList<T>> dechets;
    
    /**
     * Constructeur. Remplit la liste des dechets avec le contenu du fichier.
     * Vous pouvez modifier la signature du constructeur.
     * Tous les Dechet sont mis par défaut dans la catégorie NONCATEGORISE
     */
    public ListeDechets() {
    }
    
    /**
     * Remet les données dans l'état initial, (comme juste après chargement
     * du fichier), mais sans recharger(relire) les données depuis DechetsDao.
     */
    public void reset() {
    }

    /**
     * Déplace l'item depuis la liste des non-catégorisés vers la catégorie passée
     * en paramètre, pour autant que la catégorie passée en paramètre corresponde
     * à la catégorie de l'item.
     * @param item Dechet à déplacer (si dc est correcte)
     * @param dc nouvelle DechetCategorie de rangement (au lieu de NONCATEGORISE)
     * @throws exceptions.DechetMisMatchException si la DechetCategorie de 
     * <code>item</code> n'est pas la même que <code>dc</code>
     */
    public void classe(T item, DechetCategorie dc) throws DechetMisMatchException {
    }
    
    /**
     * @return Un item au hasard pris dans la liste des non-catégorisés. 
     * Si la  liste est vide, retourne null.
     */
    public T getRandom() {
        return null;
    }

    {
    /**
     * @param max Borne maximale (plus grande valeur).
     * @return Un nombre entier au hasard entre 0 et max-1.
     */
    private int random(int max) {
        return (int)Math.floor(max*Math.random());
    }

    /**
     * @return Le nombre d'item restants à classer.
     */
    public int getNbRestants() {
        return 0;
    }
    
    @Override
    public int getRowCount() {
        return 0;
    }

    @Override
    public int getColumnCount() {
        return 0;
    }

    @Override
    public String getColumnName(int columnIndex) {
        return null;
    }

    @Override
    /**
     * @return le contenu de la cellule à l'index <code>rowIndex</code> et 
     * à la colonne <code>columnIndex</code> dans le tableau principal.
     */
    public Object getValueAt(int rowIndex, int columnIndex) {
        return null;
    }
}
