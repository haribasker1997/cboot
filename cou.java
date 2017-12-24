package king;
import java.util.Scanner;
public class CountSeven {
	public static void main(String[]args){
		Scanner read=new Scanner(System.in);
		int n=read.nextInt();
		int count=0;
		if(n>0){
		int r=n%10;
		n=n/10;
			if(r==7){
				count++;
			}
		}
		 if(n>0){
			int r1=n%10;
			n=n/10;
			if(r1==7){
			count++;
		}
		 }
		 if(n>=1){
			 int r2=n%10;
			 n=n/10;
			 if(r2==7){	
			 count++;
			 }
		 }
			 System.out.println(count);	
	}
}
