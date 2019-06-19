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
        private Form mainscreen;
        public Settings(Form mainscreen)
        {
            InitializeComponent();
            this.mainscreen = mainscreen;
        }


        private void Button_CloseSettings_Click(object sender, EventArgs e)
        {
            this.Close();
        }

        private void Button_GetOutputPath_Click(object sender, EventArgs e)
        {
            /**  ShowMyDialogBox();
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
   **/
        }
        private static DirectoryInfo d = new DirectoryInfo(Mainscreen.teamlogos);
        FileInfo[] Files = d.GetFiles("*.png"); //Getting png files

        private static DirectoryInfo d2 = new DirectoryInfo(Mainscreen.teamlogos);
        FileInfo[] Files2 = d2.GetFiles("*.png"); //Getting png files
                                                //  string filenames4 = Directory.EnumerateFiles(Mainscreen.teamlogos, "*", SearchOption.AllDirectories).Select(Path.GetFileName); // <-- note you can shorten the lambda

        private void Settings_Load(object sender, EventArgs e)
        {
            try
            {
                comboBox_TeamAName.DataSource = Files;
                comboBox_TeamAName.DisplayMember = "Name";


                comboBox_TeamBName.DataSource = Files2;
                comboBox_TeamBName.DisplayMember = "Name";
                /**  string[] lines = File.ReadAllLines(filepath);
                  foreach (string line in lines )
                  {
                      comboBox_TeamAName.Items.Add(line);
                  }
                  */
            }

            catch (Exception)
            {
                MessageBox.Show("No team names found", "No team names",
    MessageBoxButtons.OK, MessageBoxIcon.Error);
            }

           
        }

        private void Button_SaveSettings_Click(object sender, EventArgs e)
        {
            Mainscreen.TeamAName = comboBox_TeamAName.SelectedItem.ToString();
            Mainscreen.TeamBName = comboBox_TeamBName.SelectedItem.ToString();
        ;
        }

        private void ButtonSwapTeams_Click(object sender, EventArgs e)
        {
            string ATemp = Mainscreen.TeamAName;
            string BTemp = Mainscreen.TeamBName;
            Mainscreen.TeamAName = BTemp;
            Mainscreen.TeamBName = ATemp;
            
            comboBox_TeamAName.SelectedItem = comboBox_TeamAName.FindStringExact(BTemp);
            comboBox_TeamBName.SelectedItem = comboBox_TeamBName.FindStringExact(ATemp);

        }
    }
}
