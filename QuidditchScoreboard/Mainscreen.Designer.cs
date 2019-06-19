namespace QuidditchScoreboard
{
    partial class Mainscreen
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.label1 = new System.Windows.Forms.Label();
            this.textBox_GameTime = new System.Windows.Forms.TextBox();
            this.button_StartGameTime = new System.Windows.Forms.Button();
            this.button_StopGameTime = new System.Windows.Forms.Button();
            this.button_SetTimer = new System.Windows.Forms.Button();
            this.button_GetExtraTimer = new System.Windows.Forms.Button();
            this.label2 = new System.Windows.Forms.Label();
            this.label_TeamA = new System.Windows.Forms.Label();
            this.label_TeamB = new System.Windows.Forms.Label();
            this.buttonScoreTeamAPlus = new System.Windows.Forms.Button();
            this.buttonScoreTeamAReset = new System.Windows.Forms.Button();
            this.buttonScoreTeamAMinus = new System.Windows.Forms.Button();
            this.buttonScoreTeamBPlus = new System.Windows.Forms.Button();
            this.buttonScoreTeamBReset = new System.Windows.Forms.Button();
            this.buttonScoreTeamBMinus = new System.Windows.Forms.Button();
            this.button_SnitchCatchA = new System.Windows.Forms.Button();
            this.button_Settings = new System.Windows.Forms.Button();
            this.button_StartTimeKeeper = new System.Windows.Forms.Button();
            this.button_SetPenalty = new System.Windows.Forms.Button();
            this.button_CloseApp = new System.Windows.Forms.Button();
            this.textBoxSetMinutes = new System.Windows.Forms.TextBox();
            this.textBoxScoreTeamA = new System.Windows.Forms.TextBox();
            this.textBoxScoreTeamB = new System.Windows.Forms.TextBox();
            this.textBoxSetSeconds = new System.Windows.Forms.TextBox();
            this.button_SnitchCatchB = new System.Windows.Forms.Button();
            this.button_StartNewGame = new System.Windows.Forms.Button();
            this.SuspendLayout();
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(366, 36);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(61, 13);
            this.label1.TabIndex = 0;
            this.label1.Text = "Game Time";
            // 
            // textBox_GameTime
            // 
            this.textBox_GameTime.Font = new System.Drawing.Font("Microsoft Sans Serif", 15.75F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.textBox_GameTime.Location = new System.Drawing.Point(312, 67);
            this.textBox_GameTime.Name = "textBox_GameTime";
            this.textBox_GameTime.ReadOnly = true;
            this.textBox_GameTime.Size = new System.Drawing.Size(147, 31);
            this.textBox_GameTime.TabIndex = 1;
            this.textBox_GameTime.Text = "00:00";
            this.textBox_GameTime.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            // 
            // button_StartGameTime
            // 
            this.button_StartGameTime.Location = new System.Drawing.Point(173, 114);
            this.button_StartGameTime.Name = "button_StartGameTime";
            this.button_StartGameTime.Size = new System.Drawing.Size(75, 23);
            this.button_StartGameTime.TabIndex = 2;
            this.button_StartGameTime.Text = "Start";
            this.button_StartGameTime.UseVisualStyleBackColor = true;
            this.button_StartGameTime.Click += new System.EventHandler(this.Button_StartGameTime_Click);
            // 
            // button_StopGameTime
            // 
            this.button_StopGameTime.Location = new System.Drawing.Point(332, 113);
            this.button_StopGameTime.Name = "button_StopGameTime";
            this.button_StopGameTime.Size = new System.Drawing.Size(75, 23);
            this.button_StopGameTime.TabIndex = 3;
            this.button_StopGameTime.Text = "Stop";
            this.button_StopGameTime.UseVisualStyleBackColor = true;
            this.button_StopGameTime.UseWaitCursor = true;
            this.button_StopGameTime.Click += new System.EventHandler(this.Button_StopGameTime_Click);
            // 
            // button_SetTimer
            // 
            this.button_SetTimer.Location = new System.Drawing.Point(501, 104);
            this.button_SetTimer.Name = "button_SetTimer";
            this.button_SetTimer.Size = new System.Drawing.Size(75, 23);
            this.button_SetTimer.TabIndex = 4;
            this.button_SetTimer.Text = "Set";
            this.button_SetTimer.UseVisualStyleBackColor = true;
            this.button_SetTimer.Click += new System.EventHandler(this.Button_SetTimer_Click);
            // 
            // button_GetExtraTimer
            // 
            this.button_GetExtraTimer.Location = new System.Drawing.Point(294, 159);
            this.button_GetExtraTimer.Name = "button_GetExtraTimer";
            this.button_GetExtraTimer.Size = new System.Drawing.Size(185, 23);
            this.button_GetExtraTimer.TabIndex = 6;
            this.button_GetExtraTimer.Text = "Get Extra Timer";
            this.button_GetExtraTimer.UseVisualStyleBackColor = true;
            this.button_GetExtraTimer.Click += new System.EventHandler(this.Button_GetExtraTimer_Click);
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(369, 215);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(40, 13);
            this.label2.TabIndex = 7;
            this.label2.Text = "Scores";
            // 
            // label_TeamA
            // 
            this.label_TeamA.AutoSize = true;
            this.label_TeamA.Location = new System.Drawing.Point(114, 261);
            this.label_TeamA.Name = "label_TeamA";
            this.label_TeamA.Size = new System.Drawing.Size(44, 13);
            this.label_TeamA.TabIndex = 8;
            this.label_TeamA.Text = "Team A";

            // 
            // label_TeamB
            // 
            this.label_TeamB.AutoSize = true;
            this.label_TeamB.Location = new System.Drawing.Point(565, 260);
            this.label_TeamB.Name = "label_TeamB";
            this.label_TeamB.Size = new System.Drawing.Size(44, 13);
            this.label_TeamB.TabIndex = 9;
            this.label_TeamB.Text = "Team B";
            // 
            // buttonScoreTeamAPlus
            // 
            this.buttonScoreTeamAPlus.Location = new System.Drawing.Point(173, 234);
            this.buttonScoreTeamAPlus.Name = "buttonScoreTeamAPlus";
            this.buttonScoreTeamAPlus.Size = new System.Drawing.Size(75, 23);
            this.buttonScoreTeamAPlus.TabIndex = 10;
            this.buttonScoreTeamAPlus.Text = "+10";
            this.buttonScoreTeamAPlus.UseVisualStyleBackColor = true;
            this.buttonScoreTeamAPlus.Click += new System.EventHandler(this.buttonScoreTeamAPlus_Click);
            // 
            // buttonScoreTeamAReset
            // 
            this.buttonScoreTeamAReset.Location = new System.Drawing.Point(173, 261);
            this.buttonScoreTeamAReset.Name = "buttonScoreTeamAReset";
            this.buttonScoreTeamAReset.Size = new System.Drawing.Size(75, 23);
            this.buttonScoreTeamAReset.TabIndex = 11;
            this.buttonScoreTeamAReset.Text = "Reset";
            this.buttonScoreTeamAReset.UseVisualStyleBackColor = true;
            this.buttonScoreTeamAReset.Click += new System.EventHandler(this.buttonScoreTeamAReset_Click);
            // 
            // buttonScoreTeamAMinus
            // 
            this.buttonScoreTeamAMinus.Location = new System.Drawing.Point(173, 290);
            this.buttonScoreTeamAMinus.Name = "buttonScoreTeamAMinus";
            this.buttonScoreTeamAMinus.Size = new System.Drawing.Size(75, 23);
            this.buttonScoreTeamAMinus.TabIndex = 12;
            this.buttonScoreTeamAMinus.Text = "-10";
            this.buttonScoreTeamAMinus.UseVisualStyleBackColor = true;
            this.buttonScoreTeamAMinus.Click += new System.EventHandler(this.buttonScoreTeamAMinus_Click);
            // 
            // buttonScoreTeamBPlus
            // 
            this.buttonScoreTeamBPlus.Location = new System.Drawing.Point(486, 234);
            this.buttonScoreTeamBPlus.Name = "buttonScoreTeamBPlus";
            this.buttonScoreTeamBPlus.Size = new System.Drawing.Size(75, 23);
            this.buttonScoreTeamBPlus.TabIndex = 13;
            this.buttonScoreTeamBPlus.Text = "+10";
            this.buttonScoreTeamBPlus.UseVisualStyleBackColor = true;
            this.buttonScoreTeamBPlus.Click += new System.EventHandler(this.ButtonScoreTeamBPlus_Click);
            // 
            // buttonScoreTeamBReset
            // 
            this.buttonScoreTeamBReset.Location = new System.Drawing.Point(486, 260);
            this.buttonScoreTeamBReset.Name = "buttonScoreTeamBReset";
            this.buttonScoreTeamBReset.Size = new System.Drawing.Size(75, 23);
            this.buttonScoreTeamBReset.TabIndex = 14;
            this.buttonScoreTeamBReset.Text = "Reset";
            this.buttonScoreTeamBReset.UseVisualStyleBackColor = true;
            this.buttonScoreTeamBReset.Click += new System.EventHandler(this.ButtonScoreTeamBReset_Click);
            // 
            // buttonScoreTeamBMinus
            // 
            this.buttonScoreTeamBMinus.Location = new System.Drawing.Point(486, 290);
            this.buttonScoreTeamBMinus.Name = "buttonScoreTeamBMinus";
            this.buttonScoreTeamBMinus.Size = new System.Drawing.Size(75, 23);
            this.buttonScoreTeamBMinus.TabIndex = 15;
            this.buttonScoreTeamBMinus.Text = "-10";
            this.buttonScoreTeamBMinus.UseVisualStyleBackColor = true;
            this.buttonScoreTeamBMinus.Click += new System.EventHandler(this.ButtonScoreTeamBMinus_Click);
            // 
            // button_SnitchCatchA
            // 
            this.button_SnitchCatchA.Location = new System.Drawing.Point(135, 332);
            this.button_SnitchCatchA.Name = "button_SnitchCatchA";
            this.button_SnitchCatchA.Size = new System.Drawing.Size(147, 23);
            this.button_SnitchCatchA.TabIndex = 18;
            this.button_SnitchCatchA.Text = "Snitch Catch Team A";
            this.button_SnitchCatchA.UseVisualStyleBackColor = true;
            this.button_SnitchCatchA.Click += new System.EventHandler(this.Button_SnitchCatchA_Click);
            // 
            // button_Settings
            // 
            this.button_Settings.Location = new System.Drawing.Point(220, 395);
            this.button_Settings.Name = "button_Settings";
            this.button_Settings.Size = new System.Drawing.Size(75, 23);
            this.button_Settings.TabIndex = 19;
            this.button_Settings.Text = "Settings";
            this.button_Settings.UseVisualStyleBackColor = true;
            this.button_Settings.Click += new System.EventHandler(this.Button_Settings_Click);
            // 
            // button_StartTimeKeeper
            // 
            this.button_StartTimeKeeper.Location = new System.Drawing.Point(344, 395);
            this.button_StartTimeKeeper.Name = "button_StartTimeKeeper";
            this.button_StartTimeKeeper.Size = new System.Drawing.Size(115, 23);
            this.button_StartTimeKeeper.TabIndex = 20;
            this.button_StartTimeKeeper.Text = "Start Timekeeper";
            this.button_StartTimeKeeper.UseVisualStyleBackColor = true;
            this.button_StartTimeKeeper.Click += new System.EventHandler(this.Button_StartTimeKeeper_Click);
            // 
            // button_SetPenalty
            // 
            this.button_SetPenalty.Location = new System.Drawing.Point(486, 395);
            this.button_SetPenalty.Name = "button_SetPenalty";
            this.button_SetPenalty.Size = new System.Drawing.Size(75, 23);
            this.button_SetPenalty.TabIndex = 21;
            this.button_SetPenalty.Text = "Set Penalty";
            this.button_SetPenalty.UseVisualStyleBackColor = true;
            this.button_SetPenalty.Click += new System.EventHandler(this.Button_SetPenalty_Click);
            // 
            // button_CloseApp
            // 
            this.button_CloseApp.Location = new System.Drawing.Point(608, 395);
            this.button_CloseApp.Name = "button_CloseApp";
            this.button_CloseApp.Size = new System.Drawing.Size(75, 23);
            this.button_CloseApp.TabIndex = 22;
            this.button_CloseApp.Text = "Close";
            this.button_CloseApp.UseVisualStyleBackColor = true;
            this.button_CloseApp.Click += new System.EventHandler(this.Button_CloseApp_Click);
            // 
            // textBoxSetMinutes
            // 
            this.textBoxSetMinutes.Location = new System.Drawing.Point(501, 133);
            this.textBoxSetMinutes.Name = "textBoxSetMinutes";
            this.textBoxSetMinutes.Size = new System.Drawing.Size(42, 20);
            this.textBoxSetMinutes.TabIndex = 5;
            this.textBoxSetMinutes.Text = "00";
            // 
            // textBoxScoreTeamA
            // 
            this.textBoxScoreTeamA.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.textBoxScoreTeamA.Location = new System.Drawing.Point(332, 261);
            this.textBoxScoreTeamA.Name = "textBoxScoreTeamA";
            this.textBoxScoreTeamA.ReadOnly = true;
            this.textBoxScoreTeamA.Size = new System.Drawing.Size(49, 26);
            this.textBoxScoreTeamA.TabIndex = 23;
            this.textBoxScoreTeamA.Text = "0";
            this.textBoxScoreTeamA.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            // 
            // textBoxScoreTeamB
            // 
            this.textBoxScoreTeamB.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.textBoxScoreTeamB.Location = new System.Drawing.Point(403, 260);
            this.textBoxScoreTeamB.Name = "textBoxScoreTeamB";
            this.textBoxScoreTeamB.ReadOnly = true;
            this.textBoxScoreTeamB.Size = new System.Drawing.Size(56, 26);
            this.textBoxScoreTeamB.TabIndex = 24;
            this.textBoxScoreTeamB.Text = "0";
            this.textBoxScoreTeamB.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            // 
            // textBoxSetSeconds
            // 
            this.textBoxSetSeconds.Location = new System.Drawing.Point(549, 133);
            this.textBoxSetSeconds.Name = "textBoxSetSeconds";
            this.textBoxSetSeconds.Size = new System.Drawing.Size(43, 20);
            this.textBoxSetSeconds.TabIndex = 25;
            this.textBoxSetSeconds.Text = "00";
            // 
            // button_SnitchCatchB
            // 
            this.button_SnitchCatchB.Location = new System.Drawing.Point(446, 332);
            this.button_SnitchCatchB.Name = "button_SnitchCatchB";
            this.button_SnitchCatchB.Size = new System.Drawing.Size(163, 23);
            this.button_SnitchCatchB.TabIndex = 26;
            this.button_SnitchCatchB.Text = "Snitch Catch Team B";
            this.button_SnitchCatchB.UseVisualStyleBackColor = true;
            this.button_SnitchCatchB.Click += new System.EventHandler(this.Button_SnitchCatchB_Click);
            // 
            // button_StartNewGame
            // 
            this.button_StartNewGame.Location = new System.Drawing.Point(81, 395);
            this.button_StartNewGame.Name = "button_StartNewGame";
            this.button_StartNewGame.Size = new System.Drawing.Size(101, 23);
            this.button_StartNewGame.TabIndex = 27;
            this.button_StartNewGame.Text = "Start New Game";
            this.button_StartNewGame.UseVisualStyleBackColor = true;
            this.button_StartNewGame.Click += new System.EventHandler(this.Button_StartNewGame_Click);
            // 
            // Mainscreen
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(800, 450);
            this.Controls.Add(this.button_StartNewGame);
            this.Controls.Add(this.button_SnitchCatchB);
            this.Controls.Add(this.textBoxSetSeconds);
            this.Controls.Add(this.textBoxScoreTeamB);
            this.Controls.Add(this.textBoxScoreTeamA);
            this.Controls.Add(this.button_CloseApp);
            this.Controls.Add(this.button_SetPenalty);
            this.Controls.Add(this.button_StartTimeKeeper);
            this.Controls.Add(this.button_Settings);
            this.Controls.Add(this.button_SnitchCatchA);
            this.Controls.Add(this.buttonScoreTeamBMinus);
            this.Controls.Add(this.buttonScoreTeamBReset);
            this.Controls.Add(this.buttonScoreTeamBPlus);
            this.Controls.Add(this.buttonScoreTeamAMinus);
            this.Controls.Add(this.buttonScoreTeamAReset);
            this.Controls.Add(this.buttonScoreTeamAPlus);
            this.Controls.Add(this.label_TeamB);
            this.Controls.Add(this.label_TeamA);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.button_GetExtraTimer);
            this.Controls.Add(this.textBoxSetMinutes);
            this.Controls.Add(this.button_SetTimer);
            this.Controls.Add(this.button_StopGameTime);
            this.Controls.Add(this.button_StartGameTime);
            this.Controls.Add(this.textBox_GameTime);
            this.Controls.Add(this.label1);
            this.Name = "Mainscreen";
            this.Text = "Main";
            this.Load += new System.EventHandler(this.Mainscreen_Load);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.TextBox textBox_GameTime;
        private System.Windows.Forms.Button button_StartGameTime;
        private System.Windows.Forms.Button button_StopGameTime;
        private System.Windows.Forms.Button button_SetTimer;
        private System.Windows.Forms.Button button_GetExtraTimer;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.Label label_TeamA;
        private System.Windows.Forms.Label label_TeamB;
        private System.Windows.Forms.Button buttonScoreTeamAPlus;
        private System.Windows.Forms.Button buttonScoreTeamAReset;
        private System.Windows.Forms.Button buttonScoreTeamAMinus;
        private System.Windows.Forms.Button buttonScoreTeamBPlus;
        private System.Windows.Forms.Button buttonScoreTeamBReset;
        private System.Windows.Forms.Button buttonScoreTeamBMinus;
        private System.Windows.Forms.Button button_SnitchCatchA;
        private System.Windows.Forms.Button button_Settings;
        private System.Windows.Forms.Button button_StartTimeKeeper;
        private System.Windows.Forms.Button button_SetPenalty;
        private System.Windows.Forms.Button button_CloseApp;
        private System.Windows.Forms.TextBox textBoxSetMinutes;
        public System.Windows.Forms.TextBox textBoxScoreTeamA;
        public System.Windows.Forms.TextBox textBoxScoreTeamB;
        private System.Windows.Forms.TextBox textBoxSetSeconds;
        private System.Windows.Forms.Button button_SnitchCatchB;
        private System.Windows.Forms.Button button_StartNewGame;
    }
}