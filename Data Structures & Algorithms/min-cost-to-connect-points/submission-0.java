class Solution {
    public int minCostConnectPoints(int[][] points) {
        // Prim's algorithm
        int n = points.length;
        boolean[] visited = new boolean[n];
        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> {
            if (a[0] != b[0]) return a[0] - b[0];
            else if (a[1] != b[1]) return a[1] - b[1];
            else return a[2] - b[2];
        });
        int countVisited = 0, totalCost = 0;
        visited[0] = true;
        for (int i = 1; i < n; i++) {
            pq.offer(new int[]{dist(points, 0, i), 0, i});
        }
        while (countVisited < n && !pq.isEmpty()) {
            int[] shortestEdge = pq.poll();
            int e = shortestEdge[0], i = shortestEdge[1], j = shortestEdge[2];
            if (visited[j]) continue;
            else {
                for (int k = 0; k < n; k++) {
                    if (k != j && !visited[k]) {
                        pq.offer(new int[]{dist(points, j, k), j, k});
                    }
                }
                totalCost += e;
                visited[j] = true;
                countVisited++;
            }
        }
        return totalCost;
    }

    int dist(int[][] points, int i, int j) {
        return Math.abs(points[i][0] - points[j][0]) + Math.abs(points[i][1] - points[j][1]);
    }
}
