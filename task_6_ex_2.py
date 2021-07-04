"""
Create CustomList – the linked list of values of random type, which size changes dynamically and has an ability to index
elements.

The task requires implementation of the following functionality:
• Create the empty user list and the one based on enumeration of values separated by commas. The elements are stored
in form of unidirectional linked list. Nodes of this list must be implemented in class Item.
    Method name: __init__(self, *data) -> None;
• Add and remove elements.
    Method names: append(self, value) -> None - to add to the end,
                add_start(self, value) -> None - to add to the start,
                remove(self, value) -> None - to remove the first occurrence of given value;
• Operations with elements by index. Negative indexing is not necessary.
    Method names: __getitem__(self, index) -> Any,
                __setitem__(self, index, data) -> None,
                __delitem__(self, index) -> None;
• Receive index of predetermined value.
    Method name: find(self, value) -> Any;
• Clear the list.
    Method name: clear(self) -> None;
• Receive lists length.
    Method name: __len__(self) -> int;
• Make CustomList iterable to use in for-loops;
    Method name: __iter__(self);
• Raise exceptions when:
    find() or remove() don't find specific value
    index out of bound at methods __getitem__, __setitem__, __delitem__.


Notes:
    The class CustomList must not inherit from anything (except from the object, of course).
    Function names should be as described above. Additional functionality has no naming requirements.
    Indexation starts with 0.
    List length changes while adding and removing elements.
    Inside the list the elements are connected as in a linked list, starting with link to head.
"""


class Item:
    """
    A node in a unidirectional linked list.
    """
    def __init__(self, *data):
        self.data = data
        self.next = None


class CustomList:
    """
    An unidirectional linked list.
    """
    def __init__(self, *data):
        self.data = data
        self.head = None

    def append(self, item):
        node = Item(item)
        if self.head is None:
            self.head = node
        else:
            cur = self.head
            while cur.next is not None:
                cur = cur.next
            cur.next = node

    def add_start(self, item):
        node = Item(item)
        node.next = self.head
        self.head = node

    def remove(self, item):
        cur = self.head
        pre = None
        while cur is not None:
            if cur.elem == item:
                if pre is None:
                    self.head = cur.next
                else:
                    pre.next = cur.next
                break
            else:
                pre = cur
                cur = cur.next
        raise IndexError

    def __len__(self):
        temp = self.head
        count = 0
        while temp:
            count += 1
            temp = temp.next
        return count

    def __getitem__(self, index):
            cur = self.head
            i = 0
            while cur is not None:
                if i == index:
                    return cur
                else:
                    cur = cur.next
                    i += 1
            raise ValueError

    def __setitem__(self, index, data):
        if index == 1:
            new_node = Item(data)
            new_node.next = self.head
            self.head = new_node
        i = 1
        n = self.head
        while i < index - 1 and n is not None:
            n = n.next
            i = i + 1
        if n is None:
            raise IndexError
        else:
            new_node = Item(data)
            new_node.next = n.next
            n.next = new_node

    def __delitem__(self, index):
        count = 0
        cur = self.head
        while count < index - 1:
            count += 1
            cur = cur.next
        del cur

    def find(self, x):
        n = self.head
        i = 0
        while n is not None:
            if n.data == x:
                return i
            i += 1
            n = n.next
        raise ValueError

    def __iter__(self):
        temp = self.head
        while temp is not None:
            yield temp.data
            temp = temp.next

    def clear(self):
        current = self.head
        while current:
            prev = current.next
            del current.data
            current = prev
