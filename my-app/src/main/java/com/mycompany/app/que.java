package com.mycompany.app;

import java.util.LinkedList;

public class que
{
    public static void main(String[] args)
    {
        LinkedList<MarkSys> fifo = new LinkedList<MarkSys>();
        
        MarkSys Offer1 = new MarkSys(0, "Yandex", "mail", "Alex", "Welcome", " "/** , "Send"*/);
        MarkSys Offer2 = new MarkSys(0, "Mail", "post", "Ivan", "See u later!", " "/** , "Send"*/);
        MarkSys Offer3 = new MarkSys(0, "Google", "mail", "Darya", "Good bye!", " "/** , "Send"*/);

        /**fifo.addLast(Offer2);
        fifo.addLast(Offer3);
        fifo.addLast(Offer1);
        fifo.removeFirst();

        for (MarkSys i: fifo)
        {
            System.out.println(i.getId());
            System.out.println(i.getComp());
            System.out.println(i.getNet());
            System.out.println(i.getName());
            System.out.println(i.getText());
            System.out.println(i.getStat());

        }*/
    }

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
            fifo.setFirst(null);
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
            Fifo fifo = list.getLast();
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
                    fifo = fifo.getLast();
                }
            }
            return off;
        }

        
}