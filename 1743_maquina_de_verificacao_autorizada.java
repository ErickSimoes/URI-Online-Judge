
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		int cont = 0;
		int[] x = new int[5];
		boolean b = true;
		Scanner s = new Scanner(System.in);
		for (int i = 0; i < x.length; i++) {
			x[i] = s.nextInt();
		}
		for (int i = 0; i < x.length; i++) {
			cont = s.nextInt();
			if (x[i] == cont) {
				b = false;
			}
		}
		if(b){
			System.out.println("Y");
		}else{
			System.out.println("N");
		}

	}

}