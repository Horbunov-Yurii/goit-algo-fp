import math
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon


def draw_pythagoras_tree(ax, x, y, size, angle, depth):
    if depth == 0:
        return

    # Обчислюємо координати основи квадрата
    point_a = (x, y)

    point_b = (
        x + size * math.cos(angle),
        y + size * math.sin(angle)
    )

    # Обчислюємо перпендикулярний вектор
    perpendicular_x = -math.sin(angle)
    perpendicular_y = math.cos(angle)

    # Обчислюємо верхні вершини квадрата
    point_d = (
        x + size * perpendicular_x,
        y + size * perpendicular_y
    )

    point_c = (
        point_b[0] + size * perpendicular_x,
        point_b[1] + size * perpendicular_y
    )

    # Малюємо квадрат
    square = Polygon(
        [point_a, point_b, point_c, point_d],
        closed=True,
        facecolor=plt.cm.Greens(0.3 + depth * 0.04),
        edgecolor="black",
        linewidth=0.8
    )

    ax.add_patch(square)

    # Обчислюємо вершину трикутника
    alpha = math.radians(45)

    point_e = (
        point_d[0]
        + size * math.cos(alpha) ** 2 * math.cos(angle)
        - size * math.sin(alpha) * math.cos(alpha) * math.sin(angle),

        point_d[1]
        + size * math.cos(alpha) ** 2 * math.sin(angle)
        + size * math.sin(alpha) * math.cos(alpha) * math.cos(angle)
    )

    # Обчислюємо розміри дочірніх квадратів
    left_size = math.dist(point_d, point_e)
    right_size = math.dist(point_e, point_c)

    # Обчислюємо кути дочірніх квадратів
    left_angle = math.atan2(
        point_e[1] - point_d[1],
        point_e[0] - point_d[0]
    )

    right_angle = math.atan2(
        point_c[1] - point_e[1],
        point_c[0] - point_e[0]
    )

    # Малюємо ліву гілку
    draw_pythagoras_tree(
        ax,
        point_d[0],
        point_d[1],
        left_size,
        left_angle,
        depth - 1
    )

    # Малюємо праву гілку
    draw_pythagoras_tree(
        ax,
        point_e[0],
        point_e[1],
        right_size,
        right_angle,
        depth - 1
    )


def main():
    print("Фрактал «Дерево Піфагора»")

    try:
        depth = int(input("Введіть глибину рекурсії (1-12): "))

        if depth < 1 or depth > 12:
            print("Помилка! Введіть число від 1 до 12.")
            return

    except ValueError:
        print("Помилка! Потрібно ввести ціле число.")
        return

    fig, ax = plt.subplots(figsize=(10, 10))

    draw_pythagoras_tree(
        ax,
        x=0,
        y=0,
        size=1,
        angle=0,
        depth=depth
    )

    ax.set_title(
        f"Дерево Піфагора. Глибина рекурсії: {depth}",
        fontsize=14
    )

    ax.set_aspect("equal")
    ax.autoscale_view()
    ax.margins(0.1)
    ax.axis("off")

    plt.show()


if __name__ == "__main__":
    main()
