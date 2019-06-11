using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.IO;

namespace QuidditchScoreboard
{
    public partial class Settings : Form
    {
        public Settings()
        {
            InitializeComponent();
        }
        string filePathOut;
        string filePathIn;
     
        private void Button_CloseSettings_Click(object sender, EventArgs e)
        {
            this.Close();
        }

        public void ShowMyDialogBox()
        {
            OutputPaths testDialog = new OutputPaths();

            // Show testDialog as a modal dialog and determine if DialogResult = OK.
            if (testDialog.ShowDialog(this) == DialogResult.OK)
            {
                // Read the contents of testDialog's TextBox.
                filePathOut = @"" + testDialog.textBox_OutputPaths.Text;
                filePathIn = @"" + testDialog.textBox_InputPaths.Text;
            }         
            else 
            {
                filePathOut = @"C:\";
                filePathIn = @"C:\";
            }
            testDialog.Dispose();
        }
        public static string outputScoreA;
        public static string outputScoreB;
        public static string outputTimer;
        public static string outputExtraTimer;

        public static string penaltlyreasons;
        public static string teamlogos;
        public static string teamroosters;

        public static string TeamAName;
        public static string TeamBName;


        private void Button_GetOutputPath_Click(object sender, EventArgs e)
        {
            ShowMyDialogBox();
            try
            {
                string[] lines = File.ReadAllLines(filePathOut);
                outputScoreA = lines[0];
                outputScoreB = lines[1];
                outputTimer = lines[2];
                outputExtraTimer = lines[3];
            }
             
            catch (Exception)
            {
                MessageBox.Show("The path is missing", "Error in setting output path",
    MessageBoxButtons.OK, MessageBoxIcon.Error);
            }

            try
            {
                string[] lines = File.ReadAllLines(filePathIn);
                penaltlyreasons = lines[0];
                teamlogos = lines[1];
                teamroosters = lines[2];
             
            }

            catch (Exception)
            {
                MessageBox.Show("The path is missing", "Error in setting input path",
    MessageBoxButtons.OK, MessageBoxIcon.Error);
            }

        }

        string filepathB = @"C:\Users\media markt\source\repos\QuidditchScoreboard\RealScoreBoard\RealScoreBoard\Input\ListofTeams.txt";
        string filepath = @"C:\Users\media markt\source\repos\QuidditchScoreboard\RealScoreBoard\RealScoreBoard\Input\ListofTeams.txt";
        private void Settings_Load(object sender, EventArgs e)
        {
            try
            {
                string[] lines = File.ReadAllLines(filepath);
                foreach (string line in lines )
                {
                    comboBox_TeamAName.Items.Add(line);
                }
                
            }

            catch (Exception)
            {
                MessageBox.Show("The path is missing", "Error in setting path",
    MessageBoxButtons.OK, MessageBoxIcon.Error);
            }

            try
            {
                string[] lines2 = File.ReadAllLines(filepathB);
                foreach (string line2 in lines2)
                {
                    comboBox_TeamBName.Items.Add(line2);
                }

            }

            catch (Exception)
            {
                MessageBox.Show("The path is missing", "Error in setting path",
    MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
        }

        private void Button_SaveSettings_Click(object sender, EventArgs e)
        {
            TeamAName = comboBox_TeamAName.SelectedItem.ToString();
            TeamBName = comboBox_TeamBName.SelectedItem.ToString();
                     
        }
    }
}
