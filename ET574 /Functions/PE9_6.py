import random
def middle(lst):
    """Returns a new list that contains all but the first and last elements of the given list."""
    if len(lst) > 2:
        return lst[1:-1]
    else:
        return []
def main():
    n = random.randint(1, 10)
    numList = [random.randint(1, 100) for _ in range(n)]
    print(f"List length = {n}")
    print(numList)
    result = middle(numList)
    print(result)
if __name__ == "__main__":
    main()
