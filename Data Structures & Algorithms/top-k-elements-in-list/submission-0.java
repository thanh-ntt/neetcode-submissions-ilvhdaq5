class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        HashMap<Integer, Integer> frequencies = new HashMap<>();
        for (int a : nums) {
            if (!frequencies.containsKey(a)) {
                frequencies.put(a, 0);
            }
            frequencies.put(a, frequencies.get(a) + 1);
        }
        List<Pair> freqPairs = new ArrayList<>();
        for (Map.Entry<Integer, Integer> entry : frequencies.entrySet()) {
            Pair freq = new Pair(entry.getKey(), entry.getValue());
            freqPairs.add(freq);
        }
        PriorityQueue<Pair> pq = new PriorityQueue<>(freqPairs);
        int[] res = new int[k];
        int i = 0;
        while (i < k) {
            res[i] = pq.poll().num;
            i++;
        }
        return res;
    }
}

public class Pair implements Comparable<Pair> {
    int num;
    int freq;
    public Pair(int num, int freq) {
        this.num = num;
        this.freq = freq;
    }
    @Override
    public int compareTo(Pair other) {
        if (this.freq != other.freq) {
            return Integer.compare(other.freq, this.freq);
        }
        return Integer.compare(other.num, this.num);
    }
}
