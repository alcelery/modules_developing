def calculate_total(expenses):
    total = 0
    for expense in expenses:
        total += expense["amount"]
    return total


def calculate_average(expenses):
    if not expenses:
        raise ValueError("список расходов пуст")
    return calculate_total(expenses) / len(expenses)

def most_expensive_day(expenses):
    if not expenses:
        raise ValueError("список расходов пуст")
    daily_totals = {}
    for item in expenses:
        day = item["day"]
        amount = item["amount"]
        daily_totals[day] = daily_totals.get(day, 0) + amount  
    expensive_day = max(daily_totals, key=daily_totals.get)
    return [expensive_day, daily_totals[expensive_day]]

def category_share(expenses, category):
    if not expenses:
        raise ValueError("список расходов пуст")
    if not category:
        raise ValueError("категория пуста")    
    total = 0  
    category_total = 0 
    for item in expenses:
        total += item["amount"]
        if item["category"] == category:
            category_total += item["amount"]
    if total == 0:
        return 0
    share = (category_total / total) * 100
    return share