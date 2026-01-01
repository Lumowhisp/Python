def fibonacci(n):
    last = 0
    prev = 1

    if n <= 0:
        print("Invalid input")
        return
    if n == 1:
        print(last)
        return

    print(last, prev, end=" ")

    for i in range(2, n):
        curr = last + prev
        print(curr, end=" ")
        last = prev
        prev = curr
n = int(input("Enter number of terms: "))
fibonacci(n)