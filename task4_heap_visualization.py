import heapq
import math
import matplotlib.pyplot as plt
import networkx as nx


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def build_tree(heap, index=0):
    if index >= len(heap):
        return None

    node = Node(heap[index])

    # Індекс лівої дочірньої вершини
    left_index = 2 * index + 1

    # Індекс правої дочірньої вершини
    right_index = 2 * index + 2

    node.left = build_tree(heap, left_index)
    node.right = build_tree(heap, right_index)

    return node


def add_edges(graph, node, index=0):
    if node is None:
        return

    graph.add_node(index, value=node.value)

    if node.left is not None:
        left_index = 2 * index + 1
        graph.add_edge(index, left_index)
        add_edges(graph, node.left, left_index)

    if node.right is not None:
        right_index = 2 * index + 2
        graph.add_edge(index, right_index)
        add_edges(graph, node.right, right_index)


def calculate_positions(heap):
    positions = {}

    for index in range(len(heap)):
        # Визначаємо рівень вершини
        level = int(math.log2(index + 1))

        # Перша позиція на поточному рівні
        first_index = 2 ** level - 1

        # Позиція вершини на рівні
        position = index - first_index

        # Обчислюємо координати вершини
        x = (position + 0.5) / (2 ** level)
        y = -level

        positions[index] = (x, y)

    return positions


def main():
    # Початкові числа для створення купи
    numbers = [10, 4, 15, 20, 0, 8, 12, 3, 7]

    # Створюємо мінімальну бінарну купу
    heap = numbers.copy()
    heapq.heapify(heap)

    print("Бінарна мінімальна купа:")
    print(heap)

    # Створюємо дерево з масиву купи
    root = build_tree(heap)

    # Створюємо граф
    graph = nx.Graph()

    # Додаємо вершини та ребра до графа
    add_edges(graph, root)

    # Створюємо координати вершин
    positions = calculate_positions(heap)

    # Створюємо підписи вершин
    labels = nx.get_node_attributes(graph, "value")

    # Малюємо дерево
    plt.figure(figsize=(10, 7))

    nx.draw(
        graph,
        positions,
        labels=labels,
        with_labels=True,
        node_size=1800,
        node_color="lightblue",
        font_size=12,
        font_weight="bold",
        edge_color="gray",
        width=2
    )

    plt.title("Візуалізація бінарної мінімальної купи")
    plt.axis("off")
    plt.show()


if __name__ == "__main__":
    main()
