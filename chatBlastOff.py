def blast(n=5):
        if n == 0:
            print("Blast Off!")
        else:
            print(n)
            blast(n - 1)
blast()

