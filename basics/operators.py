import operator

"""
operators.py

Small demonstration of common Python operators.
Run as: python operators.py
"""

def arithmetic_ops(a, b):
    # Arithmetic
    print("ARITHMETIC:")
    print(f"{a} + {b} = {a + b}")
    print(f"{a} - {b} = {a - b}")
    print(f"{a} * {b} = {a * b}")
    print(f"{a} / {b} = {a / b}")          # true division -> float
    print(f"{a} // {b} = {a // b}")        # floor division
    print(f"{a} % {b} = {a % b}")          # modulus
    print(f"{a} ** {b} = {a ** b}")        # exponentiation
    print()


def assignment_and_augmented():
    # Assignment and augmented assignment
    print("ASSIGNMENT & AUGMENTED:")
    x = 10
    print("initial x =", x)
    x += 5
    print("x += 5 ->", x)
    x *= 2
    print("x *= 2 ->", x)

    # For mutable objects, augmented may mutate in-place
    lst = [1, 2]
    print("initial lst =", lst)
    lst += [3]            # modifies list in-place
    print("lst += [3] ->", lst)
    print()


def comparison_ops(a, b):
    # Comparison
    print("COMPARISON:")
    print(f"{a} == {b} ->", a == b)
    print(f"{a} != {b} ->", a != b)
    print(f"{a} > {b} ->", a > b)
    print(f"{a} < {b} ->", a < b)
    print(f"{a} >= {b} ->", a >= b)
    print(f"{a} <= {b} ->", a <= b)
    print()


def logical_ops(p, q):
    # Logical
    print("LOGICAL:")
    print(f"{p} and {q} ->", p and q)
    print(f"{p} or {q} ->", p or q)
    print(f"not {p} ->", not p)
    print()


def bitwise_ops(x, y):
    # Bitwise (operate on integer binary representations)
    print("BITWISE (binary):")
    print(f"{x} & {y} -> {x & y} (binary {x & y:b})")
    print(f"{x} | {y} -> {x | y} (binary {x | y:b})")
    print(f"{x} ^ {y} -> {x ^ y} (binary {x ^ y:b})")
    print(f"~{x} -> {~x} (two's complement)")
    print(f"{x} << 2 -> {x << 2} (shift left)")
    print(f"{x} >> 2 -> {x >> 2} (shift right)")
    print()


def membership_and_identity(seq, value, a, b):
    # Membership: in / not in
    print("MEMBERSHIP & IDENTITY:")
    print(f"{value} in {seq} ->", value in seq)
    print(f"{value} not in {seq} ->", value not in seq)

    # Identity: is / is not (object identity, not equality)
    c = a
    print(f"{a} is {b} ->", a is b)
    print(f"{a} is {c} ->", a is c)
    print()


def conditional_expression(n):
    # Ternary conditional
    print("CONDITIONAL (ternary):")
    sign = "positive" if n > 0 else ("zero" if n == 0 else "negative")
    print(f"{n} is {sign}")
    print()


def precedence_example():
    # Operator precedence example
    print("PRECEDENCE:")
    expr1 = 2 + 3 * 4        # multiplication before addition -> 2 + (3*4) = 14
    expr2 = (2 + 3) * 4      # parentheses change order -> (2+3)*4 = 20
    expr3 = 2 ** 3 ** 2      # right-associative exponentiation -> 2 ** (3**2) = 2**9 = 512
    print("2 + 3 * 4 =", expr1)
    print("(2 + 3) * 4 =", expr2)
    print("2 ** 3 ** 2 =", expr3)
    print()


def operator_module_demo(a, b):
    # operator module functions mirror operators (useful for functional programming)
    print("OPERATOR MODULE:")
    print("operator.add:", operator.add(a, b))
    print("operator.mul:", operator.mul(a, b))
    print("operator.eq:", operator.eq(a, b))
    print()


arithmetic_ops(7, 3)
assignment_and_augmented()
comparison_ops(7, 3)
logical_ops(True, False)
bitwise_ops(6, 3)             # 6 -> 110, 3 -> 011
membership_and_identity([1, 2, 3], 2, [1, 2], [1, 2])
conditional_expression(-5)
precedence_example()
operator_module_demo(4, 2)