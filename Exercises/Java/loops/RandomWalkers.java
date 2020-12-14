/* *****************************************************************************
 *  Name:              Alan Turing
 *  Coursera User ID:  123456
 *  Last modified:     1/1/2019
 **************************************************************************** */


public class RandomWalkers {
    public static void main(String[] args) {
        int nsteps = Integer.parseInt(args[0]);
        int attempts = Integer.parseInt(args[1]);


        int randomDirection;
        double steps = 0;


        for (int i = 0; i < attempts; i++) {

            int x = 0;
            int y = 0;

            while ((Math.abs(x) + Math.abs(y)) < nsteps) {

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
            }


        }

        double avg = steps / attempts;

        System.out.printf("average number of steps = %.5f", avg);

    }
}
