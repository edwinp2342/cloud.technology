import random
def message(text, times):
    """Prints the text 'times' number of times."""
    for _ in range(times):
        print(text)
def main():
    text = input("Enter a text: ")
    text = text.capitalize()
    print(f"text = {text}")
    n = random.randint(1, 10)
    print(f"n = {n}")
    message(text, n)
if __name__ == "__main__":
    main()
