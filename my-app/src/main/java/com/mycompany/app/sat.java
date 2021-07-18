package com.mycompany.app;

import java.util.Arrays;

public enum sat {
    ready,
    send, 
    returned;

    private String title;

    void Sta(String title) {
       this.title = title;
    }

    public String getTitle() {
       return title;
    }

    @Override
    public String toString() {
       return "Status{" +
               "title='" + title + '\'' +
               '}';
    }
    public static void main(String[] args)
    {
      ready.title = "ready";
      send.title = "send";
      returned.title = "returned";
      System.out.println(Arrays.toString(sat.values()));
    }
}