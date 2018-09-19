/*  Turner Atwood
 *  4/12/18
 *  Digit Sum [5.9]: (https://open.kattis.com/problems/digitsum)
 */ 

import java.util.*;
import java.lang.*;

class DigitSum {

    static long[][] DPTable;

    public static void main(String args[]) {
        buildTable();

        //Run DigitSum
        Scanner in = new Scanner(System.in);
        long num = in.nextLong();
        for (int z = 0; z < num; z++) {
            long inp1 = in.nextLong() - 1;
            long inp2 = in.nextLong();
            System.out.println(sumDig(inp2) - sumDig(inp1));
        }
    }

    static long sumDig(long input) {
        if (input <= 0) {
            return 0;
        }
        if (input/10 == 0) {
            return (DPTable[0][(int)input-1]);
        }
        long sum = 0;
        String inputString = Long.toString(input);
        int leng = inputString.length();
        long power = (long)Math.pow(10,leng-1);
        long firstDigit = input/power;
        long smallerNum = input%power;
        sum += DPTable[leng-1][(int)firstDigit-1];
        sum += firstDigit*(smallerNum);
        sum += sumDig(smallerNum);
        return sum;
    }

    static void buildTable() {
        DPTable = new long[17][9];
        DPTable[0][0] = 1;
        DPTable[1][0] = 46;

        //First Row
        for (int i = 1; i < 9; i++) {
            DPTable[0][i] = DPTable[0][i-1] + (i+1);
        }

        //First column
        long power = 10;
        for (int i = 2; i < 17; i++) {
            DPTable[i][0] = 10*(DPTable[i-1][0]-1) + power*45 + 1;
            power *= 10;
        }

        //Fill in the rest
        power = 10;
        for (int i = 1; i < 17; i++) {
            for (int j = 1; j < 9; j++) {
                DPTable[i][j] = (j+1)*(DPTable[i][0]-1) + power*DPTable[0][j-1] + (j+1);
            }
            power *= 10;
        }
    }
}