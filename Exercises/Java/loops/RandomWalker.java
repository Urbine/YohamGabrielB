/* *****************************************************************************
 *  Name:              Alan Turing
 *  Coursera User ID:  123456
 *  Last modified:     1/1/2019
 **************************************************************************** */

public class RandomWalker {
    public static void main(String[] args) {

        int n = Integer.parseInt(args[0]);

        int x = 0;
        int y = 0;

        int randomDirection;
        int steps = 0;

        while ((Math.abs(x) + Math.abs(y)) < n) {

            randomDirection = (int) (Math.random() * 4);

            switch (randomDirection) {
                case 0:
                    y += 1;
                    break;
                case 1:
                    y -= 1;
                    break;
                case 2:
                    x += 1;
                    break;
                case 3:
                    x -= 1;
                    break;
                default:
                    continue;
            }

            steps++;

            System.out.println("(" + x + ", " + y + ")");
        }

        System.out.println("steps = " + steps);
    }
}
