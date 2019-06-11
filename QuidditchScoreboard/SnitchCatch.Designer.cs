namespace QuidditchScoreboard
{
    partial class SnitchCatch
    {
        /// <summary>
        /// Erforderliche Designervariable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Verwendete Ressourcen bereinigen.
        /// </summary>
        /// <param name="disposing">True, wenn verwaltete Ressourcen gelöscht werden sollen; andernfalls False.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Vom Windows Form-Designer generierter Code

        /// <summary>
        /// Erforderliche Methode für die Designerunterstützung.
        /// Der Inhalt der Methode darf nicht mit dem Code-Editor geändert werden.
        /// </summary>
        private void InitializeComponent()
        {
            this.groupBox1 = new System.Windows.Forms.GroupBox();
            this.radioButtonSnitchTeamB = new System.Windows.Forms.RadioButton();
            this.radioButton_SnitchTeamA = new System.Windows.Forms.RadioButton();
            this.buttonOKSnitch = new System.Windows.Forms.Button();
            this.buttonCancelSnitch = new System.Windows.Forms.Button();
            this.groupBox1.SuspendLayout();
            this.SuspendLayout();
            // 
            // groupBox1
            // 
            this.groupBox1.Controls.Add(this.radioButtonSnitchTeamB);
            this.groupBox1.Controls.Add(this.radioButton_SnitchTeamA);
            this.groupBox1.Location = new System.Drawing.Point(57, 21);
            this.groupBox1.Name = "groupBox1";
            this.groupBox1.Size = new System.Drawing.Size(532, 100);
            this.groupBox1.TabIndex = 0;
            this.groupBox1.TabStop = false;
            this.groupBox1.Text = "groupBox1";
            // 
            // radioButtonSnitchTeamB
            // 
            this.radioButtonSnitchTeamB.AutoSize = true;
            this.radioButtonSnitchTeamB.Location = new System.Drawing.Point(300, 41);
            this.radioButtonSnitchTeamB.Name = "radioButtonSnitchTeamB";
            this.radioButtonSnitchTeamB.Size = new System.Drawing.Size(62, 17);
            this.radioButtonSnitchTeamB.TabIndex = 1;
            this.radioButtonSnitchTeamB.TabStop = true;
            this.radioButtonSnitchTeamB.Text = "Team B";
            this.radioButtonSnitchTeamB.UseVisualStyleBackColor = true;
            // 
            // radioButton_SnitchTeamA
            // 
            this.radioButton_SnitchTeamA.AutoSize = true;
            this.radioButton_SnitchTeamA.Location = new System.Drawing.Point(26, 41);
            this.radioButton_SnitchTeamA.Name = "radioButton_SnitchTeamA";
            this.radioButton_SnitchTeamA.Size = new System.Drawing.Size(62, 17);
            this.radioButton_SnitchTeamA.TabIndex = 0;
            this.radioButton_SnitchTeamA.TabStop = true;
            this.radioButton_SnitchTeamA.Text = "Team A";
            this.radioButton_SnitchTeamA.UseVisualStyleBackColor = true;
            // 
            // buttonOKSnitch
            // 
            this.buttonOKSnitch.Location = new System.Drawing.Point(178, 175);
            this.buttonOKSnitch.Name = "buttonOKSnitch";
            this.buttonOKSnitch.Size = new System.Drawing.Size(75, 23);
            this.buttonOKSnitch.TabIndex = 1;
            this.buttonOKSnitch.Text = "OK";
            this.buttonOKSnitch.UseVisualStyleBackColor = true;
            this.buttonOKSnitch.Click += new System.EventHandler(this.ButtonOKSnitch_Click);
            // 
            // buttonCancelSnitch
            // 
            this.buttonCancelSnitch.Location = new System.Drawing.Point(318, 175);
            this.buttonCancelSnitch.Name = "buttonCancelSnitch";
            this.buttonCancelSnitch.Size = new System.Drawing.Size(75, 23);
            this.buttonCancelSnitch.TabIndex = 2;
            this.buttonCancelSnitch.Text = "Cancel";
            this.buttonCancelSnitch.UseVisualStyleBackColor = true;
            this.buttonCancelSnitch.Click += new System.EventHandler(this.ButtonCancelSnitch_Click);
            // 
            // SnitchCatch
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(636, 229);
            this.Controls.Add(this.buttonCancelSnitch);
            this.Controls.Add(this.buttonOKSnitch);
            this.Controls.Add(this.groupBox1);
            this.Name = "SnitchCatch";
            this.Text = "Snitch Catch";
            this.groupBox1.ResumeLayout(false);
            this.groupBox1.PerformLayout();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.GroupBox groupBox1;
        private System.Windows.Forms.RadioButton radioButtonSnitchTeamB;
        private System.Windows.Forms.RadioButton radioButton_SnitchTeamA;
        private System.Windows.Forms.Button buttonOKSnitch;
        private System.Windows.Forms.Button buttonCancelSnitch;
    }
}

