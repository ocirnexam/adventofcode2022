with open('puzzle1input.txt') as input:
    arr = []
    for segment in input.read().split('\n\n'):
        arr.append(list(map(int, segment.split('\n'))))
    print(max(sum(a) for a in arr))
