package com.mycompany.app;
import java.util.Scanner;

public class main 
{
    public static void main(String[] args) 
    { 
        Scanner scanner = new Scanner(System.in);   
        
        MarkSys of1 = new MarkSys(0, "Yandex", "Post", "Ivan", "Hi!", "");
        MarkSys of2 = new MarkSys(1, "Mail", "Net", "Alex", "See you later", "");

        deque fifo = new deque();
        fifo.addBack(of2);
        fifo.addBack(of1);
        fifo.addBack(new MarkSys(2, "Google", "Link", "Lera", "How u doing?", "Send"));
        fifo.Demo();
        fifo.popFront();
        fifo.Demo();
        while (true)
        {
            print("Plaese enter ID:  ");
            String id = scanner.nextLine();
            try 
            {
                Integer.parseInt(id);
                if (fifo.CheckId(id)) 
                {
                    MarkSys offer = fifo.Choose(id);
                    if (offer.getStat() != "Send")
                    {
                        print("Set new company name: ");
                        String NewComp = scanner.nextLine();
                        offer.setComp(NewComp); 
                        print("Set new response channel: ");
                        String NewNet = scanner.nextLine();
                        offer.setNet(NewNet); 
                        print("Set new client name: ");
                        String NewName = scanner.nextLine();
                        offer.setName(NewName);
                        print("Set new text: ");
                        String NewText = scanner.nextLine();
                        offer.setText(NewText);
                        print("\n\n");
                        break;
                    }
                    else 
                    {
                        print("Error! Status is Send, you can't change that offer!");
                    }
                }
                else
                {
                    print("Re-enter ID.");
                }
            }
            catch (Exception e)
            {
                print("Error! Please check your data and repeat.");
                scanner.nextLine();
            }
        }
        fifo.Demo();

        while (true)
        {
            print("Plaese enter ID:  ");
            String id = scanner.nextLine();
            try 
            {
                Integer.parseInt(id);
                if (fifo.CheckId(id)) 
                {
                    MarkSys offer = fifo.Choose(id);
                    print("Do you want to get auto status or set manual? 1 - auto, 2 - man");
                    int ans = scanner.nextInt();
                    if (ans == 1)
                    {
                        offer.setStat();
                        print("\nNew status for choosen offer is: " + offer.getStat().toString() + "\n");
                        fifo.Demo();
                        break;
                    }
                    else if (ans == 2)
                    {
                        print("Set new status: ");
                        String stat = scanner.next();
                        try
                        {
                            offer.setStatMan(stat);
                            print("\nNew status for choosen offer is: " + offer.getStat().toString() + "\n");
                            fifo.Demo();
                            break;
                        }
                        catch (Exception e)
                        {
                            print("Wrong status! Please, try again.");
                        }
                    }
                    else
                    {
                        print("You pick wrong param. Try again!");
                    }
                } 
                else 
                {
                    print("Error! Please try again."); 
                }
            } 
            catch (Exception e) 
            {
                print("Error! Inappropriate value.");
            }
        }
        print(of2.toString());
    }
    private static void print(String string) 
    {
        System.out.println(string);
    }
}