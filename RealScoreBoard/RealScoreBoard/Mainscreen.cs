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
    public partial class Mainscreen : Form
    {
        System.Timers.Timer t;
        int m, s;
        int scoreA;
        int scoreB;

        public Mainscreen()
        {
            InitializeComponent();
                      
        }
          string filenameScoreB ="C:\\Users\\media markt\\source\\repos\\QuidditchScoreboard\\QuidditchScoreboard\\Output\\ScoreB.txt";
          string filenameScoreA ="C:\\Users\\media markt\\source\\repos\\QuidditchScoreboard\\QuidditchScoreboard\\Output\\ScoreA.txt";
        string TimerUp ="C:\\Users\\media markt\\source\\repos\\QuidditchScoreboard\\QuidditchScoreboard\\Output\\timer_up.txt";


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
            Settings Settings1 = new Settings();
            Settings1.Show();
        }

        private void Button_CloseApp_Click(object sender, EventArgs e)
        {
            this.Close();
            t.Stop();
        }
       
       private void Button_GetExtaTimer_Click(object sender, EventArgs e)
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
        }

        #region ManualGameTime
        private void OnTimeEvent (object sender, System.Timers.ElapsedEventArgs e)
        {
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
            System.IO.StreamWriter objWriter;
            System.IO.StreamWriter objWriter2;
            System.IO.StreamWriter objWriter3;
            objWriter = new System.IO.StreamWriter(filenameScoreA);
            objWriter2 = new System.IO.StreamWriter(filenameScoreB);
            objWriter3 = new System.IO.StreamWriter(TimerUp);

            objWriter.Write(ScoreAText);
            objWriter2.Write(ScoreBText);
            objWriter3.Write(timerText);

            objWriter.Close();
            objWriter2.Close();
            objWriter3.Close();
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
