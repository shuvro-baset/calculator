from fractions import Fraction

class F:
    def frac():
        uinput = str(input('user input: ')) #can't literal in 'int'
        print(Fraction(uinput))#.limit_denominator(1000),limit_denominator(max_denominator=1000000)

F.frac()
