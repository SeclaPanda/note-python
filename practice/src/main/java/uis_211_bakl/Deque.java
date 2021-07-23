package uis_211_bakl;

public class Deque
{
    private Fifo Head, Tail;

    private void print(String string) 
    {
        System.out.println(string);
    }
    
    public void deque()
    {
        Head = null;
        Tail = null;
    }
    
    public void addBack(AdsSys of)
    {
        Fifo temp = new Fifo();
        temp.setNext(null);
        temp.setData(of);
        if (Head != null)
        {
            temp.setPrev(Tail);
            Tail.setNext(temp);
            Tail = temp; 
        }
        else
        {
            temp.setPrev(null);
            Head = Tail = temp;
        }
    }

    public void Demo()
    {
        Fifo temp;
        temp = Head;
        while (temp != null)
        {
            print(temp.getData().toString() + "\n\n");
            temp = temp.getNext();
        }
    }

    public void popFront()
    {
        Fifo temp = Head.getNext();
        Head = null;
        Head = temp;
        Head.setPrev(null);
    }

    public AdsSys Choose(String id) 
    {
        AdsSys out = new AdsSys();
        Fifo temp;
        temp = Head;
        while (temp != null) 
        {
            if (Integer.parseInt(id) == temp.getData().getId())
            {
                out = temp.getData();
                break;
            }
            else
            {
                out = null;
                temp = temp.getNext();
            }
        }
        return out; 
    }

    public boolean CheckId(String id)
    {
        Fifo temp;   
        temp = Head;
        boolean check = false;
        int x = Integer.parseInt(id);
        while (temp != null)
        {
            int y = temp.getData().getId();
            if (x == y)
            {
                check = true;
                print("Check ID is complete!");
                break;
            }
            else
            {
                check = false; 
                temp = temp.getNext();
            }
        } 
        if (check == false)
        {
            print("Check ID is failed!");
        }
        return check;
    }
}
