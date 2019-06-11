namespace QuidditchScoreboard
{
    partial class ExtraTimer
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;



        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.label1 = new System.Windows.Forms.Label();
            this.textBox_TimerLabel = new System.Windows.Forms.TextBox();
            this.SuspendLayout();
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(123, 74);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(68, 13);
            this.label1.TabIndex = 0;
            this.label1.Text = "Timer Label: ";
            // 
            // textBox_TimerLabel
            // 
            this.textBox_TimerLabel.Location = new System.Drawing.Point(223, 66);
            this.textBox_TimerLabel.Name = "textBox_TimerLabel";
            this.textBox_TimerLabel.Size = new System.Drawing.Size(242, 20);
            this.textBox_TimerLabel.TabIndex = 1;
            this.textBox_TimerLabel.TextChanged += new System.EventHandler(this.TextBox_TimerLabel_TextChanged);
            // 
            // ExtraTimer
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(800, 450);
            this.Controls.Add(this.textBox_TimerLabel);
            this.Controls.Add(this.label1);
            this.Name = "ExtraTimer";
            this.Text = "Extra Timer";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.TextBox textBox_TimerLabel;
    }
}