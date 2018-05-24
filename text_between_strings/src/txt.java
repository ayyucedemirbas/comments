import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.util.*;
import java.io.*;


public class txt {
	public static void main(String[] args) throws FileNotFoundException{
		String pattern1 = "'";
		String pattern2 = "'";
		String text ="";
		int counter=0;
		File f= new File("/home/ayyuce/Desktop/yorumlar2.txt");
		File f1= new File("/home/ayyuce/Desktop/ex2.txt");
		Scanner s= new Scanner(f);
		PrintWriter pw= new PrintWriter(f1);
		
		while(s.hasNextLine()){
			text=s.nextLine();
			Pattern p = Pattern.compile(Pattern.quote(pattern1) + "(.*?)" + Pattern.quote(pattern2));
			Matcher m = p.matcher(text);
			while (m.find()) {
			  System.out.println(m.group(1));
			  counter++;
			  pw.println(m.group(1));
			}
		}
       s.close();
       pw.close();
       System.out.println(counter);
		
	}

}
