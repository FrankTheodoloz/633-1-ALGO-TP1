package vue;

import domaine.Dechet;
import domaine.DechetCategorie;
import metier.ListeDechets;

import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class FrmTri extends JFrame {
    private JPanel pnl;
    private JToggleButton jtbStart;
    private JButton jbReset;
    private JLabel lblItem;
    private JLabel lblInfo;
    private JButton jbCompost;
    private JButton jbVerre;
    private JButton jbPET;
    private JButton jbMetal;
    private JButton jbPapier;
    private JButton jbAutres;
    private JTable tblDechets;
    private JTextField jtFile;
    private JCheckBox chbSkipErrors;
    private JLabel lblStats;
    private JLabel lblNumbers;

    private enum TriStatus{INIT,READY,PLAYING,TERMINATED};

    private static final String CLICK_START = "Cliquez sur Start";
    private static final String MS          = "ms";
    private static final String TEMPS_REAC  = "Temps de réaction moyen: ";
    private static final String ERREURS     = ", Erreurs : ";
    private static final String RESTANTS    = ", Restants : ";
    private static final String TRAITE      = "Traités : ";
    private static final String START       = "Start";
    private static final String STOP        = "Stop";
    private static final String BRAVO       = "Bravo!";
    private static final String RATE        = "Raté!";
    private static final String TERMINE     = "Félicitations, vous avez terminé!";

    /**
     * La liste de tous les Dechet (classés et à classer)
     */
    private ListeDechets<Dechet> listeDechetsGlobale;

    /**
     * L'instance de Dechet affiché pour classement.
     */
    private Dechet item;

    int success_counter = 0;
    int fail_counter = 0;
    long reaction_time = 0;
    long start_time = System.currentTimeMillis();

    /**
     * Creates new form FrmTri
     */
    public FrmTri() {
        initComponents();
        setStatus(TriStatus.INIT);
    }

    private void initComponents() {
        setContentPane(pnl); pack();
        setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE);
        setTitle("Apprenez à trier les déchets");
        setLocationRelativeTo(null);
        jtFile.addActionListener(new ActionListener() { @Override public void actionPerformed(ActionEvent e) { jtFileActionPerformed(e); } });
        jtbStart.addActionListener(new ActionListener() { @Override public void actionPerformed(ActionEvent e) { jtbStartActionPerformed(e); } });
        jbReset.addActionListener(new ActionListener() { @Override public void actionPerformed(ActionEvent e) { jbResetActionPerformed(e); } });
        jbCompost.addActionListener(new ActionListener() { @Override public void actionPerformed(ActionEvent e) { jbCompostActionPerformed(e); } });
        jbVerre.addActionListener(new ActionListener() { @Override public void actionPerformed(ActionEvent e) { jbVerreActionPerformed(e); } });
        jbPET.addActionListener(new ActionListener() { @Override public void actionPerformed(ActionEvent e) { jbPETActionPerformed(e); } });
        jbMetal.addActionListener(new ActionListener() { @Override public void actionPerformed(ActionEvent e) { jbMetalActionPerformed(e); } });
        jbPapier.addActionListener(new ActionListener() { @Override public void actionPerformed(ActionEvent e) { jbPapierActionPerformed(e); } });
        jbAutres.addActionListener(new ActionListener() { @Override public void actionPerformed(ActionEvent e) { jbAutresActionPerformed(e); } });
    }

    /**
     * Appelle le chargement du fichier.
     * @param evt 
     */
    private void jtFileActionPerformed(java.awt.event.ActionEvent evt) {
        /** A COMPLETER **/
    }

    /**
     * Un clic sur un des boutons "DechetCategorie" doit mettre l'item affiché
     * dans la bonne catégorie.
     * @param dc
     */
    private void gereClicSurBoutonClassement(DechetCategorie dc) {
        /** A COMPLETER **/
    }

    /**
     * Affiche un Dechet au hasard (parmi les Dechet restants NONCATEGORISE)
     */
    private void displayRandomItem() {
        /** A COMPLETER **/
    }

    private void displayCounterAndStat() {
        lblNumbers.setText(TRAITE + (success_counter+fail_counter) +
                RESTANTS + (listeDechetsGlobale.getNbRestants()) +
                ERREURS + fail_counter);
        lblStats.setText(TEMPS_REAC + ((success_counter+fail_counter)==0 ? "0" : (reaction_time/(success_counter+fail_counter))) + MS);
    }

    /**
     * Modifie le statut des éléments d'interface (boutons, labels)
     * conformément aux spécifications en fonction du TriStatus
     * @param ts
     */
    private void setStatus(TriStatus ts) {
        switch(ts) {
            case INIT:
                jtbStart.setEnabled(false);
                enableBtnClassement(false);
                jbReset.setEnabled(false);
                break;
            case READY:
                jtbStart.setText(START);
                jtbStart.setEnabled(true);
                enableBtnClassement(false);
                jbReset.setEnabled(true);
                lblItem.setText(CLICK_START);
                break;
            case PLAYING:
                jtbStart.setText(STOP);
                jbReset.setEnabled(false);
                enableBtnClassement(true);
                displayRandomItem();
                break;
            case TERMINATED:
                jtbStart.setText(START);
                jtbStart.setEnabled(false);
                enableBtnClassement(false);
                jbReset.setEnabled(true);
                lblItem.setText(TERMINE);
                break;
        }
    }

    /**
     * Active/desactive les boutons de classement
     * @param ok = true pour activer / false pour desactiver
     */
    private void enableBtnClassement(boolean ok) {
        jbMetal.setEnabled(ok);
        jbAutres.setEnabled(ok);
        jbCompost.setEnabled(ok);
        jbPET.setEnabled(ok);
        jbPapier.setEnabled(ok);
        jbVerre.setEnabled(ok);
    }

    private void jtbStartActionPerformed(java.awt.event.ActionEvent evt) {
        /** A COMPLETER **/
    }

    /**
     * Effectue une réinitialisation du jeu. Tous les déchets sont à nouveau
     * "non catégorisé" et les statistiques sont remises à zéro.
     * @param evt
     */
    private void jbResetActionPerformed(java.awt.event.ActionEvent evt) {
        /** A COMPLETER **/
    }

    /**
     * Boutons de classement dans les différentes catégories.
     * @param evt
     */
    private void jbPETActionPerformed(java.awt.event.ActionEvent evt) {
        /** A COMPLETER **/
    }
    private void jbCompostActionPerformed(java.awt.event.ActionEvent evt) {
        /** A COMPLETER **/
    }
    private void jbPapierActionPerformed(java.awt.event.ActionEvent evt) {
        /** A COMPLETER **/
    }
    private void jbVerreActionPerformed(java.awt.event.ActionEvent evt) {
        /** A COMPLETER **/
    }
    private void jbMetalActionPerformed(java.awt.event.ActionEvent evt) {
        /** A COMPLETER **/
    }
    private void jbAutresActionPerformed(java.awt.event.ActionEvent evt) {
        /** A COMPLETER **/
    }
}
