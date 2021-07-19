package com.mycompany.app;

public class que
{
    private void print(String string) 
    {
        System.out.println(string);
    }
    
    private Fifo list;
    private int len;

    public que()
    {
        list = null;
        len = 0;
    }

    public void push(MarkSys data)
    {
        Fifo fifo = new Fifo();
        fifo.setData(data);
        fifo.setLast(null);
        if (list == null)
        {
            list = fifo;
            fifo.setLast(null);
        }
        else
        {
            fifo.setFirst(list);
            list.setLast(fifo);
            list = fifo;
        }
        len++;
    }

    public void pop()
    {
        if (len == 0)
        {
            print("Empty! Can't delete.");
        }
        else
        {
            Fifo fifo = list.getFirst();
            list = fifo;
            list.setFirst(null);
        }
    }

    public MarkSys getObj (int Id)
        {
            Fifo fifo = list;
            MarkSys off = new MarkSys();
            while (fifo != null)
            {
                if (Id == fifo.getData().getId())
                {
                    off = fifo.getData();
                    break;
                }
                else
                {
                    fifo = fifo.getFirst();
                }
            }
            return off;
        }

    public boolean check (int Id)
    {
        Fifo fifo = list;
        boolean check = false;
    while (fifo != null)
        {
            if (Id == list.getData().getId())
            {
                check = true;
                break;
            }
            else
            {
                fifo = fifo.getFirst(); 
            }    
        }
        
        return check;
    }
        
    public String showFifo() 
    { 
        String out = ""; 
        Fifo fifo = list; 
        while (fifo != null) 
        { 
            out += fifo.getData(); 
            out += "\n\n"; 
            fifo = fifo.getFirst();
        } 
        if (out == "")
            return "Стек пуст."; 
        else 
            return out; 
    }
}