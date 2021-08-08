import java.util.*;
import java.io.*;

        
public class Rip{
    static File output;
    static PrintStream stream;
    

    public static void main(String args[])throws FileNotFoundException{
        //sets up all files, scanners and printstreams
        File input = new File(args[0]);
        Scanner scan = new Scanner(input); //scans file
        Scanner in = new Scanner(System.in); //gets input for file type
        int choice = 6;

        while(choice > 5){
        System.out.println("1 for Plants \n2 for Stems \n3 for Flowers \n4 for Berries \n5 for Leaves");
        choice = in.nextInt();
        }

        switch(choice){
            case 1: output = new File("Plants.txt"); break;
            case 2 : output = new File("Stems.txt"); break; 
            case 3 : output = new File("Flowers.txt"); break;
            case 4 : output = new File("Berries.txt"); break;
            case 5 : output = new File("Leaves.txt"); break;
        }
        stream = new PrintStream(output);

        //sets base data
        String line = scan.next();
        char brac = line.charAt(0); //checks for '}' bracket at end of each data json
        line = line.substring(1);
        String data = Character.toString(brac);
        while(scan.hasNext()) {
            
            if(line.isEmpty()) {
                //if the line is gets next stream
                data = data + ' ';
                line = scan.next();
            } 
            while(brac != '}' && !line.isEmpty()){
                brac = line.charAt(0);
                line = line.substring(1);
                data = data + brac;
            }

            if(brac == '}'){ 
                //if it hits end of data, parse and resets data
                Choose(choice, data);
                if(!line.isEmpty()){
                    brac = line.charAt(0);
                    data = Character.toString(brac);
                    line = line.substring(1);
                } 
            }
        }

        scan.close();
        in.close();
        stream.close();
    }
    
    public static void Choose(int choice, String data)throws FileNotFoundException {
        switch(choice){
            case 1: ParsePlant(data); break;
            case 2 : ParseStem(data); break; 
            case 3 : ParseFlower(data); break;
            case 4 : ParseBerry(data); break;
            case 5 : ParseLeaf(data); break;
        }
    }

    public static void ParsePlant(String plant)throws FileNotFoundException {
        //10, 15, 12, 14
        plant = plant.substring(10); //take off first part
        String skipper = plant.substring(0, plant.indexOf('\"')); //grab name
        stream.println("Name: " + skipper); //print
        plant = plant.substring(skipper.length()); //take off name
        //repeat for rest of plant
        
        plant = plant.substring(16);
        skipper = plant.substring(0, plant.indexOf("\""));
        stream.println("Latin Name: " + skipper);
        plant = plant.substring(skipper.length());

        plant = plant.substring(13);
        skipper = plant.substring(0, plant.indexOf(","));
        stream.println("Native?: " + skipper);
        plant = plant.substring(skipper.length());

        stream.println("Height: ");
        
        plant = plant.substring(15);
        skipper = plant.substring(0, plant.indexOf('\"'));
        stream.println("Image: " + skipper);
        
        stream.println(); //spacing between each plant
    }
    
    public static void ParseStem(String stem)throws FileNotFoundException {
        
        stem = stem.substring(11); //take off first part
        String skipper = stem.substring(0, stem.indexOf('\"')); //grab name
        stream.println("Plant: " + skipper); //print
        stem = stem.substring(skipper.length()); //take off name
        //repeat for rest of stem

        stem = stem.substring(10); //take off first part
        skipper = stem.substring(0, stem.indexOf("\""));
        stream.println("Description: " + skipper);
        
        stream.println(); //spacing between each stem
     
    }
    
    public static void ParseFlower(String flower)throws FileNotFoundException {
        
        flower = flower.substring(11);
        String skipper = flower.substring(0, flower.indexOf("\""));
        stream.println("Plant: " + skipper);
        flower = flower.substring(skipper.length());

        flower = flower.substring(15);
        skipper = flower.substring(0, flower.indexOf(","));
        stream.println("Image: " + skipper);
        flower = flower.substring(skipper.length());

        flower = flower.substring(11);
        skipper = flower.substring(0, flower.indexOf('\"'));
        stream.println("Colors: " + skipper);
        flower = flower.substring(skipper.length());
        
        flower = flower.substring(10);
        skipper = flower.substring(0, flower.indexOf("\""));
        stream.println("Description: " + skipper);
        
        stream.println(); //spacing between each flower

    }
    
    public static void ParseBerry(String berry)throws FileNotFoundException {
        
        berry = berry.substring(11);
        String skipper = berry.substring(0, berry.indexOf("\""));
        stream.println("Plant: " + skipper);
        berry = berry.substring(skipper.length());

        berry = berry.substring(15);
        skipper = berry.substring(0, berry.indexOf(","));
        stream.println("Image: " + skipper);
        berry = berry.substring(skipper.length());

        berry = berry.substring(11);
        skipper = berry.substring(0, berry.indexOf('\"'));
        stream.println("Colors: " + skipper);
        berry = berry.substring(skipper.length());
        
        berry = berry.substring(10);
        skipper = berry.substring(0, berry.indexOf("\""));
        stream.println("Description: " + skipper);
        
        stream.println(); //spacing between each berry

    }
    
    public static void ParseLeaf(String leaf)throws FileNotFoundException {
        
        leaf = leaf.substring(11);
        String skipper = leaf.substring(0, leaf.indexOf("\""));
        stream.println("Plant: " + skipper);
        leaf = leaf.substring(skipper.length());

        leaf = leaf.substring(15);
        skipper = leaf.substring(0, leaf.indexOf(","));
        stream.println("Image: " + skipper);
        leaf = leaf.substring(skipper.length());

        leaf = leaf.substring(11);
        skipper = leaf.substring(0, leaf.indexOf('\"'));
        stream.println("Shapes: " + skipper);
        leaf = leaf.substring(skipper.length());
        
        leaf = leaf.substring(10);
        skipper = leaf.substring(0, leaf.indexOf("\""));
        stream.println("Description: " + skipper);
        
        stream.println(); //spacing between each leaf

    }

}