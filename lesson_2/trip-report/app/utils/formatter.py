from app.services.calculator import calculate_total, calculate_average

def format_report(expenses):
    total = calculate_total(expenses)
    average = calculate_average(expenses)
    lines = [
        "ОТЧЁТ ПО ПОЕЗДКЕ",
        "-" * 32,
        f"записей: {len(expenses)}",
        f"всего потрачено: {total} ₽",
        f"средняя трата: {average:.2f} ₽",
    ]
    return "\n".join(lines)