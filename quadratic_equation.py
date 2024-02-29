def solve_quadratic_equation(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant > 0:
        x1 = (-b + discriminant**0.5) / (2*a)
        x2 = (-b - discriminant**0.5) / (2*a)
        return x1, x2
    elif discriminant == 0:
        x = -b / (2*a)
        return x
    else:
        real_part = -b / (2*a)
        imaginary_part = (-discriminant)**0.5 / (2*a)
        x1 = complex(real_part, imaginary_part)
        x2 = complex(real_part, -imaginary_part)
        return x1, x2

# Пример использования функции
a = 1
b = -3
c = 2
result = solve_quadratic_equation(a, b, c)
print("Корни уравнения", a, "x^2 +", b, "x +", c, "= 0:", result)
