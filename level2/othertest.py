import fractions

import time

# get the start time
st = time.time()


def solution(pegs):

    #making a list of differece between pegs
    d = [pegs[i+1]-pegs[i] for i in range(len(pegs)-1)]

   #checking whether there are an even or odd amount of pegs
    if len(pegs)%2 == 0:
            evenpegs = True
    elif len(pegs)%2 == 1:
            evenpegs = False
    radius = 0

    #calculating r[0] for even pegs
    if evenpegs == True:
        add = True
        for i in d:
            if add == True:
                radius = radius + i
                add = False
            elif add == False:
                radius = radius - i
                add = True
        radius = radius/1.5

    #calculating r[0] for odd pegs
    if evenpegs == False:
        add = True
        for i in d:
            if add == True:
                radius = radius + i
                add = False
            elif add == False:
                radius = radius - i
                add = True
        radius = radius/0.5

    #calculating all the gear radii
    r = [radius]
    for i in range(len(d)):
        r += [d[i] - r[i]]
    #checking none of the gears are smaller than 1, if so returning -1,-1
    for i in r:
        if i < 1:
            return -1,-1
    #turning radius of first gear into a fraction and returning numerator and denominator
    else:
        f = fractions.Fraction(radius).limit_denominator()
        return f.numerator, f.denominator



# assert solution([1,100]) == [66,1]
# assert solution([375,3850,7328,8630]) == [866,1]
# assert solution([13,130,234,327,394]) == [78,1]
# assert solution([9377,9447,9569,9646]) == [50,3]
assert solution([4,30,50]) == [12,1]
# assert solution([4, 17, 50]) == [-1,-1]
# assert solution([2,3,4,]) == [-1,-1]

# wait for 3 seconds
time.sleep(3)
et = time.time() - 3

elapsed_time = et - st
print('Execution time:', elapsed_time, 'seconds')
