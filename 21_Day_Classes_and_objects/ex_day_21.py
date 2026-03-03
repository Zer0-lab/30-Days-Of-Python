import statistics
from collections import Counter

class Statistics:
    def __init__(self, numbers):
        self.numbers = numbers

    def mean(self):
        return statistics.mean(self.numbers)

    def count(self):
        return len(self.numbers)
    
    def sum(self):
        return sum(self.numbers)
    
    def min(self):
        return min(self.numbers)
    
    def max(self):
        return max(self.numbers)
    
    def range(self):
        return max(self.numbers) - min(self.numbers)
    
    def median(self):
        return statistics.median(self.numbers)
    
    def mode(self):
        counts = Counter(self.numbers)
        mode_value, mode_count = counts.most_common(1)[0]
        return {"mode": mode_value, "count": mode_count}
    
    def std(self):
        return statistics.stdev(self.numbers)
    
    def variance(self):
        return statistics.variance(self.numbers)
    
    def freq_dist(self):
        counts = Counter(self.numbers)
        total = self.count()
        distribution = [
            (round((count / total) * 100, 1), value)
            for value, count in counts.items()
        ]
        distribution.sort(key=lambda item: (-item[0], -item[1]))
        return distribution
    
    def summary(self):
        return {
            "count": self.count(),
            "sum": self.sum(),
            "min": self.min(),
            "max": self.max(),
            "range": self.range(),
            "mean": self.mean(),
            "median": self.median(),
            "mode": self.mode(),
            "std": self.std(),
            "variance": self.variance(),
            "freq_dist": self.freq_dist()
        }
    
ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]

data = Statistics(ages)

print("Mode: ", data.mode())
print("Frequency Distribution: ", data.freq_dist())
for key, value in data.summary().items():
    print(f"{key}: {value}")


class PersonAccount:
    def __init__(self, firstname, lastname, incomes, expenses):
        self.firstname = firstname
        self.lastname = lastname
        self.incomes = incomes
        self.expenses = expenses

        def total_income(self):
            return sum(self.incomes)
        
        def total_expense(self):
            return sum(self.expenses)
        
        def account_info(self):
            return f"Name: {self.firstname} {self.lastname}\nIncomes: {self.incomes}\nExpenses: {self.expenses}"
        
        def add_income(self, income):
            self.incomes.append(income)
        
        def add_expense(self, expense):
            self.expenses.append(expense)
        
        def account_balance(self):
            return self.total_income() - self.total_expense()
        
        def __str__(self):
            return f"Name: {self.firstname} {self.lastname}\nIncomes: {self.incomes}\nExpenses: {self.expenses}"
        