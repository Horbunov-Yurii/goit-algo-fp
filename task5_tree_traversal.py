import matplotlib.pyplot as plt
import networkx as nx
from collections import deque
from matplotlib.colors import to_hex


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def build_tree():
    # Створюємо бінарне дерево
    root = Node(0)

    root.left = Node(4)
    root.right = Node(1)

    root.left.left = Node(5)
    root.left.right = Node(10)

    root.right.left = Node(3)
    root.right.right = Node(2)

    return root


def get_tree_data(root):
    graph = nx.Graph()
    positions = {}
    labels = {}

    # Використовуємо чергу для визначення координат вузлів
    queue = deque([(root, 0, 0, 0)])

    while queue:
        node, x, y, level = queue.popleft()

        graph.add_node(node.value)
        positions[node.value] = (x, y)
        labels[node.value] = str(node.value)

        if node.left is not None:
            left_x = x - 1 / (2 ** (level + 1))

            graph.add_edge(node.value, node.left.value)

            queue.append((
                node.left,
                left_x,
                y - 1,
                level + 1
            ))

        if node.right is not None:
            right_x = x + 1 / (2 ** (level + 1))

            graph.add_edge(node.value, node.right.value)

            queue.append((
                node.right,
                right_x,
                y - 1,
                level + 1
            ))

    return graph, positions, labels


def generate_colors(number_of_nodes):
    # Створюємо послідовність кольорів від темного до світлого
    colors = plt.cm.Blues(
        [i / max(number_of_nodes - 1, 1) for i in range(number_of_nodes)]
    )

    return [to_hex(color) for color in colors]


def visualize_traversal(graph, positions, labels, traversal_order, title):
    colors = generate_colors(len(traversal_order))

    # Спочатку всі вузли мають однаковий колір
    node_colors = {
        node: "#d3d3d3"
        for node in graph.nodes
    }

    plt.ion()

    fig, ax = plt.subplots(figsize=(9, 6))

    for step, node in enumerate(traversal_order):
        # Змінюємо колір поточного вузла
        node_colors[node] = colors[step]

        ax.clear()

        nx.draw(
            graph,
            positions,
            labels=labels,
            with_labels=True,
            node_color=[
                node_colors[current_node]
                for current_node in graph.nodes
            ],
            node_size=1800,
            font_size=12,
            font_weight="bold",
            edge_color="gray",
            width=2,
            ax=ax
        )

        ax.set_title(
            f"{title}\nКрок {step + 1}: відвідано вузол {node}",
            fontsize=14
        )

        plt.pause(0.8)

    plt.ioff()
    plt.show()


def dfs(root):
    # DFS використовує стек
    stack = [root]
    visited = []

    while stack:
        node = stack.pop()
        visited.append(node.value)

        # Спочатку додаємо правого нащадка,
        # щоб лівий оброблявся першим
        if node.right is not None:
            stack.append(node.right)

        if node.left is not None:
            stack.append(node.left)

    return visited


def bfs(root):
    # BFS використовує чергу
    queue = deque([root])
    visited = []

    while queue:
        node = queue.popleft()
        visited.append(node.value)

        if node.left is not None:
            queue.append(node.left)

        if node.right is not None:
            queue.append(node.right)

    return visited


def main():
    root = build_tree()

    graph, positions, labels = get_tree_data(root)

    print("Обхід DFS:")
    dfs_order = dfs(root)
    print(dfs_order)

    print("\nОбхід BFS:")
    bfs_order = bfs(root)
    print(bfs_order)

    # Візуалізація DFS
    visualize_traversal(
        graph,
        positions,
        labels,
        dfs_order,
        "DFS — обхід у глибину"
    )

    # Візуалізація BFS
    visualize_traversal(
        graph,
        positions,
        labels,
        bfs_order,
        "BFS — обхід у ширину"
    )


if __name__ == "__main__":
    main()
