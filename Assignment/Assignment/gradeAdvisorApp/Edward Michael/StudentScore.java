import java.util.Scanner;
public class StudentScore {
public static void main(String[] args) {
Scanner scanner = new Scanner(System.in);
	

main();


   }





	public static int score(int number){

System.out.println("Enter Score");
int score = scanner.nextInt();
System.out.println(score);
if (score > 100 || score < 0)  {
return "Invalid score, enter a value between 0 and 100";
return score;
}


public static string grade(int score){

 if (score >= 80){

 return "Grade A :Excellent performance!";

    } else if (score >= 65){

	  return "Grade B : Good job, keep improving!";
 } else if (score >= 50) {
    return "Grade C : Fair, More Effort!";
} else if (score <= 40) {

 return "Grade D : poor performance, seek help!";
}
else {
 return "You can do better, keep studying";
 }

public static int retry(int score){
System.out.println("Try another score? Yes/No: ");
String retryInput = scanner.next();
	  if (retryInput.equalsIgnoreCase("Yes")) {
		return score();
}
public static void main (){
score(int number);
grade(int score);
retry(int score);
}

}


}