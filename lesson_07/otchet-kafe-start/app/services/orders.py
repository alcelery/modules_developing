"""Модуль для работы с заказами. Загрузка из файла и аналитика."""
from pathlib import Path

from app.domain.order import Order
from app.services.importer import read_rows


def load_orders(path: Path) -> list[Order]:
    """Загружает список заказов из файла CSV.

    Args:
        path: Путь к файлу с данными о заказах.

    Returns:
        Список объектов Order, созданных на основе прочитанных строк.
    """    
    return [
        Order(waiter=row["waiter"], kopeks=int(row["kopeks"]))
        for row in read_rows(path)
    ]


def revenue_by_waiter(orders: list[Order], top: int = 0) -> dict[str, int]:
    """Считает выручку по каждому официанту.

    Args:
        orders: Заказы за смену, список не должен быть пустым.
        top: Сколько официантов оставить в результате. Значение 0
            означает, что возвращаются все.

    Returns:
        Выручка в копейках по именам официантов, в порядке убывания суммы.

    Raises:
        ValueError: Если список заказов пуст.
    """
    if not orders:
        raise ValueError("Список заказов пуст")
    totals: dict[str, int] = {}
    for order in orders:
        totals[order.waiter] = totals.get(order.waiter, 0) + order.kopeks
    ranked = sorted(totals.items(), key=lambda pair: -pair[1])
    if top:
        ranked = ranked[:top]
    return dict(ranked)


def sort_orders_in_place(orders: list[Order]) -> None:
    """Сортирует список заказов на месте по убыванию суммы.

    Args:
        orders: Список заказов, который будет отсортирован. 
            Изменяет исходный список на месте.
    """    
    orders.sort(key=lambda order: -order.kopeks)
