package com.mycompany.app;

public class Fifo 
{
    private MarkSys data;
    private Fifo next, prev;

    public void setData(MarkSys data)
    {
        this.data = data;
    }

    public MarkSys getData()
    {
        return data;
    }

    public Fifo getNext()
    {
        return next;
    }

    public void setNext(Fifo next)
    {
        this.next = next;
    }

    public Fifo getPrev()
    {
        return prev;
    }

    public void setPrev(Fifo prev)
    {
        this.prev = prev;
    }
}
