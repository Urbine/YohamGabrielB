/**
 * Write a description of Part2 here.
 *
 * @author (your name)
 * @version (a version number or a date)
 */
public class Part2 {
    /**
     * Method howMany
     *
     * @param stringA A parameter
     * @param stringB A parameter
     * @return The return value
     * <p>
     * Write the method named howMany that has two String
     * parameters named stringa and stringb. This method returns an integer indicating
     * how many times stringa appears in stringb, where each occurrence of stringa
     * must not overlap with another occurrence of it.
     * <p>
     * For example, the call howMany(“GAA”, “ATGAACGAATTGAATC”) returns 3 as GAA occurs 3
     * times. The call howMany(“AA”, “ATAAAA”) returns 2.
     * Note that the AA’s found cannot overlap.
     */
    public int howMany(String stringA, String stringB) {
        int result = 0;
        int firstIndex = stringB.indexOf(stringA);
        while (firstIndex != -1) {
            result = result + 1;
            firstIndex = stringB.indexOf(stringA, firstIndex);
        }


        return result;
    }

    public void testHowMany() {
        System.out.println("++++++ Testing howMany() ++++++");
        String a;
        String b;
        a = "GAA";
        b = "ATGAACGAATTGAATC";
        int x = howMany(a, b);
        System.out.println("How many?" + x);

        a = "AA";
        //   012345
        b = "ATAAAA";
        int y = howMany(a, b);
        System.out.println("How many?" + y);

        hy = "Gt" + "sdd";
    }

    public static void main(String[] args) {
        Part2 p2 = new Part2();
        p2.testHowMany();
    }
}
