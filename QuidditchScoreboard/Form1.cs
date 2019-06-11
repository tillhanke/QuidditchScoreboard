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
    public partial class OutputPaths : Form
    {
        public OutputPaths()
        {
            InitializeComponent();
        }

        private void Button_CancelOutput_Click(object sender, EventArgs e)
        {
            this.Close();
        }

        private void TextBox1_TextChanged(object sender, EventArgs e)
        {

        }

        private void Button_OKOutput_Click(object sender, EventArgs e)
        {
            this.button_OKOutput.DialogResult = System.Windows.Forms.DialogResult.OK;
        }

        private void TextBox_InputPaths_TextChanged(object sender, EventArgs e)
        {

        }
    }
}
