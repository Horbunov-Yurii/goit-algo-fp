class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head

        while current.next is not None:
            current = current.next

        current.next = new_node

    def reverse(self):
        previous = None
        current = self.head

        while current is not None:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node

        self.head = previous

    def merge_sort(self):
        self.head = self._merge_sort(self.head)

    def _merge_sort(self, head):
        if head is None or head.next is None:
            return head

        middle = self._get_middle(head)
        second_half = middle.next
        middle.next = None

        left = self._merge_sort(head)
        right = self._merge_sort(second_half)

        return self._merge(left, right)

    def _get_middle(self, head):
        slow = head
        fast = head

        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next

        return slow

    def _merge(self, left, right):
        dummy = Node(0)
        current = dummy

        while left is not None and right is not None:
            if left.data <= right.data:
                current.next = left
                left = left.next
            else:
                current.next = right
                right = right.next

            current = current.next

        if left is not None:
            current.next = left

        if right is not None:
            current.next = right

        return dummy.next

    @staticmethod
    def merge_two_sorted_lists(list1, list2):
        dummy = Node(0)
        current = dummy

        while list1 is not None and list2 is not None:
            if list1.data <= list2.data:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next

            current = current.next

        if list1 is not None:
            current.next = list1

        if list2 is not None:
            current.next = list2

        return dummy.next

    def display(self):
        current = self.head

        while current is not None:
            print(current.data, end=" -> ")
            current = current.next

        print("None")


if __name__ == "__main__":
    print("TEST 1: Reverse")

    linked_list = LinkedList()
    linked_list.append(10)
    linked_list.append(20)
    linked_list.append(30)

    linked_list.reverse()
    linked_list.display()

    print("\nTEST 2: Merge Sort")

    linked_list = LinkedList()
    linked_list.append(30)
    linked_list.append(10)
    linked_list.append(40)
    linked_list.append(20)
    linked_list.append(5)

    linked_list.merge_sort()
    linked_list.display()

    print("\nTEST 3: Merge Two Sorted Lists")

    list1 = LinkedList()
    list1.append(10)
    list1.append(30)
    list1.append(50)

    list2 = LinkedList()
    list2.append(20)
    list2.append(40)
    list2.append(60)

    merged_head = LinkedList.merge_two_sorted_lists(
        list1.head,
        list2.head
    )

    merged_list = LinkedList()
    merged_list.head = merged_head
    merged_list.display()



