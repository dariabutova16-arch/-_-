def calculate_salary(hours, rate):
    if hours <= 40:
        salary = hours * rate
    else:
        salary = 40 * rate + (hours - 40) * rate * 1.5
    return salary


def main():
    hours = float(input("Введіть кількість відпрацьованих годин: "))
    rate = float(input("Введіть погодинну ставку: "))

    result = calculate_salary(hours, rate)

    print(f"Заробітна плата: {result} грн")


main()
