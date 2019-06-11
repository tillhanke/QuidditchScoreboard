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
    public partial class Timekeeper : Form
    {
        public Timekeeper()
        {
            InitializeComponent();
        }


        private void Button_CloseTimekeeper_Click(object sender, EventArgs e)
        {
            this.Close();
        }

        private void Button_TimekeeperConnect_Click(object sender, EventArgs e)
        {

        }
    }
}
