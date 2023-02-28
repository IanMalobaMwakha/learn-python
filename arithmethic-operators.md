# Arithmethic Operators

| Operator |           Description           | Example  | Result of Example |
| :------: | :-----------------------------: | :------: | :---------------: |
|    +     |            Addition             |  1 + 1   |         2         |
|    -     |           Subtraction           |  2 - 1   |         1         |
|    \*    |         Multiplication          |  2 \* 2  |         4         |
|    /     |            Division             |  4 / 2   |         2         |
|    %     |             Modulus             |  5 % 2   |         1         |
|    ++    |            Increment            |   1++    |         2         |
|    --    |            Decrement            |   1--    |         0         |
|   \*\*   |         Exponentiation          | 2 \*\* 2 |         4         |
|    //    | Integer Division/Floor Division |  5 // 2  |         2         |

## Addition

The addition operator is used to add two numbers together. The result of the addition is the sum of the two numbers.

Code:

```python
1 + 1
```

Result:

```shell
2
```

## Subtraction

The subtraction operator is used to subtract two numbers. The result of the subtraction is the difference of the two numbers.

Code:

```python
2 - 1
```

Result:

```shell
1
```

## Multiplication

The multiplication operator is used to multiply two numbers. The result of the multiplication is the product of the two numbers.

Code:

```python
2 * 2
```

Result:

```shell
4
```

## Division

The division operator is used to divide two numbers. The result of the division is the quotient of the two numbers.

Code:

```python
4 / 2
```

Result:

```shell
2
```

## Modulus

The modulus operator is used to get the remainder of a division. The result of the modulus is the remainder of the division.

Code:

```python
5 % 2
```

Result:

```shell
1
```

## Increment

The increment operator is used to increase the value of a number by 1. The result of the increment is the number increased by 1.

Code:

```python
1++
```

Result:

```shell
2
```

## Decrement

The decrement operator is used to decrease the value of a number by 1. The result of the decrement is the number decreased by 1.

Code:

```python
1--
```

Result:

```shell
0
```

## Exponentiation

The exponentiation operator is used to raise a number to a power. The result of the exponentiation is the number raised to the power.

Code:

```python
2 ** 2
```

Result:

```shell
4
```

## Integer Division/Floor Division

The integer division operator is used to divide two numbers and return the integer part of the quotient. The result of the integer division is the integer part of the quotient.

Code:

```python
5 // 2
```

Result:

```shell
2
```

## Order of Operations

The order of operations is the order in which operators are evaluated. The order of operations is as follows:

1. Parentheses
2. Exponentiation
3. Multiplication
4. Division
5. Modulus
6. Addition
7. Subtraction

## Examples

Code:

```python
1 + 2 * 3
```

Result:

```shell
7
```

Explanation: The multiplication is evaluated before the addition.

---

Code:

```python
(1 + 2) * 3
```

Result:

```shell
9
```

Explanation: The addition is evaluated before the multiplication.

---

Code:

```python
1 + 2 ** 3
```

Result:

```shell
9
```

Explanation: The exponentiation is evaluated before the addition.

---

Code:

```python
(1 + 2) ** 3
```

Result:

```shell
27
```

Explanation: The addition is evaluated before the exponentiation.

---

Code:

```python
1 + 2 * 3 ** 4
```

Result:

```shell
163
```

Explanation: The exponentiation is evaluated before the multiplication and the addition.

Code:

```python
(1 + 2) * 3 ** 4
```

Result:

```shell
81
```

## Explanation: The exponentiation is evaluated before the multiplication and the addition.

Code:

```python
1 + 2 * 3 // 4
```

Result:

```shell
2
```

Explanation: The integer division is evaluated before the multiplication and the addition.

---

Code:

```python
(1 + 2) * 3 // 4
```

Result:

```shell
1
```

Explanation: The integer division is evaluated before the multiplication and the addition.

---

Code:

```python
1 + 2 * 3 % 4
```

Result:

```shell
3
```

Explanation: The modulus is evaluated before the multiplication and the addition.

---

Code:

```python
(1 + 2) * 3 % 4
```

Result:

```shell
3
```

## Explanation: The modulus is evaluated before the multiplication and the addition.

Code:

```python
1 + 2 * 3 ** 4 // 5 % 6
```

Result:

```shell
3
```

## Explanation: The modulus is evaluated before the integer division, the exponentiation is evaluated before the multiplication, the integer division is evaluated before the multiplication, and the addition is evaluated before the multiplication.

Code:

```python
(1 + 2) * 3 ** 4 // 5 % 6
```

Result:

```shell
3
```

## Explanation: The modulus is evaluated before the integer division, the exponentiation is evaluated before the multiplication, the integer division is evaluated before the multiplication, and the addition is evaluated before the multiplication.

Code:

```python
1 + 2 * 3 ** 4 // 5 % 6 - 7
```

Result:

```shell
-4
```

## Explanation: The subtraction is evaluated before the modulus, the modulus is evaluated before the integer division, the exponentiation is evaluated before the multiplication, the integer division is evaluated before the multiplication, and the addition is evaluated before the multiplication.

Code:

```python
(1 + 2) * 3 ** 4 // 5 % 6 - 7
```

Result:

```shell
-4
```

## Explanation: The subtraction is evaluated before the modulus, the modulus is evaluated before the integer division, the exponentiation is evaluated before the multiplication, the integer division is evaluated before the multiplication, and the addition is evaluated before the multiplication.

Code:

```python
1 + 2 * 3 ** 4 // 5 % 6 - 7 + 8
```

Result:

```shell
4
```

Explanation: The addition is evaluated before the subtraction, the subtraction is evaluated before the modulus, the modulus is evaluated before the integer division, the exponentiation is evaluated before the multiplication, the integer division is evaluated before the multiplication, and the addition is evaluated before the multiplication.

Code:

```python
(1 + 2) * 3 ** 4 // 5 % 6 - 7 + 8
```

Result:

```shell
4
```

Explanation: The addition is evaluated before the subtraction, the subtraction is evaluated before the modulus, the modulus is evaluated before the integer division, the exponentiation is evaluated before the multiplication, the integer division is evaluated before the multiplication, and the addition is evaluated before the multiplication.
