package com.mycompany.app;

public class MarkSys
{
    private int Id;  
    private String Comp;
    private String Net;
    private String Name;
    private String Text;
    private String Stat;

    public MarkSys(int Id, String Comp, String Net, String Name, String Text, String Stat)
    {
        this.Id = Id;
        this.Comp = Comp;
        this.Net = Net;
        this.Name = Name;
        this.Text = Text;
        this.Stat = Stat;
    }

    public MarkSys(){
    }

    public int getId()
    {
        return Id;
    }

    public void setId(int Id)
    {
        this.Id = Id;
    }

    public String getComp()
    {
        return Comp;
    } 

    public void setComp(String Comp)
    {
        this.Comp = Comp;
    }

    public String getNet()
    {
        return Net;
    } 

    public void setNet(String Net)
    {
        this.Net = Net;
    }

    public String getName()
    {
        return Name;
    } 

    public void setName(String Name)
    {
        this.Name = Name;
    }

    public String getText()
    {
        return Text;
    } 

    public void setText(String Text)
    {
        this.Text = Text;
    }

    public String getStat()
    {
        return Stat;
    } 

    public void setStat()
    {
        if (Comp != " " && Net != " " && Name != " " && Text != " ")
        {
            this.Stat = "Ready";
        }
        else if (Comp == " " || Net == " " || Name == " " || Text == " ")
        {
            this.Stat = "Returned";
        }
        else
        {
            this.Stat = "Send";
        }
    }

    public void setStatMan(String Stat)
    {
        this.Stat = Stat;
    }

    public String toString()
    {
        return "Id: " + Id + "\nCompany name: " + Comp + "\nNetwork channel: " + Net + "\nName: " + Name + "\nText: " + Text + "\nStatus: " + Stat; 
    }
} 