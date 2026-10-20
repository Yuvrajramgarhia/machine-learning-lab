import java.util.*;

public class fs {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String startDay = sc.next().toLowerCase();
        int n = sc.nextInt();

        Map<String, Integer> dayMap = new HashMap<>();
        dayMap.put("sun", 0);
        dayMap.put("mon", 1);
        dayMap.put("tue", 2);
        dayMap.put("wed", 3);
        dayMap.put("thu", 4);
        dayMap.put("fri", 5);
        dayMap.put("sat", 6);

        int startIndex = dayMap.get(startDay);
        int sundayCount = 0;

        for (int day = 1; day <= n; day++) {
            if ((startIndex + day - 1) % 7 == 0) {
                sundayCount++;
            }
        }

        System.out.println(sundayCount);
    }
}