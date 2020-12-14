/* *****************************************************************************
 *  Name:              Yoham Gabriel
 *  Coursera User ID:  123456
 *  Last modified:     November 3, 2020
 **************************************************************************** */

public class RightTriangle {

    public static void main(String[] args) {
        int a = Integer.parseInt(args[0]);
        int b = Integer.parseInt(args[1]);
        int c = Integer.parseInt(args[2]);
        // boolean validityCheck;
        // validityCheck = (a < b && b < c);
        boolean notNegative;
        notNegative = (a > 0 && b > 0 && c > 0);

        double csqrt = Math.sqrt(a + b);
        double bsqrt = Math.sqrt(a + c);
        double asqrt = Math.sqrt(b + c);


        boolean eval1 = ((int) csqrt == c);
        boolean eval2 = ((int) bsqrt == b);
        boolean eval3 = ((int) asqrt == a);
        boolean eval4 = (a * a + b * b == c * c) ||
                (a * a + c * c == b * b) || (b * b + c * c == a * a);

        boolean result = notNegative && (eval1 || eval2 || eval3) && eval4;
        System.out.println(result);
    }
}

