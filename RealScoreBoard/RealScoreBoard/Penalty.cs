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
    public partial class Penalty : Form
    {
        public Penalty()
        {
            InitializeComponent();
        }

   

        private void Button_CancelPenalty_Click(object sender, EventArgs e)
        {
            this.Close();
        }
    }
}
