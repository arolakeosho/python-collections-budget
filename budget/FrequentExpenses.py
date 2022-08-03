import collections #counter collections to count categories
from . import Expense
import matplotlib.pyplot as plt
#create a list of spending categories

expenses= Expense.Expenses()
expenses.read_expenses('data/spending_data.csv')
spending_categories= []
for expense in expenses.list:
    spending_categories.append(expense.category)

#Count Categories with a Counter Collection
spending_counter= collections.Counter(spending_categories)
top5= spending_counter.most_common(5)
categories, count= zip(*top5)
fig, ax = plt.subplots()
ax.bar(categories, count)
ax.set_title('# of Purchase by Category')
plt.show()
