def main():
    # input
    try:
        n = int(input())
    except ValueError:
        raise ValueError("Input must be a natural number.")

    # range + type + odd checks
    if not 1 <= n < 1000:
        raise ValueError(
            "Input must be greater or equal to 1 and not greater than 1000."
        )
    if n % 2 == 0:
        raise ValueError("Input must be an odd number.")

    # main loop
    for i in range(1, n + 1, 2):
        print("*" * i)


if __name__ == "__main__":
    main()
