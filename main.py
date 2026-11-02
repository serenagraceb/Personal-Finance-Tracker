import mysql.connector
from sub import calculate_total,calculate_category
import matplotlib.pyplot as plt
from dotenv import load_dotenv
import os
load_dotenv("p.env")
class Transaction:
    def __init__(self,amount,category,income_expense):
        if amount<=0:
            raise ValueError("Amount must be positive")
        self.amount=amount
        self.income_expense=income_expense
        self.category=category
    def to_list(self):
        return [self.amount,self.category,self.income_expense]
class FinanceTracker:
    def __init__(self):
        self.connection=mysql.connector.connect(
            host="localhost",
            user="root",
            password=os.getenv("MYSQL_PASSWORD"),
            database="finance_tracker"
        )
        self.cursor=self.connection.cursor()
    def add_transaction(self,transaction):
        query="""
        INSERT INTO transactions(amount,category,income_expense)
        VALUES(%s,%s,%s)
        """
        values=(
            transaction.amount,
            transaction.category,
            transaction.income_expense
        )
        self.cursor.execute(query,values)
        self.connection.commit()
    def get_transactions(self):
        self.cursor.execute(
            "SELECT amount,category,income_expense FROM transactions"
        )
        return self.cursor.fetchall()
    def show_all(self):
        data = self.get_transactions()
        for i in data:
            print(i)
    def total_income(self):
        data=self.get_transactions()
        return calculate_total(data,"income")
    def total_expense(self):
        data=self.get_transactions()
        return calculate_total(data,"expense")
    def category(self):
        data=self.get_transactions()
        return calculate_category(data)
    def plot_expenses(self):
        summary=self.category()
        categories=list(summary.keys())
        amounts=list(summary.values())
        plt.pie(amounts,labels=categories)
        plt.title("Expenses by Category")
        plt.show()
def main():
    tracker=FinanceTracker()
    while True:
        choice=input("Enter your choice: ")
        try:
            if choice=="add":
                amount=float(input("Enter amount:"))
                category=input("Enter category:")
                income_expense=input("Enter income/expense:")
                if income_expense not in ["income","expense"]:
                    raise ValueError("Invalid type")
                t=Transaction(amount,category,income_expense)
                tracker.add_transaction(t)
            elif choice=="show":
                tracker.show_all()
            elif choice=="income":
                print("Total Income:",tracker.total_income())
            elif choice=="expense":
                print("Total Expense:",tracker.total_expense())
            elif choice=="category":
                print(tracker.category())
            elif choice=="graph":
                tracker.plot_expenses()
            elif choice=="exit":
                break
            else:
                print("Invalid choice")
        except Exception as e:
            print("Error:", e)
if __name__ == "__main__":
    main()