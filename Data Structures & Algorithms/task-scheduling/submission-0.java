class Solution {
    public int leastInterval(char[] tasks, int n) {
        int[] count = new int[26];
        for (char t : tasks) {
            count[t - 'A']++;
        }
        int maxCount = 0;
        int numMaxTask = 0;
        for (int c : count) {
            if (c > maxCount) {
                maxCount = c;
                numMaxTask = 1;
            } else if (c == maxCount) {
                numMaxTask++;
            }
        }
        System.out.println("maxCount " + maxCount + ", numMaxTask " + numMaxTask);
        return Math.max((maxCount - 1) * (n + 1) + numMaxTask, tasks.length);
    }
}
