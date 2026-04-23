class Solution {
    public int[] findOrder(int numCourses, int[][] prerequisites) {
        int[] inDegree = new int[numCourses];
        Map<Integer, List<Integer>> graph = new HashMap<>();
        for (int[] e : prerequisites) {
            if (!graph.containsKey(e[1])) {
                graph.put(e[1], new ArrayList<>());
            }
            graph.get(e[1]).add(e[0]);
            inDegree[e[0]]++;
        }
        Stack<Integer> s = new Stack<>();
        for (int i = 0; i < numCourses; i++) {
            if (inDegree[i] == 0) {
                s.push(i);
            }
        }
        List<Integer> res = new ArrayList<>();
        while (!s.isEmpty()) {
            int u = s.pop();
            if (graph.containsKey(u)) {
                for (int v : graph.get(u)) {
                    inDegree[v]--;
                    if (inDegree[v] == 0) {
                        s.push(v);
                    }
                }
            }
            res.add(u);
        }
        if (res.size() < numCourses) {
            return new int[0];
        } else {
            return res.stream().mapToInt(i -> i).toArray();
        }
    }
}
