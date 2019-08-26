from fractions import Fraction
print(Fraction(11,30))
print(Fraction(4,8))
print(Fraction())

#FRACTION INSIDE OHTER FRACTION GIVE THE SAME FRACTION
print(Fraction(Fraction(5,10)))

#CONVERT THE FLOATING INTEGER INTO FRACTION
print(Fraction(2.12))

#THAT CONVERT THE DECIMAL VALUE INTO SAME VALUE FRACTION
print(Fraction('1.13'))

#LIMIT THE DENOMINATOR
print(Fraction('3.14159264').limit_denominator(10))

#PERFORM MATHEMATICAL OPERATIONS ON FRACTION
x=Fraction(5,7)+Fraction(9,13)
print(x)

y=Fraction(9,19)*Fraction(44,13)
print(y)

z=Fraction(12,5)**(Fraction(12,10))
print(z)

W=Fraction(12,5)/Fraction(22,7)
print(W)