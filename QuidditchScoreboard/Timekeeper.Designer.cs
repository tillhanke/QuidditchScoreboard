namespace QuidditchScoreboard
{
    partial class Timekeeper
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
            this.label2 = new System.Windows.Forms.Label();
            this.textBox_TimekeeperID = new System.Windows.Forms.TextBox();
            this.textBox_TimekeeperAuthent = new System.Windows.Forms.TextBox();
            this.button_TimekeeperConnect = new System.Windows.Forms.Button();
            this.button_CloseTimekeeper = new System.Windows.Forms.Button();
            this.SuspendLayout();
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(89, 52);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(52, 13);
            this.label1.TabIndex = 0;
            this.label1.Text = "Game ID:";
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(85, 98);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(83, 13);
            this.label2.TabIndex = 1;
            this.label2.Text = "Authentification:";
            // 
            // textBox_TimekeeperID
            // 
            this.textBox_TimekeeperID.Location = new System.Drawing.Point(186, 44);
            this.textBox_TimekeeperID.Name = "textBox_TimekeeperID";
            this.textBox_TimekeeperID.Size = new System.Drawing.Size(410, 20);
            this.textBox_TimekeeperID.TabIndex = 2;
            // 
            // textBox_TimekeeperAuthent
            // 
            this.textBox_TimekeeperAuthent.Location = new System.Drawing.Point(186, 91);
            this.textBox_TimekeeperAuthent.Name = "textBox_TimekeeperAuthent";
            this.textBox_TimekeeperAuthent.Size = new System.Drawing.Size(410, 20);
            this.textBox_TimekeeperAuthent.TabIndex = 3;
            // 
            // button_TimekeeperConnect
            // 
            this.button_TimekeeperConnect.Location = new System.Drawing.Point(186, 162);
            this.button_TimekeeperConnect.Name = "button_TimekeeperConnect";
            this.button_TimekeeperConnect.Size = new System.Drawing.Size(75, 23);
            this.button_TimekeeperConnect.TabIndex = 4;
            this.button_TimekeeperConnect.Text = "Connect";
            this.button_TimekeeperConnect.UseVisualStyleBackColor = true;
            this.button_TimekeeperConnect.Click += new System.EventHandler(this.Button_TimekeeperConnect_Click);
            // 
            // button_CloseTimekeeper
            // 
            this.button_CloseTimekeeper.Location = new System.Drawing.Point(399, 162);
            this.button_CloseTimekeeper.Name = "button_CloseTimekeeper";
            this.button_CloseTimekeeper.Size = new System.Drawing.Size(75, 23);
            this.button_CloseTimekeeper.TabIndex = 5;
            this.button_CloseTimekeeper.Text = "Close";
            this.button_CloseTimekeeper.UseVisualStyleBackColor = true;
            this.button_CloseTimekeeper.Click += new System.EventHandler(this.Button_CloseTimekeeper_Click);
            // 
            // Timekeeper
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(760, 207);
            this.Controls.Add(this.button_CloseTimekeeper);
            this.Controls.Add(this.button_TimekeeperConnect);
            this.Controls.Add(this.textBox_TimekeeperAuthent);
            this.Controls.Add(this.textBox_TimekeeperID);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.label1);
            this.Name = "Timekeeper";
            this.Text = "Timekeeper";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.TextBox textBox_TimekeeperID;
        private System.Windows.Forms.TextBox textBox_TimekeeperAuthent;
        private System.Windows.Forms.Button button_TimekeeperConnect;
        private System.Windows.Forms.Button button_CloseTimekeeper;
    }
}