from app.services.calculator import calculate_total, calculate_average, most_expensive_day, category_share

def format_report(expenses):
    total = calculate_total(expenses)
    average = calculate_average(expenses)
    most_exp_day = most_expensive_day(expenses)
    food_cat = category_share(expenses, "еда")
    place_cat = category_share(expenses, "жильё")
    lines = [
        "ОТЧЁТ ПО ПОЕЗДКЕ",
        "-" * 32,
        f"записей: {len(expenses)}",
        f"всего потрачено: {total} ₽",
        f"средняя трата: {average:.2f} ₽",
        f"самый дорогой день: день {most_exp_day[0]}, {most_exp_day[1]} ₽",
        f"Доля категории «еда»: {food_cat:.2f} %",
        f"Доля категории «жильё»: {place_cat:.2f} %",
    ]
    return "\n".join(lines)