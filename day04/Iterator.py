it = iter([1,2,3,4,5])

while True:
    try:
        x = next(it)
    except StopIteration:
        break