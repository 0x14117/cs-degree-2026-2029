// Broken.java
// DELIBERATE ERROR on line 7: printn is not a method. javac refuses to compile the file.
public class Broken {
    public static void main(String[] args) {
        System.out.println("Line 1");
        System.out.println("Line 2");
        System.out.printn("Line 3");
    }
}
