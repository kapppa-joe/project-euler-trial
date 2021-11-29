from __future__ import annotations


class BigNum:
    """
    Custom class to implement decimal big number addition by using a singly linked list to represent numbers
    """

    def __init__(self, number_string: str):
        number_string = number_string.strip()
        if not number_string.isdigit():
            raise ValueError('cannot interpret input string')
        self.start = Node(number_string)

    def __str__(self):
        return str(self.start)

    def clone(self):
        return BigNum(str(self))

    def add(self, other: BigNum) -> BigNum:
        clone = self.clone()
        clone.start.add(other.start)
        return clone

    def __add__(self, other: BigNum) -> BigNum:
        return self.add(other)

    def __eq__(self, other: BigNum) -> bool:
        return self.start.equal_to(other.start)


class Node:
    def __init__(self, number_string: str):
        self.digit = int(number_string[-1])
        self.next = None
        if len(number_string) > 1 and not all(char == '0' for char in number_string[:-1]):
            self.next = Node(number_string[:-1])

    def __str__(self):
        if not self.next:
            return str(self.digit)
        else:
            return str(self.next) + str(self.digit)

    def add(self, other: Node):
        """
        addition method. mutate in-place
        """
        self.digit += other.digit
        self.handle_carry_over()

        if other.next:
            if not self.next:
                self.next = Node('0')
            self.next.add(other.next)

    def handle_carry_over(self):
        """
        handle carryover
        """
        if self.digit < 10:
            return

        carry_over = self.digit // 10
        self.digit = self.digit % 10

        if not self.next:
            self.next = Node('0')
        self.next.digit += carry_over
        self.next.handle_carry_over()

    def equal_to(self, other) -> bool:
        """
        for implement __eq__
        """
        if self.digit != other.digit:
            return False
        if bool(self.next) != bool(other.next):
            return False
        if self.next:
            return self.next.equal_to(other.next)
        else:
            return True
