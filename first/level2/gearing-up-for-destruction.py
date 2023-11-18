import time

# get the start time
st = time.time()


from fractions import Fraction
def solution(pegs):
     # This function uses the following variables: n,pegs to calculate the sum of twice the
     # positive or negative of the inner peg positions plus or minus the first and last positions
    def calculate_total():
        inner_sum = sum(2 * pegs[i] * (-1 if i % 2 == 0 else 1) for i in range(1, n - 1))
        total_sum = -pegs[0] + inner_sum + (pegs[-1] if n % 2 == 0 else -1*pegs[-1])

        return total_sum

     # This function uses the formula "2*total*(1/3 if n%2==0 else 1)" to calculate the first radius.
    def calculate_first_radius():
        # print("total:",total) #TODO: remove
        # The variable "total" should be a positive integer.
        int_radius = 2 * total

        if n%2 != 0:
            return Fraction(int_radius).limit_denominator()
        else:
            frac_radius = Fraction(int_radius / 3).limit_denominator()

        # frac_radius = Fraction(2 * float(total) * (1/3 if n % 2 == 0 else 1)).limit_denominator()
        return frac_radius

     # This function checks that the first gear radius is not less than 2 and that every
     # gear radius is not less than 1.
    def invalid_radii(): #n,first_radius,pegs
        if first_radius < 2:
            return True

        current_radius = first_radius
        for i in range(1,n):
            current_radius = pegs[i] - pegs[i-1] - current_radius
            if current_radius < 1:
                return True
        return False

    # Main Function
    n = len(pegs)
    total = calculate_total()

    # print("even" if n%2 == 0 else "odd") #TODO: remove
    if total <= 0:
        # print("total <=0") #TODO: remove
        return [-1, -1]

    first_radius = calculate_first_radius()
    # print("first radius:",first_radius) #TODO: remove

    if invalid_radii():
        # print("invalid radii") #TODO: remove
        return [-1,-1]

    return [first_radius.numerator, first_radius.denominator]


assert solution([1,100]) == [66,1]
assert solution([375,3850,7328,8630]) == [866,1]
assert solution([13,130,234,327,394]) == [78,1]
assert solution([9377,9447,9569,9646]) == [50,3]
assert solution([4,30,50]) == [12,1]
assert solution([4, 17, 50]) == [-1,-1]
assert solution([2,3,4,]) == [-1,-1]


# wait for 3 seconds
time.sleep(3)
et = time.time() - 3

elapsed_time = et - st
print('Execution time:', elapsed_time, 'seconds')
