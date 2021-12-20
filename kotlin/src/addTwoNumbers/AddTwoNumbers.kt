package addTwoNumbers

class ListNode(var `val`: Int) {
    var next: ListNode? = null
}

class Solution {
    fun addTwoNumbers(l1: ListNode?, l2: ListNode?): ListNode? {
        var l1curr = l1
        var l2curr = l2
        var carry = 0
        var head = ListNode(0)
        var tail = head
        while (l1curr != null || l2curr != null || carry != 0) {
            val reg1 = l1curr?.`val` ?: 0
            val reg2 = l2curr?.`val` ?: 0

            val total = reg1 + reg2 + carry
            carry = total / 10
            val remainder = total % 10

            val newNode = ListNode(remainder)

            tail.next = newNode
            tail = newNode

            l1curr = l1curr?.next
            l2curr = l2curr?.next
        }

        return head.next // Head is actually a temporary node, makes the above code simpler.
    }
}

fun main() {
    val s = Solution()
    val l1 = ListNode(1)
    val l2 = ListNode(2)
    val l3 = ListNode(3)
    l1.next = l2
    l2.next = l3

    val k1 = ListNode(4)
    val k2 = ListNode(5)
    val k3 = ListNode(6)
    k1.next = k2
    k2.next = k3

    println(s.addTwoNumbers(l1, k1))
}