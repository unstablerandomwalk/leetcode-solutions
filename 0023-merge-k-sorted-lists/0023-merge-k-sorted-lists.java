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
    public ListNode mergeKLists(ListNode[] lists) {
        ArrayList<ListNode> node = new ArrayList<>();
        ArrayList<Integer> val = new ArrayList<>();
        for (ListNode head : lists) {
            if (head != null) {
                node.add(head);
                val.add(head.val);
            }
        }

        ListNode dummy = new ListNode(0);
        ListNode curr = dummy;

        while (!node.isEmpty()) {
            int minIndex = 0;
            for (int i = 1; i < val.size(); i++) {
                if (val.get(i) < val.get(minIndex)) {
                    minIndex = i;
                }
            }
            curr.next = node.get(minIndex);
            curr = curr.next;

            node.set(minIndex, node.get(minIndex).next);

            if (node.get(minIndex) != null) {
                val.set(minIndex, node.get(minIndex).val);
            } else {
                node.remove(minIndex);
                val.remove(minIndex);
            }
        }

        return dummy.next;
    }
}