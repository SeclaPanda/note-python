package uis_211_bakl; 
import java.util.Scanner;
import org.joda.time.LocalDateTime;

public class Main
{
    public static void main(String[] args) 
    { 
        Scanner scanner = new Scanner(System.in);   //Make scanner for manual input
        
        AdsSys of1 = new AdsSys(0, "15 Discount", "Message", "Ivan", "Hi! There are your personal 15% discount.", ""); //Make first object of our class
        AdsSys of2 = new AdsSys(1, "20 Discount", "Banner", "Alex", "Hello! We are glad to work with you, enjoy your 20% off!", ""); //Make second object

        Deque fifo = new Deque(); //make an object of data type - first-in-first-out
        fifo.addBack(of2); //add second object to fifo
        fifo.addBack(of1); //add first object to fifo
        fifo.addBack(new AdsSys(2, "First Purchase", "Link", "Lera", "How u doing? There are your first purchase discount. Welcome!", "Send")); //make third object of class and adding to fifo
        fifo.Demo(); //print fifo
        fifo.popFront(); //delete of2 from fifo
        fifo.Demo(); //print fifo
        while (true) //making an loop for programm
        {
            print("Plaese enter ID:  "); //ask which object you wanna change
            String id = scanner.nextLine(); //manual input
            try 
            {
                Integer.parseInt(id); //change string id to int id
                if (fifo.CheckId(id))  //check id for available to insert changes 
                {
                    AdsSys offer = fifo.Choose(id); //choose object from fifo based on id
                    if (offer.getStat() != "Send") //checking can object be changed 
                    {
                        print("Set new campaign name: "); //printing request to change campaign name
                        String NewCamp = scanner.nextLine(); //manual input changes
                        offer.setCamp(NewCamp); //set changes
                        print("Set new response channel: ");//printing request to change response channel name
                        String NewNet = scanner.nextLine();//manual input changes
                        offer.setNet(NewNet); //set changes
                        print("Set new client name: ");//printing request to change client name
                        String NewName = scanner.nextLine();//manual input changes
                        offer.setName(NewName);//set changes
                        print("Set new text: ");//printing request to change text 
                        String NewText = scanner.nextLine();//manual input changes
                        offer.setText(NewText);//set changes
                        print("\n\n");// print two empty lines
                        break; //stop loop
                    }
                    else 
                    {
                        print("Error! Status is Send, you can't change that offer!"); //error if object can't be changed
                    }
                }
                else
                {
                    print("Re-enter ID."); //error if entered wrong id
                }
            }
            catch (Exception e) //exception
            {
                print("Error! Please check your data and repeat."); //wrong id
                scanner.nextLine(); //manual input for id
            }
        }
        LocalDateTime dttm = LocalDateTime.now(); //make an object of joda time plugin for date and time
        fifo.Demo(); //printing fifo
        print("Local time of changes is: " + dttm.toString("MM/dd/yyyy HH:mm:ss")); //print local time and date as time and date of changes

        while (true) //waking a loop for second part of programm
        {
            print("Plaese enter ID:  "); //printing a request for input id
            String id = scanner.nextLine(); //manual input id
            try  
            {
                Integer.parseInt(id); //change string id to int id
                if (fifo.CheckId(id)) //check id for available to change id
                {
                    AdsSys offer = fifo.Choose(id); //choose object to chamge from fifo
                    print("Do you want to get auto status or set manual? 1 - auto, 2 - man"); //printing request and instruction for change status of object
                    int ans = scanner.nextInt(); //manual input answer to previous line
                    if (ans == 1) //check answer
                    {
                        offer.setStat(); //set new status automatically
                        print("\nNew status for choosen offer is: " + offer.getStat().toString() + "\n"); 
                        LocalDateTime dt = LocalDateTime.now(); //make an object of joda time plugin for date and time
                        fifo.Demo(); //printing fifo
                        print("Local time of changes is: " + dt.toString("MM/dd/yyyy HH:mm:ss")); //print local time and date as time and date of changes
                        break; //stop loop 
                    }
                    else if (ans == 2) //check answer 
                    {
                        print("Set new status: "); //printing request for new status
                        String stat = scanner.next(); //manual import status
                        try
                        {
                            offer.setStatMan(stat); //set new status to object manually
                            print("\nNew status for choosen offer is: " + offer.getStat().toString() + "\n"); //printing new status
                            LocalDateTime tm = LocalDateTime.now(); //make an object of joda time plugin for date and time
                            fifo.Demo(); //printing fifo
                            print("Local time of changes is: " + tm.toString("MM/dd/yyyy HH:mm:ss")); //print local time and date as time and date of changes
                            break; //stop loop
                        }
                        catch (Exception e) //exception 
                        {
                            print("Wrong status! Please, try again."); //print a error message
                        }
                    }
                    else //if answer incorrect
                    {
                        print("You pick wrong param. Try again!"); //print a error message 
                    }
                } 
                else 
                {
                    print("Error! Please try again.");  //print a error message
                }
            } 
            catch (Exception e) //exception 
            {
                print("Error! Inappropriate value.");//print a error message
            }
        }
        print(of2.toString()); //print an object from our class to show how work tostring method in our class
    }
    private static void print(String string)  //making an method to easy print in programm
    {
        System.out.println(string);
    }
}
