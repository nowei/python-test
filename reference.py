class A:
    def outer():
        m = 3
        def inner():
            print(m)
            print(4)
            m = max(m, 5)
            print(m)
        inner()

if __name__ == "__main__":
    A.outer()
    print('hi')