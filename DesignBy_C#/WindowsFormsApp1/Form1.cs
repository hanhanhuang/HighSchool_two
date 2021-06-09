using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace WindowsFormsApp1
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
            
        }
        public int player = 2; //玩家
        public int x = 0;  //x贏的次數
        public int o = 0; //o贏的次數
        public int turn = 0; //順序(幾輪
        
        
        
        private void groupBox2_Enter(object sender, EventArgs e)
        {

        }

        private void button12_Click(object sender, EventArgs e)
        {
            this.Close(); //關閉程式
        }

        private void Button_click(object sender, EventArgs e)
        {
            Button button = (Button)sender; 
            if (button.Text=="") //button 已有文字則不能做改動
            {
                if (player % 2 == 0)
                {
                    turn++; 
                    if (turn != 9) //turn=9代表九宮格裡皆有文字 不能在輪流
                    {
                        label7.Text = " O turn.";
                    }
                    else
                        label7.Text = "";
                    button.Text = " X ";
                    player++;
                }
                else
                {
                    turn++;
                    if (turn != 9)
                    {
                        label7.Text = " X turn.";
                    }
                    button.Text = " O ";
                    player++;
                    
                }
                if (Checkwinner() == true) //區分是誰連線
                {
                    if(button.Text==" X ")
                    {
                        label7.Text = "";
                        MessageBox.Show(textBox1.Text + " WIN!!!");
                        x++;
                    }
                    else if(button.Text==" O ")
                    {
                        label7.Text = "";
                        MessageBox.Show(textBox2.Text + " WIN!!!");
                        o++;
                    }
                    label4.Text = "WIN:" + x + "次";
                    label5.Text = "WIN:" + o + "次";
                }
                else if((Checkwinner() == false) && turn==9)
                {
                    MessageBox.Show("平手...");
                }
                
            }
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }
        bool Checkwinner() //檢查連線
        {
            //行
            if ((NO1.Text == NO2.Text) && (NO2.Text == NO3.Text) && NO1.Text != "")
            {
                NO1.BackColor = NO2.BackColor = NO3.BackColor = Color.Yellow; //標示哪條連線
                return true;
            }
            else if ((NO4.Text == NO5.Text) && (NO5.Text == NO6.Text) && NO4.Text != "")
            {
                NO4.BackColor = NO5.BackColor = NO6.BackColor = Color.Yellow;
                return true;
            }
            else if ((NO7.Text == NO8.Text) && (NO8.Text == NO9.Text) && NO7.Text != "")
            {
                NO7.BackColor = NO8.BackColor = NO9.BackColor = Color.Yellow;
                return true;
            }

            //列
            if ((NO1.Text == NO4.Text) && (NO4.Text == NO7.Text) && NO1.Text != "")
            {
                NO1.BackColor = NO4.BackColor = NO7.BackColor = Color.Yellow;
                return true;
            }
            else if ((NO2.Text == NO5.Text) && (NO5.Text == NO8.Text) && NO2.Text != "")
            {
                NO2.BackColor = NO5.BackColor = NO8.BackColor = Color.Yellow;
                return true;
            }
            else if ((NO3.Text == NO6.Text) && (NO6.Text == NO9.Text) && NO3.Text != "")
            {
                NO3.BackColor = NO6.BackColor = NO9.BackColor = Color.Yellow;
                return true;
            }

            //斜
            if ((NO1.Text == NO5.Text) && (NO5.Text == NO9.Text) && NO1.Text != "")
            {
                NO1.BackColor = NO5.BackColor = NO9.BackColor = Color.Yellow;
                return true;
            }
            else if ((NO3.Text == NO5.Text) && (NO5.Text == NO7.Text) && NO3.Text != "")
            {
                NO3.BackColor = NO5.BackColor = NO7.BackColor = Color.Yellow;
                return true;
            }
            else
                return false;

        }

        private void textBox1_TextChanged(object sender, EventArgs e)
        {

        }

        private void button10_Click(object sender, EventArgs e)
        {
            NO1.Enabled = NO2.Enabled = NO3.Enabled = true;
            NO4.Enabled = NO5.Enabled = NO6.Enabled = true;
            NO7.Enabled = NO8.Enabled = NO9.Enabled = true;
            textBox1.Enabled = textBox2.Enabled = false;
            button10.Enabled = false;
        }
        void Newgame() //重新開始 全部值皆要重設
        {
            player = 2;
            turn = 0;
            label7.Text = " X turn.";
            NO1.Text = NO2.Text = NO3.Text = "";
            NO4.Text = NO5.Text = NO6.Text = "";
            NO7.Text = NO8.Text = NO9.Text = "";

            NO1.BackColor = NO2.BackColor = NO3.BackColor = Color.Gainsboro;
            NO4.BackColor = NO5.BackColor = NO6.BackColor = Color.Gainsboro;
            NO7.BackColor = NO8.BackColor = NO9.BackColor = Color.Gainsboro;
        }

        private void button11_Click(object sender, EventArgs e)
        {
            Newgame(); //重新開始 (接續玩家名字以及獲勝次數
        }

        private void button1_Click(object sender, EventArgs e)
        {

        }
    }
}
