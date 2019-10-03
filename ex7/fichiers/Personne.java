public class Personne {

  private String nom;
  private String prenom;

  public Personne(String nom, String prenom) {
    this.nom = nom;
    this.prenom = prenom;
  }

  public String getNom() {
    return nom;
  }

  public void setNom(String nom) {
    this.nom = nom;
  }

  public String getPrenom() {
    return prenom;
  }

  public void setPrenom(String prenom) {
    this.prenom = prenom;
  }

  @Override
  public boolean equals(Object o) {
    Personne other = (Personne)o;
    return (other.prenom.equals(prenom) && other.nom.equals(nom));
  }

  @Override
  public int hashCode() {
    return nom.hashCode() * prenom.hashCode();
  }


}
