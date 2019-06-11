using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace QuidditchScoreboard
{
    public partial class SnitchCatch : Form
    {
        public SnitchCatch()
        {
            InitializeComponent();
        }

         public int ScoreA
        {
            get;
            set;
        }
        public int ScoreB
        {
            get;
            set;
        }

       
        private void ButtonCancelSnitch_Click(object sender, EventArgs e)
        {
            this.Close();
        }

        private void ButtonOKSnitch_Click(object sender, EventArgs e)
        {
            if (radioButton_SnitchTeamA.Checked)
            {
                ScoreA = ScoreA + 30;
                                 
           }
            if (radioButtonSnitchTeamB.Checked)
            {
                ScoreB = ScoreB + 30;
            }
            this.Close();
        }
    }
}
