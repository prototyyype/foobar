from fractions import Fraction
def solution(pegs):
    first_radius, temp = -1, 0
    n = len(pegs)

    # Subtract first peg position from sum
    sum = -pegs[0]

    # Calculate temp, or the sum of inner peg positions (not including first and last elements)
    for i in range(1,n-1):
        temp += -2*pegs[i] if i % 2 == 0 else 2*pegs[i]


        # temp += 2*pegs[i] * (1*(i%2 != 0))

    # Add or subtract last peg position to total sum
    sum += temp + pegs[-1] if n % 2 == 0 else temp - pegs[-1]

    # sum += temp + (pegs[-1] * (1*(n%2 == 0)))

    # If sum <=0, there is no real number solution.
    if sum <= 0:
        return [-1,-1]
    else:
        first_radius = Fraction(2* float(sum) * (1/3 if n % 2 == 0 else 1)).limit_denominator()

    if first_radius < 2:
        return [-1,-1]

    # Check that all radii are at least >=1
    current_radius = first_radius
    for i in range(1,n):
        current_radius = pegs[i] - pegs[i-1] - current_radius
        if current_radius < 1:
            return [-1,-1]

    return [first_radius.numerator, first_radius.denominator]


assert solution() ==
