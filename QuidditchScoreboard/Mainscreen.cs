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
using WebSocketSharp; 

namespace QuidditchScoreboard
{
    public partial class Mainscreen : Form
    {
        System.Timers.Timer t;
        int m, s;
        int scoreA;
        int scoreB;

        public static string outputScoreA;
        public static string outputScoreB;
        public static string outputTimer;
        public static string outputExtraTimer;
        public static string Inputfolder;
        public static string Outputfolder;
        public static string penaltlyreasons;
        public static string teamlogos;
        public static string teamroosters;
        public static string cards;

        public static string TeamAName = "Team A";
        public static string TeamBName ="Team B";

       

        public Mainscreen()
        {
            InitializeComponent();
            //Set filepaths
            System.IO.StreamWriter objWriter;
            Inputfolder = @"C:\Input";
            Outputfolder = @"C:\Output";
            outputScoreA = Outputfolder + @"\TeamAScore.txt";
            outputScoreB = Outputfolder + @"\TeamBScore.txt";
            outputTimer = Outputfolder + @"\Timer.txt";
            outputExtraTimer = Outputfolder + @"\ExtraTimer.txt";
            teamlogos = Inputfolder + @"\Teamlogos";
            cards = Inputfolder + @"\Cards";
            teamroosters = Inputfolder + @"\Teamrosters";

            Directory.CreateDirectory(Outputfolder);
            Directory.CreateDirectory(Inputfolder);
            Directory.CreateDirectory(teamlogos);
            Directory.CreateDirectory(cards);
            Directory.CreateDirectory(teamroosters);

            using (objWriter = File.AppendText(outputScoreA))
            using (objWriter = File.AppendText(outputScoreB))
            using (objWriter = File.AppendText(outputTimer))
            using (objWriter = File.AppendText(outputExtraTimer))

             
            //    Directory.CreateDirectory(outputTimer);
            //  Directory.CreateDirectory(outputExtraTimer);
            // Directory.CreateDirectory("my folder");
            objWriter.Close();
        }


        public void UpdateLables()
        {
            label_TeamA.Text = TeamAName;
            label_TeamB.Text = TeamBName;
        }

        #region OpenNewForms
        private void Button_StartTimeKeeper_Click(object sender, EventArgs e)
        {
            Timekeeper Timekeeper1 = new Timekeeper();
            Timekeeper1.Show();
        }

        private void Button_SetPenalty_Click(object sender, EventArgs e)
        {
            Penalty Penalty1 = new Penalty();
            Penalty1.Show();
        }

        private void Button_Settings_Click(object sender, EventArgs e)
        {
            Settings Settings1 = new Settings(this);
            Settings1.Show();
        }

        private void Button_CloseApp_Click(object sender, EventArgs e)
        {
            this.Close();
            t.Stop();
        }
       
      
        private void Button_GetExtraTimer_Click(object sender, EventArgs e)
        {
            ExtraTimer Extra1 = new ExtraTimer();
            Extra1.Show();
        }

        #endregion
       
        private void Mainscreen_Load(object sender, EventArgs e)
        {
            t = new System.Timers.Timer();
            t.Interval = 1000;
            t.Elapsed += OnTimeEvent;
            UpdateLables();

        }

