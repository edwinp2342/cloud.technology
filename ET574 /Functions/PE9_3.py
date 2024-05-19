def hello():
    print("Hello World")
def helloNo(n):
    for _ in range(n):
        hello()
helloNo(3)
