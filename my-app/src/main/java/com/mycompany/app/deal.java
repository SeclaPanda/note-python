package com.mycompany.app;
import java.util.Scanner;

public class deal
{
    public static void main(String[] args)
    {
        Scanner input = new Scanner(System.in);

        MarkSys Offer = new MarkSys(0, "Yandex", "mail", "Alex", "Welcome", "Send");
        
        int OfferId = Offer.getId();
        String OfferComp = Offer.getComp();
        String OfferNet = Offer.getNet();
        String OfferName = Offer.getName();
        String OfferText = Offer.getText();
        String OfferStat = Offer.getStat();

        System.out.println("Id = " + OfferId);
        System.out.println("Company Name = " + OfferComp);
        System.out.println("Response channel = " + OfferNet);
        System.out.println("Client name = " + OfferName);
        System.out.println("Text = " + OfferText);
        System.out.println("Status = " + OfferStat);

        if (OfferStat != "Send")
        {
            System.out.print("Set new company name: ");
            String NewComp = input.nextLine();
            Offer.setComp(NewComp); 
            System.out.print("Set new response channel: ");
            String NewNet = input.nextLine();
            Offer.setNet(NewNet); 
            System.out.print("Set new client name: ");
            String NewName = input.nextLine();
            Offer.setName(NewName);
            System.out.print("Set new text: ");
            String NewText = input.nextLine();
            Offer.setText(NewText);
            System.out.print("Set new status: ");
            String NewStat = input.nextLine();
            Offer.setStat(NewStat);

            print();
        
        }
        else
        {
            System.out.println("You can't edit sended offer!");
        }
    }
    public void print()
    {
        System.out.println("Id = " + Offer.getId());
        System.out.println("Company Name = " + Offer.getComp());
        System.out.println("Response channel = " + Offer.getNet());
        System.out.println("Client name = " + Offer.getName());
        System.out.println("Text = " + Offer.getText());
        System.out.println("Status = " + Offer.getStat());
    }
}