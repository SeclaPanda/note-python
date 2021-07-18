package com.mycompany.app;

import java.util.LinkedList;
import java.util.Queue;

public class que
{
    public static void main(String[] args)
    {
        LinkedList<MarkSys> que = new LinkedList<MarkSys>();
        MarkSys Offer1 = new MarkSys(0, "Yandex", "mail", "Alex", "Welcome", " "/** , "Send"*/);
        MarkSys Offer2 = new MarkSys(0, "Mail", "post", "Ivan", "See u later!", " "/** , "Send"*/);
        MarkSys Offer3 = new MarkSys(0, "Google", "mail", "Darya", "Good bye!", " "/** , "Send"*/);

        que.add(Offer2);
        que.add(Offer3);
        que.add(Offer1);

        for (MarkSys i: que)
        {
            System.out.println(i);
        }
    }
}