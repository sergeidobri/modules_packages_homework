import matplotlib.pyplot as plt
from datetime import datetime
from application.salary import calculate_salary
from application.db.people import get_employees

def main():
    print(datetime.now())

    x, y = [], []

    for employee in get_employees():
        x.append(employee)
        y.append(calculate_salary(employee))
        print(f"{x[-1]}: з/п {y[-1]} рублей")
    
    plt.bar(x, y, label="Ожидаемые заработные платы")
    plt.xlabel("Рабочий")
    plt.ylabel("Зар. плата")
    plt.title("Диаграмма")
    plt.legend()
    plt.show()

if __name__ == '__main__':
    main()
