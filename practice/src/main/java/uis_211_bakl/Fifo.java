package uis_211_bakl;

public class Fifo
{
    private AdsSys data;
    private Fifo next, prev;

    public void setData(AdsSys data)
    {
        this.data = data;
    }

    public AdsSys getData()
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
