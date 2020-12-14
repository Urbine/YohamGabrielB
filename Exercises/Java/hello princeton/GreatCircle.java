/* *****************************************************************************
 *  Name:              Yoham Gabriel B
 *  Coursera User ID:  123456
 *  Last modified:     November 05, 2020
 **************************************************************************** */

public class GreatCircle {
    public static void main(String[] args) {
        final double R = 6371.0; // Radius of the earth
        double x1 = Double.parseDouble(args[0]);
        double y1 = Double.parseDouble(args[1]);
        double x2 = Double.parseDouble(args[2]);
        double y2 = Double.parseDouble(args[3]);
        double latDistance = Math.toRadians(x2 - x1);
        double lonDistance = Math.toRadians(y2 - y1);
        double a = Math.sin(latDistance / 2) * Math.sin(latDistance / 2) +
                Math.cos(Math.toRadians(x1)) * Math.cos(Math.toRadians(x2)) *
                        Math.sin(lonDistance / 2) * Math.sin(lonDistance / 2);
        double c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));
        double distance = R * c;

        System.out.println(distance + " kilometers");
    }
}
