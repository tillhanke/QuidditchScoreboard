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
    public partial class ExtraTimer : Form
    {
        public ExtraTimer()
        {
            InitializeComponent();
        }
       

        System.Timers.Timer t2;
        int m2, s2;
        


        private void TextBox_TimerLabel_TextChanged(object sender, EventArgs e)
        {

        }

        private void Button_ExtraTimerStart_Click(object sender, EventArgs e)
        {
            t2.Start();
            UpdateTimerFiles(string.Format("{0}:{1}", m2.ToString().PadLeft(2, '0'), s2.ToString().PadLeft(2, '0')));

        }

        private void Button_ExtraTimerStop_Click(object sender, EventArgs e)
        {
            t2.Stop();
            UpdateTimerFiles(string.Format("{0}:{1}", m2.ToString().PadLeft(2, '0'), s2.ToString().PadLeft(2, '0')));
        }

        private void Button_ExtraTimerSet_Click(object sender, EventArgs e)
        {
            try
            {
                s2 = Int32.Parse(textBox_ExtraTimerSec.Text);
                m2 = Int32.Parse(textBox_ExtraTimerMin.Text);
                textBox_ExtraTimer.Text = string.Format("{0}:{1}", m2.ToString().PadLeft(2, '0'), s2.ToString().PadLeft(2, '0'));
                UpdateTimerFiles(string.Format("{0}:{1}", m2.ToString().PadLeft(2, '0'), s2.ToString().PadLeft(2, '0')));
            }
            catch (FormatException)
            {
                MessageBox.Show("Please only use whole numbers as values", "Error in setting the timer",
     MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
        }

        private void ExtraTimer_Load(object sender, EventArgs e)
        {
            t2 = new System.Timers.Timer();
            t2.Interval = 1000;
            t2.Elapsed += OnTimeEvent;
           

        }

        private void OnTimeEvent(object sender, System.Timers.ElapsedEventArgs e)
        {
            if (radioButton_ExtraTimerForw.Checked)
            {
                Invoke(new Action(() =>
                {
                    s2 += 1;
                    if (s2 == 60)
                    {
                        s2 = 0;
                        m2 += 1;
                    }
                    if (s2 > 60)
                    {
                        s2 = s2 - 60;
                        m2 += 1;
                    }

                    textBox_ExtraTimer.Text = string.Format("{0}:{1}", m2.ToString().PadLeft(2, '0'), s2.ToString().PadLeft(2, '0'));
                    UpdateTimerFiles(string.Format("{0}:{1}", m2.ToString().PadLeft(2, '0'), s2.ToString().PadLeft(2, '0')));
                }));

            }
            else if (radioButton_ExtraTimerBack.Checked)
            {
                Invoke(new Action(() =>
                {
                    s2 -= 1;
                    if (m2 <= 0 && s2 <= 0)
                    {
                        t2.Stop();
                        m2 = 0;
                        s2 = 0;

                        textBox_ExtraTimer.Text = string.Format("{0}:{1}", m2.ToString().PadLeft(2, '0'), s2.ToString().PadLeft(2, '0'));
                        UpdateTimerFiles(string.Format("{0}:{1}", m2.ToString().PadLeft(2, '0'), s2.ToString().PadLeft(2, '0')));

                    }
                    if (s2 == 0 && m2 != 0)
                    {
                        s2 = 60;
                        m2 -= 1;

                    }
                   

                    textBox_ExtraTimer.Text = string.Format("{0}:{1}", m2.ToString().PadLeft(2, '0'), s2.ToString().PadLeft(2, '0'));
                    UpdateTimerFiles(string.Format("{0}:{1}", m2.ToString().PadLeft(2, '0'), s2.ToString().PadLeft(2, '0')));
                }));

            }

        }
        
       

        
        private void Button_CloseExtraTimer_Click(object sender, EventArgs e)
        {
            t2.Stop();
            this.Close();
            
        }

        private void UpdateTimerFiles(string timerText)

        {
            string TimerDown = Mainscreen.outputExtraTimer;
            System.IO.StreamWriter objWriter;
            objWriter = new System.IO.StreamWriter(TimerDown);

            objWriter.Write(timerText);

            objWriter.Close();
        }
    }
}
