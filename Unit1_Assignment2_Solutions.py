
# Unit 1 Assignment 2 - Data Types, Strings, Loops in Python
# Solutions to 30 Practice Questions

# 1. Sum of all elements in a list
nums = [1, 2, 3, 4, 5]
print("1. Sum:", sum(nums))

# 2. Print the third element of a tuple
t = (10, 20, 30, 40, 50)
print("2. Third element:", t[2])

# 3. Common elements between two sets
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print("3. Common elements:", a & b)

# 4. Dictionary of fruits and quantities
fruits = {"apple": 10, "banana": 5, "orange": 8}
print("4. Fruits dictionary:", fruits)

# 5. Check if a string is palindrome
s = "madam".lower()
print("5. Palindrome:", "Yes" if s == s[::-1] else "No")

# 6. Print numbers 1 to 10 (for loop)
print("6. Numbers 1-10:")
for i in range(1, 11):
    print(i, end=" ")
print()

# 7. Even numbers from 1 to 20 (while loop)
print("7. Even numbers 1-20:")
i = 1
while i <= 20:
    if i % 2 == 0:
        print(i, end=" ")
    i += 1
print()

# 8. Find maximum and minimum
nums = [2, 7, 1, 9, 5]
print("8. Max:", max(nums), "Min:", min(nums))

# 9. Remove duplicates from a list
nums = [1, 2, 2, 3, 4, 4, 5]
nums = list(set(nums))
print("9. Without duplicates:", nums)

# 10. Sort list of strings alphabetically
words = ["banana", "apple", "cherry"]
print("10. Sorted:", sorted(words))

# 11. Multiply each element by 2
nums = [1, 4, 70, 3, 2]
print("11. Doubled list:", [n * 2 for n in nums])

# 12. Count occurrences of each element
nums = [1, 1, 4, 70, 43, 4, 2, 4]
count = {n: nums.count(n) for n in nums}
print("12. Element count:", count)

# 13. Dictionary with squares 1–5
squares = {x: x**2 for x in range(1, 6)}
print("13. Squares:", squares)

# 14. Filter even numbers
nums = [1, 2, 3, 4, 5, 6]
evens = [n for n in nums if n % 2 == 0]
print("14. Even numbers:", evens)

# 15. Count vowels in a string
s = "Adam".lower()
vowels = "aeiou"
count = sum(1 for ch in s if ch in vowels)
print("15. Vowels in string:", count)

# 16. Tuple unpacking
t = (10, 20, 30)
a, b, c = t
print("16. Unpacked:", a, b, c)

# 17. Count words in a sentence
sentence = "Python is fun"
print("17. Word count:", len(sentence.split()))

# 18. Find the longest name
names = ["Adam", "Julie", "Alexander"]
print("18. Longest name:", max(names, key=len))

# 19. Set of first five prime numbers
primes = {2, 3, 5, 7, 11}
print("19. Prime numbers set:", primes)

# 20. Product of all elements in a list
def product(lst):
    p = 1
    for n in lst:
        p *= n
    return p
print("20. Product:", product([2, 3, 4]))

# 21. Find the shortest string
words = ["dog", "elephant", "cat"]
print("21. Shortest string:", min(words, key=len))

# 22. Check if number is prime
n = 7
is_prime = n > 1 and all(n % i != 0 for i in range(2, int(n**0.5)+1))
print("22. Is prime:", is_prime)

# 23. Dictionary of squares (1–5)
d = {i: i**2 for i in range(1, 6)}
print("23. Squares dictionary:", d)

# 24. Reverse a string (2 methods)
def reverse1(s): return s[::-1]
def reverse2(s):
    rev = ""
    for ch in s:
        rev = ch + rev
    return rev
print("24. Reverse1:", reverse1("hello"))
print("24. Reverse2:", reverse2("world"))

# 25. Common elements between two lists
a = [1, 2, 3, 4]
b = [3, 4, 5, 6]
common = [x for x in a if x in b]
print("25. Common list:", common)

# 26. FizzBuzz
print("26. FizzBuzz:")
for i in range(1, 51):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

# 27. Average of list
nums = [10, 20, 30, 40]
print("27. Average:", sum(nums)/len(nums))

# 28. Reverse words in a sentence
sentence = "I love Python"
words = sentence.split()
print("28. Reversed sentence:", " ".join(words[::-1]))

# 29. Longest and shortest strings
words = ["apple", "kiwi", "banana"]
print("29. Longest:", max(words, key=len))
print("29. Shortest:", min(words, key=len))

# 30. Prime numbers between 1 and 100
print("30. Prime numbers 1-100:")
for n in range(2, 101):
    if all(n % i != 0 for i in range(2, int(n**0.5)+1)):
        print(n, end=" ")
print()
