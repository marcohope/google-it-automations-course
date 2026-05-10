def sum_positive_nums(n):
    if n < 1:
        return 0
    return n + sum_positive_nums(n - 1)

sum_positive_nums(5)
sum_positive_nums(10)
