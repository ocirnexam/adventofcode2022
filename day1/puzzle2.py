with open('puzzle1input.txt') as input:
    arr = []
    for segment in input.read().split('\n\n'):
        arr.append(list(map(int, segment.split('\n'))))
    print(sum(sorted([sum(a) for a in arr],reverse=True)[:3]))