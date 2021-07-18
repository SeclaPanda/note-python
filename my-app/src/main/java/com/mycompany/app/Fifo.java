package com.mycompany.app;

public class Fifo 
{
    private MarkSys data;
    private Fifo first, last;

    public Fifo()
    {
        first = null;
        last = null;
    }

    public void setData(MarkSys data)
    {
        this.data = data;
    }

    public MarkSys getData()
    {
        return data;
    }

    public Fifo getFirst()
    {
        return first;
    }

    public void setFirst(Fifo first)
    {
        this.first = first;
    }

    public Fifo getLast()
    {
        return last;
    }

    public void setLast(Fifo last)
    {
        this.last = last;
    }
}
