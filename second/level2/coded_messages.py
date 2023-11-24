def solution(l, t):
    left, total = 0,0

    for right, num in enumerate(l):
        total += num

        while total > t:
            total -= l[left]
            left += 1

        if total == t:
            return [left, right]

    return [-1, -1]
