import java.util.ArrayList;

public class Ecole {

  private ArrayList<Personne> personnes;

  public Ecole() {
    personnes.add(new Personne("Stettler", "Christian"));
    personnes.add(new Personne("Douglas", "Teodoro"));
    personnes.add(new Personne("Soukouti", "Nader"));
  }

  public ArrayList<Personne> getPersonnes()
    return personnes;
  }

  public void setPersonnes(ArrayList<Personne> personnes) {
    this.personnes = personnes;
  }

  @Override
  public boolean equals(Object o) {
    Ecole other = (Ecole)o;
    return other.personnes.equals(this.personnes);
  }

  @Override
  public int hashCode() {
    return personnes.hashCode();
  }
}
