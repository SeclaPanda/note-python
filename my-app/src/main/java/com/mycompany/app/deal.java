package com.mycompany.app;
import java.util.Arrays;
import java.util.Scanner;

public class deal
{
    public static void main(String[] args)
    {
        Scanner input = new Scanner(System.in);

        MarkSys Offer = new MarkSys(0, "Yandex", "mail", "Alex", "Welcome", " "/** , "Send"*/);
        
        if (Offer.getStat() == " ")
        {
            Offer.setStat();
        }
        print("Id: " + Offer.getId());
        print("Company Name: " + Offer.getComp());
        print("Response channel: " + Offer.getNet());
        print("Client name: " + Offer.getName());
        print("Text: " + Offer.getText());
        print("Status: " + Offer.getStat());

        if (Offer.getStat() != "Send")
        {
            print("Set new company name: ");
            String NewComp = input.nextLine();
            Offer.setComp(NewComp); 
            print("Set new response channel: ");
            String NewNet = input.nextLine();
            Offer.setNet(NewNet); 
            print("Set new client name: ");
            String NewName = input.nextLine();
            Offer.setName(NewName);
            print("Set new text: ");
            String NewText = input.nextLine();
            Offer.setText(NewText);
            
            Offer.setStat();

            print("Id = " + Offer.getId());
            print("Company Name = " + Offer.getComp());
            print("Response channel = " + Offer.getNet());
            print("Client name = " + Offer.getName());
            print("Text = " + Offer.getText());
            print("Status = " + Offer.getStat());
        
        }
        else
        {
            System.out.println("You can't edit sended offer!");
        }
    }

    private static void print(String s) {
        System.out.println(s);
    }
}