        #region ManualGameTime
        private void OnTimeEvent (object sender, System.Timers.ElapsedEventArgs e)
        {
            UpdateLables();
            Invoke(new Action(() =>
            {
                s += 1;
                if (s==60)
                {
                    s = 0;
                    m += 1;
                }
                if (s>60)
                {
                    s = s-60;
                    m += 1;
                }
              
                textBox_GameTime.Text = string.Format("{0}:{1}", m.ToString().PadLeft(2, '0'), s.ToString().PadLeft(2, '0'));
                UpdateScoreFiles(textBoxScoreTeamA.Text, textBoxScoreTeamB.Text, string.Format("{0}:{1}", m.ToString().PadLeft(2, '0'), s.ToString().PadLeft(2, '0')));
            }));

        }
        private void Button_StartGameTime_Click(object sender, EventArgs e)
        {
            t.Start();
            UpdateScoreFiles(textBoxScoreTeamA.Text, textBoxScoreTeamB.Text, string.Format("{0}:{1}", m.ToString().PadLeft(2, '0'), s.ToString().PadLeft(2, '0')));
        }
        private void Button_StopGameTime_Click(object sender, EventArgs e)
        {
            t.Stop();
            UpdateLables();

          UpdateScoreFiles(textBoxScoreTeamA.Text, textBoxScoreTeamB.Text, string.Format("{0}:{1}", m.ToString().PadLeft(2, '0'), s.ToString().PadLeft(2, '0')));  
        }
        private void Button_SetTimer_Click(object sender, EventArgs e)
        {
            try {
                s = Int32.Parse(textBoxSetSeconds.Text);
                m = Int32.Parse(textBoxSetMinutes.Text);
                textBox_GameTime.Text = string.Format("{0}:{1}", m.ToString().PadLeft(2, '0'), s.ToString().PadLeft(2, '0'));
                UpdateScoreFiles(textBoxScoreTeamA.Text, textBoxScoreTeamB.Text, string.Format("{0}:{1}", m.ToString().PadLeft(2, '0'), s.ToString().PadLeft(2, '0')));
            }
            catch (FormatException)
            {
                MessageBox.Show("Please only use whole numbers as values", "Error in setting the timer",
     MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
        }

        #endregion

        #region ManualScores

        private void UpdateScoreFiles (String ScoreAText, String ScoreBText, string timerText)

            {
             string filenameScoreB = outputScoreB;
            string filenameScoreA = outputScoreA;
             string TimerUp = outputTimer;


        
            System.IO.StreamWriter objWriter2;
            System.IO.StreamWriter objWriter3;
            System.IO.StreamWriter objWriter4;
            objWriter2 = new System.IO.StreamWriter(filenameScoreA);
            objWriter3 = new System.IO.StreamWriter(filenameScoreB);
            objWriter4 = new System.IO.StreamWriter(TimerUp);

            objWriter2.Write(ScoreAText);
            objWriter3.Write(ScoreBText);
            objWriter4.Write(timerText);

            objWriter2.Close();
            objWriter3.Close();
            objWriter4.Close();
            }

        private void ButtonScoreTeamBPlus_Click(object sender, EventArgs e)
        {
            scoreB += 10;
            textBoxScoreTeamB.Text = scoreB.ToString();

           UpdateScoreFiles(textBoxScoreTeamA.Text, textBoxScoreTeamB.Text, string.Format("{0}:{1}", m.ToString().PadLeft(2, '0'), s.ToString().PadLeft(2, '0')));
            
        }
         private void Button_SnitchCatchA_Click(object sender, EventArgs e)
        {
            scoreA += 30;
            textBoxScoreTeamA.Text = scoreA.ToString();
            buttonScoreTeamBMinus.Enabled = false;
            buttonScoreTeamBReset.Enabled = false;
            buttonScoreTeamBPlus.Enabled = false;
            button_SnitchCatchA.Enabled = false;
            button_SnitchCatchB.Enabled = false;
            buttonScoreTeamAMinus.Enabled = false;
            buttonScoreTeamAPlus.Enabled = false;
            buttonScoreTeamAReset.Enabled = false;
            t.Stop();
            button_StartGameTime.Enabled = false;
            button_StopGameTime.Enabled = false;
            button_SetTimer.Enabled = false;
            UpdateScoreFiles(textBoxScoreTeamA.Text, textBoxScoreTeamB.Text, string.Format("{0}:{1}", m.ToString().PadLeft(2, '0'), s.ToString().PadLeft(2, '0')));
        }


        private void Button_SnitchCatchB_Click(object sender, EventArgs e)
        {
            scoreB += 30;
            textBoxScoreTeamB.Text = scoreB.ToString();
            buttonScoreTeamBMinus.Enabled = false;
            buttonScoreTeamBReset.Enabled = false;
            buttonScoreTeamBPlus.Enabled = false;
            button_SnitchCatchA.Enabled = false;
            button_SnitchCatchB.Enabled = false;
            buttonScoreTeamAMinus.Enabled = false;
            buttonScoreTeamAPlus.Enabled = false;
            buttonScoreTeamAReset.Enabled = false;
            t.Stop();
            button_StartGameTime.Enabled = false;
            button_StopGameTime.Enabled = false;
            button_SetTimer.Enabled = false;
             UpdateScoreFiles(textBoxScoreTeamA.Text, textBoxScoreTeamB.Text, string.Format("{0}:{1}", m.ToString().PadLeft(2, '0'), s.ToString().PadLeft(2, '0')));
        }

        private void ButtonScoreTeamBReset_Click(object sender, EventArgs e)
        {
            scoreB = 0;
            textBoxScoreTeamB.Text = scoreB.ToString();
             UpdateScoreFiles(textBoxScoreTeamA.Text, textBoxScoreTeamB.Text, string.Format("{0}:{1}", m.ToString().PadLeft(2, '0'), s.ToString().PadLeft(2, '0')));
        }

        private void ButtonScoreTeamBMinus_Click(object sender, EventArgs e)
        {
            scoreB -= 10;
            textBoxScoreTeamB.Text = scoreB.ToString();
             UpdateScoreFiles(textBoxScoreTeamA.Text, textBoxScoreTeamB.Text, string.Format("{0}:{1}", m.ToString().PadLeft(2, '0'), s.ToString().PadLeft(2, '0')));
        }
        private void buttonScoreTeamAReset_Click(object sender, EventArgs e)
        {
            scoreA = 0;
            textBoxScoreTeamA.Text = scoreA.ToString();
           UpdateScoreFiles(textBoxScoreTeamA.Text, textBoxScoreTeamB.Text, string.Format("{0}:{1}", m.ToString().PadLeft(2, '0'), s.ToString().PadLeft(2, '0')));
        }

        private void buttonScoreTeamAMinus_Click(object sender, EventArgs e)
        {
            scoreA -= 10;
            textBoxScoreTeamA.Text = scoreA.ToString();
            UpdateScoreFiles(textBoxScoreTeamA.Text, textBoxScoreTeamB.Text, string.Format("{0}:{1}", m.ToString().PadLeft(2, '0'), s.ToString().PadLeft(2, '0')));
        }

        private void Button_StartNewGame_Click(object sender, EventArgs e)
        {
            buttonScoreTeamBMinus.Enabled = true;
            buttonScoreTeamBReset.Enabled = true;
            buttonScoreTeamBPlus.Enabled = true;
            button_SnitchCatchA.Enabled = true;
            button_SnitchCatchB.Enabled = true;
            buttonScoreTeamAMinus.Enabled = true;
            buttonScoreTeamAPlus.Enabled = true;
            buttonScoreTeamAReset.Enabled = true;
            t.Stop();
            button_StartGameTime.Enabled = true;
            button_StopGameTime.Enabled = true;
            button_SetTimer.Enabled = true;
            m = 0;
            s = 0;
            textBox_GameTime.Text = string.Format("{0}:{1}", m.ToString().PadLeft(2, '0'), s.ToString().PadLeft(2, '0'));
            scoreA = 0;
            scoreB = 0;
            textBoxScoreTeamA.Text = scoreA.ToString();
            textBoxScoreTeamB.Text = scoreB.ToString();

            UpdateScoreFiles(textBoxScoreTeamA.Text, textBoxScoreTeamB.Text, string.Format("{0}:{1}", m.ToString().PadLeft(2, '0'), s.ToString().PadLeft(2, '0')));
            UpdateLables();
        }

     

        private void buttonScoreTeamAPlus_Click(object sender, EventArgs e)
        {
            scoreA += 10;
            textBoxScoreTeamA.Text = scoreA.ToString();
            UpdateScoreFiles(textBoxScoreTeamA.Text, textBoxScoreTeamB.Text, string.Format("{0}:{1}", m.ToString().PadLeft(2, '0'), s.ToString().PadLeft(2, '0')));
        }

        #endregion
       
       
    }
}
