package banking;
import java.util.Random;
import java.util.Scanner;
import java.util.HashMap; 

    class Account {
        String cardNum;
        String pin;
        int bal = 0;
        Boolean status = false;
        
        void generateCard() {
            generateCardNum();
            generatePin();
            
        }
        
        void generateCardNum() {
            String bin = "400000";
            
            // generating account ID
            Random rand = new Random();
            String accId = String.format("%09d", rand.nextInt(1000000000));
            
            String checksum = "0";
            
            cardNum = bin + accId + checksum;
        }
        
        public String getCardNum() {
            return cardNum;
        }
        
        void generatePin() {
            Random rand = new Random();
            pin = String.format("%04d", rand.nextInt(10000));
        }
        
        public String getPin() {
            return pin;
        }
        
        public String getMenu() {
            if (status == false) {
                return "1. Create an account\n2. Log into account\n0. Exit\n";
            }
            else {
                return "1. Balance\n2. Log out\n0. Exit\n";
            }
        }
    }

public class Main {
    public static void main(String[] args) {
        HashMap<String, String> allCards = new HashMap<String, String>();
        
        String createAcc = "1. Create an account";
        String logIn = "2. Log into account";
        String exit = "0. Exit";
        
        Account acc = new Account();
        System.out.println(acc.getMenu());
        
        Scanner sc = new Scanner(System.in);
        int nextIn = -1;
        
        while(nextIn != 0) {
            System.out.println(acc.getMenu());
            nextIn = sc.nextInt();
            switch (nextIn) {
                case 0:
                    System.out.println("Bye!");
                    break;
                case 1:
                    acc.generateCard();
                    allCards.put(acc.getCardNum(), acc.getPin());
                    System.out.println("Your card has been created\nYour card number:");
                    System.out.println(acc.getCardNum());
                    System.out.printf("%s", "Your card PIN:\n");
                    System.out.printf("%s\n\n", acc.getPin());
                    break;
                case 2:
                    if (acc.status == false) {
                        System.out.println("Enter your card number:");
                        String userCardNum = sc.next();
                        if (allCards.get(userCardNum) != null) {
                            System.out.println("Enter your pin:");
                            String userPin = sc.next();
                            String checkVal = allCards.get(userCardNum);
                            if (checkVal.equals(userPin)) {
                                System.out.println("You have successfully logged in!\n");
                                acc.status = true;
                                break;
                            }
                        }
                    }
                    else if (acc.status == true) {
                        acc.status = false;
                        break;
                    }
            }
        }
    }
}