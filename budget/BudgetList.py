from .  import Expense
class Budgetlist():
        def __init__(self, budget):
            self.budget = budgetlist
            self.sum_expenses=0
            self.expenses= []
            self.sum_overages=0
            self.overages= []

        def __len__(self):
            return (len(self.expenses) + len(self.overages))

        def append(self, item):
             if (self.sum_expenses+item < self.budget):
                 self.expenses.append(item)
                 self.sum_expenses += item
             else:
                self.coverages.append(item)
                self.sum_overages+=item

def main():
    #using class above
    myBudgetlist = Budgetlist(1200)
    #add expenses, the last expense is 100 and that goes in overages
    expenses = Expense.Expenses()
    expenses.read_expenses('data/spending_data.csv')
    for expense in expenses.list:
        myBudgetlist.append(expense.amount)

print('The count of all expenses: ' + str(len(myBudgetlist)))

if __name__ == "__main__":
    main()
