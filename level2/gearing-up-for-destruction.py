from fractions import Fraction
def invalid_radii(first_radius, pegs):
    if first_radius < 2:
        return True

    current_radius = first_radius
    for i in range(1,n):
        current_radius = pegs[i] - pegs[i-1] - current_radius
        if current_radius < 1:
            return True

    return False
def calculate_total(n, pegs):
    total = -pegs[0]
    inner_sum = sum(2 * pegs[i] * (-1 if i % 2 == 0 else 1) for i in range(1, n - 1))
    total += inner_sum + (pegs[-1] if n % 2 == 0 else -1*pegs[-1])

    return total

def solution(pegs):
    n = len(pegs)

    if (total := calculate_total(n,pegs) <= 0:
        return [-1, -1]

    first_radius = Fraction(2 * float(total) * (1/3 if n % 2 == 0 else 1)).limit_denominator()

    if invalid_radii(first_radius, pegs):
        return [-1,-1]

    return [first_radius.numerator, first_radius.denominator]
