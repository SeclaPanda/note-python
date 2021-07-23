package uis_211_bakl;

public class AdsSys 
{
    private int Id;  
    private String Camp;
    private String Net;
    private String Name;
    private String Text;
    private String Stat;

    public AdsSys(int Id, String Camp, String Net, String Name, String Text, String Stat)
    {
        this.Id = Id;
        this.Camp = Camp;
        this.Net = Net;
        this.Name = Name;
        this.Text = Text;
        this.Stat = Stat;
    }

    public AdsSys(){
    }

    public int getId()
    {
        return Id;
    }

    public void setId(int Id)
    {
        this.Id = Id;
    }

    public String getCamp()
    {
        return Camp;
    } 

    public void setCamp(String Camp)
    {
        this.Camp = Camp;
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

    public void setStat() //method for automatically adding status to objects
    {
        if (Camp != " " && Net != " " && Name != " " && Text != " ")
        {
            this.Stat = "Ready";
        }
        else if (Camp == " " || Net == " " || Name == " " || Text == " ")
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
        return "Id: " + Id + "\nCampaign name: " + Camp + "\nNetwork channel: " + Net + "\nName: " + Name + "\nText: " + Text + "\nStatus: " + Stat; 
    }    
}
