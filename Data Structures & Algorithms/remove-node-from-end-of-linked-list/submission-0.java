/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        int size = 0;
        ListNode c = head;
        while (c != null) {
            size++;
            c = c.next;
        }
        int m = size - n;
        if (m == 0) {
            return head.next;
        }
        ListNode prev = head;
        ListNode cur = head.next;
        int count = 1;
        while (true) {
            if (count == m) {
                prev.next = cur.next;
                return head;
            }
            prev = cur;
            cur = cur.next;
            count++;
        }
    }
}
