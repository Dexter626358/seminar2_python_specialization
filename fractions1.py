import fractions
import random

"Парсер строки по /"
def fraction_parser(fraction: str) -> tuple:
    numerator, dominator = fraction.split("/")
    return int(numerator), int(dominator)

"Нахождение суммы дробей"
def sum_fractions(fract1: str, fract2: str) -> str:
    result = ""
    numerator1 = fraction_parser(fract1)[0]
    numerator2 = fraction_parser(fract2)[0]
    dominator1 = fraction_parser(fract1)[1]
    dominator2 = fraction_parser(fract2)[1]
    if dominator1 == dominator2:
        numerator3 = numerator1 + numerator2
        dominator3 = dominator1
        gcd = gcd_fun(numerator3, dominator3)
        if gcd != 1:
            numerator3 /= gcd
            dominator3 /= gcd
            if dominator3 != 1:
                result = str(int(numerator3)) + "/" + str(int(dominator3))
            else:
                result = str(int(numerator3))
    else:
        lcm = least_common_multiple(dominator1, dominator2)
        coeff1 = int(lcm / dominator1)
        coeff2 = int(lcm / dominator2)
        numerator3 = numerator1 * coeff1 + numerator2 * coeff2
        dominator3 = lcm
        gcd = gcd_fun(numerator3, dominator3)
        if gcd != 1:
            numerator3 /= gcd
            dominator3 /= gcd
            if dominator3 != 1:
                result = str(int(numerator3)) + "/" + str(int(dominator3))
            else:
                result = str(int(numerator3))
        else:
            result = str(int(numerator3)) + "/" + str(int(dominator3))
    return result

"Умножение дробей"
def mult_fractions(fract1: str, fract2: str):
    numerator1 = fraction_parser(fract1)[0]
    numerator2 = fraction_parser(fract2)[0]
    dominator1 = fraction_parser(fract1)[1]
    dominator2 = fraction_parser(fract2)[1]
    numerator3 = numerator1 * numerator2
    dominator3 = dominator1 * dominator2
    gcd = gcd_fun(numerator3, dominator3)
    if gcd != 1:
        numerator3 /= gcd
        dominator3 /= gcd
    if dominator3 == 1:
        result = str(int(numerator3))
    else:
        result = str(int(numerator3)) + "/" + str(int(dominator3))
    return result


"Нахождение наименьшего общего кратного"
def least_common_multiple(num1: int, num2: int):
    if num1 > num2:
        greater = num1
    else:
        greater = num2
    while True:
        if greater % num1 == 0 and greater % num2 == 0:
            lcm = greater
            break
        greater += 1
    return lcm


# нахождение наибольшего общего делителя
def gcd_fun(num1, num2):
    if num2 == 0:
        return num1
    else:
        return gcd_fun(num2, num1 % num2)


for i in range(1, 10):
        fraction1 = str(random.randint(1, 10)) + "/" + str(random.randint(1, 10))
        fraction2 = str(random.randint(1, 10)) + "/" + str(random.randint(1, 10))
        f1 = fractions.Fraction(fraction_parser(fraction1)[0], fraction_parser(fraction1)[1])
        f2 = fractions.Fraction(fraction_parser(fraction2)[0], fraction_parser(fraction2)[1])
        print(f"{fraction1} + {fraction2}")
        print(sum_fractions(fraction1, fraction2))
        print(f1 + f2)
        print(f"{fraction1} * {fraction2}")
        print(mult_fractions(fraction1, fraction2))
        print(f1 * f2)
        print()


