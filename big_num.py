from __future__ import annotations
from typing import Generator, cast


class BigNum:
    """
    Custom class to implement decimal big number addition by using a singly linked list to represent numbers
    """

    def __init__(self, number_string: str):
        self.isNegative = False
        number_string = number_string.strip()
        if number_string.startswith('-'):
            self.isNegative = True
            number_string = number_string[1:]
        if not number_string.isdigit():
            raise ValueError('cannot interpret input string')

        digits = reversed(number_string)
        self.head = Node(next(digits))
        pointer = self.head
        for d in digits:
            pointer.next = Node(d)
            pointer = pointer.next
        self.head.handle_trailing_zeros()

    def __str__(self):
        sign = '-' if self.isNegative else ''
        pointer = self.head
        str_acc = ''
        while pointer:
            str_acc = str(pointer.digit) + str_acc
            pointer = pointer.next
        return sign + str_acc

    def __repr__(self):
        return f'BigNum(\'{str(self)}\')'

    def __len__(self):
        return self.head.len()

    def __eq__(self, other: BigNum) -> bool:
        return self.head.equal_to(other.head) and self.isNegative == other.isNegative

    def __add__(self, other: BigNum) -> BigNum:
        if self.isNegative != other.isNegative:
            return self - other.negation()
        return self.add(other)

    def __sub__(self, other: BigNum) -> BigNum:
        if self.isNegative != other.isNegative:
            return self + other.negation()
        return self.subtract(other)

    def __mul__(self, other: BigNum) -> BigNum:
        return self.multiply(other)

    def clone(self):
        return BigNum(str(self))

    def add(self, other: BigNum) -> BigNum:
        clone = self.clone()
        clone.head.add(other.head)
        return clone

    def subtract(self, other: BigNum) -> BigNum:
        if len(self) < len(other):
            clone = other.clone()
            clone = clone - self
            clone.isNegative = not clone.isNegative
            return clone

        clone = self.clone()
        flip_sign = clone.head.subtract(other.head)
        if flip_sign:
            clone.isNegative = not clone.isNegative

        clone.head.handle_trailing_zeros()
        return clone

    def negation(self) -> BigNum:
        clone = self.clone()
        clone.isNegative = not self.isNegative
        return clone

    def shift_left(self, i) -> BigNum:
        if i < 0:
            raise ValueError("negative shift count")
        elif self.isNegative:
            raise ValueError("can't shift negative number")
        elif self.head.digit == 0 and not self.head.next:
            return self.clone()

        clone = self.clone()
        while i != 0:
            new_head = Node('0')
            new_head.next = clone.head
            clone.head = new_head
            i -= 1
        return clone

    def multiply(self, other: BigNum) -> BigNum:
        base = self.clone()
        base.isNegative = False

        result = BigNum('0')

        pointer = other.head
        while pointer:
            if pointer.digit != 0:
                partial_result = base.clone()
                partial_result.head.multiply_single_digit(pointer)
                result += partial_result
            pointer = pointer.next
            base = base.shift_left(1)

        result.isNegative = self.isNegative ^ other.isNegative
        return result


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

    def len(self):
        if not self.next:
            return 1
        else:
            return 1 + self.next.len()

    def equal_to(self, other: Node) -> bool:
        """
        for implement __eq__
        """
        if self.digit != other.digit:
            return False
        if bool(self.next) != bool(other.next):
            return False
        if self.next:
            return self.next.equal_to(cast(Node, other.next))
        else:
            return True

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

    def subtract(self, other: Node) -> bool:
        """
        subtraction method. mutate in place
        """
        flip_side = False
        next_flip_sign = False
        if other.next:
            if not self.next:
                self.next = Node('0')
            next_flip_sign = self.next.subtract(other.next)

        self.digit -= other.digit
        self_flip_sign = self.digit < 0

        if self.next and not next_flip_sign and self_flip_sign:
            self.handle_borrow()
        if self.next and next_flip_sign and not self_flip_sign:
            self.handle_lend()

        if self.digit < 0:
            flip_side = True
            self.digit = abs(self.digit)

        return flip_side or next_flip_sign

    def handle_trailing_zeros(self):
        if not self.next:
            return
        self.next.handle_trailing_zeros()
        if self.next.digit == 0 and not self.next.next:
            self.next = None

    def can_be_borrowed(self):
        if self.digit >= 1:
            return True
        else:
            return self.next and self.next.can_be_borrowed()

    def handle_borrow(self):
        """
        handle borrow
        """
        if self.digit >= 0:
            return
        if not self.next or not self.next.can_be_borrowed():
            return
        borrow = self.digit // 10
        self.digit = self.digit % 10
        next = cast(Node, self.next)
        next.digit += borrow
        next.handle_borrow()

    def handle_lend(self):
        if self.digit == 0:
            return
        next = cast(Node, self.next)
        next.digit -= 1
        self.digit = 10 - self.digit
        next.handle_borrow()

    def multiply_single_digit(self, other: Node):
        self.digit *= other.digit
        if self.next:
            self.next.multiply_single_digit(other)
        self.handle_carry_over()


def gen_fib() -> Generator[BigNum, None, None]:
    # A generator of Fibonacci seq using the custom-made BigNum class
    curr = BigNum('1')
    next = BigNum('1')

    while True:
        yield curr
        curr, next = next, curr + next
