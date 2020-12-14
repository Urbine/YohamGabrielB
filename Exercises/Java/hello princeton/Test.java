/* *****************************************************************************
 *  Name:              Ada Lovelace
 *  Coursera User ID:  123456
 *  Last modified:     October 16, 1842
 **************************************************************************** */

public class Test {
    public static void main(String[] args) {

        int n = 123456789;
        int m = 0;
        while (n != 0) {
            m = (10 * m) + (n % 10);
            n = n / 10;
        }
        System.out.println(m);

        int a = 3;
        int b = 2;
        int c = 4;
        if (a < b) {
            if (b < c) {
                if (c < a) System.out.println(a + " " + b + " " + c);
                else System.out.println(c + " " + b + " " + a);
            }
            else System.out.println(a + " " + c + " " + b);
        }
        else System.out.println(b + " " + a + " " + c);


    }
}

