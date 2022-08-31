
//  Definition for singly-linked list.
class ListNode {
    int val;
    ListNode next;
    ListNode() {}
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode next) { this.val = val; this.next = next; }
}
 
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        
        int carry = 0; 
        ListNode ans = new ListNode();
        ListNode finalAnswer = ans;

        while (l1 != null || l2 != null){

            int sum =0 ;
            sum += (l1 != null)? l1.val : 0;
            sum += (l2 != null)? l2.val : 0;
            sum += carry;

            ListNode current = new ListNode(sum %10);
            
            carry = sum /10;
            ans.next = current;
            ans = ans.next;
            l1 = (l1 != null)? l1.next: null;
            l2 = (l2 != null)? l2.next: null;
            
        }


        if (carry > 0){
            ans.next = new ListNode(carry);
        }


        return finalAnswer.next;

    }
}

class myClass{
    public static void main(String[] args) {
        
        System.out.println("Hello world");
    }
}