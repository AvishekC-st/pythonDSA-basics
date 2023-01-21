import random

random.seed("ABC")


def


def main():
    array = [random.randint(0, 1000) for _ in range(100)]
    print("Original array:", array)

    merge_sort(array)
    print("Sorted array:", array)


if __name__ == "__main__":
    main()
