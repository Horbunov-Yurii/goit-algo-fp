def greedy_algorithm(items, budget):
    # Сортуємо продукти за співвідношенням калорій до вартості
    sorted_items = sorted(
        items.items(),
        key=lambda item: item[1]["calories"] / item[1]["cost"],
        reverse=True
    )

    total_cost = 0
    total_calories = 0
    selected_items = []

    for name, data in sorted_items:
        if total_cost + data["cost"] <= budget:
            selected_items.append(name)
            total_cost += data["cost"]
            total_calories += data["calories"]

    return selected_items, total_calories, total_cost


def dynamic_programming(items, budget):
    # Отримуємо назви продуктів
    names = list(items.keys())

    number_of_items = len(names)

    # Створюємо таблицю для збереження результатів
    dp = [
        [0 for _ in range(budget + 1)]
        for _ in range(number_of_items + 1)
    ]

    # Заповнюємо таблицю
    for i in range(1, number_of_items + 1):
        name = names[i - 1]

        cost = items[name]["cost"]
        calories = items[name]["calories"]

        for current_budget in range(budget + 1):
            # Не беремо поточний продукт
            dp[i][current_budget] = dp[i - 1][current_budget]

            # Перевіряємо, чи можемо взяти продукт
            if cost <= current_budget:
                new_calories = (
                    dp[i - 1][current_budget - cost] + calories
                )

                dp[i][current_budget] = max(
                    dp[i][current_budget],
                    new_calories
                )

    # Відновлюємо вибрані продукти
    selected_items = []
    current_budget = budget

    for i in range(number_of_items, 0, -1):
        if dp[i][current_budget] != dp[i - 1][current_budget]:
            name = names[i - 1]

            selected_items.append(name)
            current_budget -= items[name]["cost"]

    selected_items.reverse()

    total_cost = sum(
        items[name]["cost"]
        for name in selected_items
    )

    total_calories = dp[number_of_items][budget]

    return selected_items, total_calories, total_cost


def main():
    # Список продуктів
    items = {
        "pizza": {"cost": 50, "calories": 300},
        "hamburger": {"cost": 40, "calories": 250},
        "hot-dog": {"cost": 30, "calories": 200},
        "pepsi": {"cost": 10, "calories": 100},
        "cola": {"cost": 15, "calories": 120},
        "potato": {"cost": 25, "calories": 150}
    }

    budget = 100

    print("Бюджет:", budget)

    # Запускаємо жадібний алгоритм
    greedy_items, greedy_calories, greedy_cost = greedy_algorithm(
        items,
        budget
    )

    print("\nЖадібний алгоритм:")
    print("Вибрані продукти:", greedy_items)
    print("Загальна вартість:", greedy_cost)
    print("Загальна кількість калорій:", greedy_calories)

    # Запускаємо динамічне програмування
    dp_items, dp_calories, dp_cost = dynamic_programming(
        items,
        budget
    )

    print("\nДинамічне програмування:")
    print("Вибрані продукти:", dp_items)
    print("Загальна вартість:", dp_cost)
    print("Загальна кількість калорій:", dp_calories)


if __name__ == "__main__":
    main()
