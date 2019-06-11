namespace QuidditchScoreboard
{
    partial class OutputPaths
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
            this.textBox_OutputPaths = new System.Windows.Forms.TextBox();
            this.label1 = new System.Windows.Forms.Label();
            this.button_OKOutput = new System.Windows.Forms.Button();
            this.button_CancelOutput = new System.Windows.Forms.Button();
            this.label2 = new System.Windows.Forms.Label();
            this.textBox_InputPaths = new System.Windows.Forms.TextBox();
            this.label3 = new System.Windows.Forms.Label();
            this.SuspendLayout();
            // 
            // textBox_OutputPaths
            // 
            this.textBox_OutputPaths.Location = new System.Drawing.Point(102, 49);
            this.textBox_OutputPaths.Name = "textBox_OutputPaths";
            this.textBox_OutputPaths.Size = new System.Drawing.Size(587, 20);
            this.textBox_OutputPaths.TabIndex = 0;
            this.textBox_OutputPaths.TextChanged += new System.EventHandler(this.TextBox1_TextChanged);
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(13, 52);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(83, 13);
            this.label1.TabIndex = 1;
            this.label1.Text = "Output File Path";
            // 
            // button_OKOutput
            // 
            this.button_OKOutput.Location = new System.Drawing.Point(150, 105);
            this.button_OKOutput.Name = "button_OKOutput";
            this.button_OKOutput.Size = new System.Drawing.Size(75, 23);
            this.button_OKOutput.TabIndex = 2;
            this.button_OKOutput.Text = "OK";
            this.button_OKOutput.UseVisualStyleBackColor = true;
            this.button_OKOutput.Click += new System.EventHandler(this.Button_OKOutput_Click);
            // 
            // button_CancelOutput
            // 
            this.button_CancelOutput.Location = new System.Drawing.Point(538, 105);
            this.button_CancelOutput.Name = "button_CancelOutput";
            this.button_CancelOutput.Size = new System.Drawing.Size(75, 23);
            this.button_CancelOutput.TabIndex = 3;
            this.button_CancelOutput.Text = "Cancel";
            this.button_CancelOutput.UseVisualStyleBackColor = true;
            this.button_CancelOutput.Click += new System.EventHandler(this.Button_CancelOutput_Click);
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(90, 131);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(408, 13);
            this.label2.TabIndex = 4;
            this.label2.Text = "Hint: Sometimes you have to click OK twice. The default folder is C:\\ for the pat" +
    "hs file";
            // 
            // textBox_InputPaths
            // 
            this.textBox_InputPaths.Location = new System.Drawing.Point(102, 76);
            this.textBox_InputPaths.Name = "textBox_InputPaths";
            this.textBox_InputPaths.Size = new System.Drawing.Size(587, 20);
            this.textBox_InputPaths.TabIndex = 5;
            this.textBox_InputPaths.TextChanged += new System.EventHandler(this.TextBox_InputPaths_TextChanged);
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(16, 82);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(75, 13);
            this.label3.TabIndex = 6;
            this.label3.Text = "Input File Path";
            // 
            // OutputPaths
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(721, 159);
            this.Controls.Add(this.label3);
            this.Controls.Add(this.textBox_InputPaths);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.button_CancelOutput);
            this.Controls.Add(this.button_OKOutput);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.textBox_OutputPaths);
            this.Name = "OutputPaths";
            this.Text = "Output Paths";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        public System.Windows.Forms.TextBox textBox_OutputPaths;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Button button_OKOutput;
        private System.Windows.Forms.Button button_CancelOutput;
        private System.Windows.Forms.Label label2;
        public System.Windows.Forms.TextBox textBox_InputPaths;
        private System.Windows.Forms.Label label3;
    }
}