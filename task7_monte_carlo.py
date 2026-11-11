import random
import matplotlib.pyplot as plt
from collections import Counter


def monte_carlo_simulation(number_of_rolls):
    results = Counter()

    for _ in range(number_of_rolls):
        # Кидаємо два кубики
        dice_1 = random.randint(1, 6)
        dice_2 = random.randint(1, 6)

        # Обчислюємо суму двох кубиків
        total = dice_1 + dice_2

        results[total] += 1

    # Обчислюємо ймовірності
    probabilities = {}

    for total in range(2, 13):
        probabilities[total] = (
            results[total] / number_of_rolls * 100
        )

    return results, probabilities


def calculate_theoretical_probabilities():
    probabilities = {}

    # У двох кубиків є 36 можливих комбінацій
    total_combinations = 36

    for total in range(2, 13):
        combinations = 0

        for dice_1 in range(1, 7):
            for dice_2 in range(1, 7):
                if dice_1 + dice_2 == total:
                    combinations += 1

        probabilities[total] = (
            combinations / total_combinations * 100
        )

    return probabilities


def main():
    number_of_rolls = 100000

    print("Метод Монте-Карло")
    print("Кількість кидків:", number_of_rolls)

    # Виконуємо симуляцію
    results, monte_carlo_probabilities = monte_carlo_simulation(
        number_of_rolls
    )

    # Обчислюємо теоретичні ймовірності
    theoretical_probabilities = calculate_theoretical_probabilities()

    print("\nРезультати моделювання:")
    print("-" * 65)
    print(
        f"{'Сума':<10}"
        f"{'Кількість':<15}"
        f"{'Монте-Карло':<18}"
        f"{'Теоретична':<15}"
    )
    print("-" * 65)

    for total in range(2, 13):
        print(
            f"{total:<10}"
            f"{results[total]:<15}"
            f"{monte_carlo_probabilities[total]:.2f}%"
            f"{'':<12}"
            f"{theoretical_probabilities[total]:.2f}%"
        )

    # Створюємо дані для графіка
    sums = list(range(2, 13))

    monte_carlo_values = [
        monte_carlo_probabilities[total]
        for total in sums
    ]

    theoretical_values = [
        theoretical_probabilities[total]
        for total in sums
    ]

    # Будуємо графік
    x = range(len(sums))
    width = 0.35

    plt.figure(figsize=(11, 6))

    plt.bar(
        [value - width / 2 for value in x],
        monte_carlo_values,
        width,
        label="Монте-Карло"
    )

    plt.bar(
        [value + width / 2 for value in x],
        theoretical_values,
        width,
        label="Теоретична ймовірність"
    )

    plt.xticks(x, sums)
    plt.xlabel("Сума двох кубиків")
    plt.ylabel("Ймовірність (%)")
    plt.title("Порівняння ймовірностей методом Монте-Карло")
    plt.legend()
    plt.grid(axis="y", alpha=0.3)

    plt.show()


if __name__ == "__main__":
    main()
