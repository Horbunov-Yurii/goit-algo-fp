import heapq


def dijkstra(graph, start):
    # Перевіряємо, чи існує початкова вершина
    if start not in graph:
        raise ValueError("Початкової вершини немає в графі")

    # Перевіряємо, чи немає від'ємних ваг
    for vertex in graph:
        for neighbor, weight in graph[vertex]:
            if weight < 0:
                raise ValueError("Алгоритм Дейкстри не підтримує від'ємні ваги")

    # Створюємо словник відстаней
    distances = {}

    for vertex in graph:
        distances[vertex] = float("inf")

    distances[start] = 0

    # Створюємо бінарну купу
    priority_queue = [(0, start)]

    while priority_queue:
        # Отримуємо вершину з найменшою відстанню
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # Пропускаємо застарілі значення
        if current_distance > distances[current_vertex]:
            continue

        # Перевіряємо сусідні вершини
        for neighbor, weight in graph[current_vertex]:
            new_distance = current_distance + weight

            # Якщо знайшли коротший шлях
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance

                # Додаємо нову відстань у бінарну купу
                heapq.heappush(
                    priority_queue,
                    (new_distance, neighbor)
                )

    return distances


def main():
    # Створюємо зважений граф
    graph = {
        "A": [("B", 4), ("C", 2)],
        "B": [("A", 4), ("C", 1), ("D", 5)],
        "C": [("A", 2), ("B", 1), ("D", 8), ("E", 10)],
        "D": [("B", 5), ("C", 8), ("E", 2)],
        "E": [("C", 10), ("D", 2)],
        "F": []
    }

    start_vertex = "A"

    # Запускаємо алгоритм Дейкстри
    distances = dijkstra(graph, start_vertex)

    # Виводимо результати
    print("Алгоритм Дейкстри")
    print(f"Початкова вершина: {start_vertex}")
    print("\nНайкоротші відстані:")

    for vertex, distance in distances.items():
        if distance == float("inf"):
            print(f"{start_vertex} -> {vertex}: шлях відсутній")
        else:
            print(f"{start_vertex} -> {vertex}: {distance}")


if __name__ == "__main__":
    main()