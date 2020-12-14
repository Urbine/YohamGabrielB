/* *****************************************************************************
 *  Name:              Yoham Gabriel
 *  Coursera User ID:  123456
 *  Last modified:     11/12/2020
 **************************************************************************** */

public class GeneralizedHarmonic {
    public static void main(String[] args) {

        int n = Integer.parseInt(args[0]);
        int r = Integer.parseInt(args[1]);

        if (n < 0) {
            n = Math.abs(n);
        }

        double resultr = 0.00;

        // double resultn = 0.00;

        for (double i = 1; i <= n; i++) {

            resultr += 1 / Math.pow(i, r);

        }

        System.out.println(resultr);

    }
}
