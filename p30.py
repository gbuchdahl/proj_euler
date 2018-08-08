def main():
    nums = range(2, 1000000)
    checked_nums = filter(lambda x: check_pow_sum(x, 5), nums)
    print("Total: {}".format(sum(checked_nums)))

def check_pow_sum(num, pow):
    numbers = list(str(num))
    ints_to_pow = map(lambda x: (int(x))**pow, numbers)
    return sum(ints_to_pow) == num

if __name__ == "__main__":
    main()