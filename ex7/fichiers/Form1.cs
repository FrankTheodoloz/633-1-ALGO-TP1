using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace WindowsFormsApp1
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            Form2 form = new Form2();
            if (form.ShowDialog() == DialogResult.OK) {
                listBox1.Items.Add(form.GetCours());
            }
        }

        private void Annuler_Click(object sender, EventArgs e)
        {
            Close(;
        }

        private void listBox1_SelectedIndexChanged(object sender, EventArgs e)
        {
            Form3 form = new Form3();
            form.SetCours(listBox1.SelectedItem.ToString());
            form.Text = listBox1.SelectedItem.ToString();
            form.MdiParent = this.MdiParent;
            form.Show();
        }
    }
}
