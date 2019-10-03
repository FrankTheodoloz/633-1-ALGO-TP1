package dao;

import domaine.*;
import java.util.ArrayList;

/**
 * Classe DAO, permettant de charger le contenu d'un fichier spécifié en paramètre
 * en sautant optionnellement les erreurs de données
 * 
 * @author _____VOTRE_NOM_____
 */
public class DechetsDao {
       
    /**
     * Chargement des déchets. 
     * La signature de cette méthode peut être modifiée si vous en avez besoin.
     * @param filename Le nom du fichier à charger.
     * @param skiperrors = true si le chargement doit continuer même si une 
     * ligne n'est pas correctement formatée ou contient des informations 
     * incorrectes.
     * @return La liste de Dechet
     */
    public static ArrayList<Dechet> chargerDechets(String filename, boolean skiperrors) {
        return null;
    }

}