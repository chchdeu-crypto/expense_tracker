from datetime import *
from rich.console import Console
from rich.table import Table
import questionary
console=Console()
expenses = []

def show_expenses(expenses, total):
    if len(expenses) == 0:
        console.print("No expense has been added yet.",style="red")
    else:
        table = Table()
        table.add_column("date")
        table.add_column("title")
        table.add_column("category")
        table.add_column("cost")
        for expens in expenses:
            table.add_row(str(expens["date"]),expens["title"],expens["category"],f'{expens["cost"]:.2f}')
        console.print(table)
    console.print(f"Total: {total:.2f} ILS",style="bold green")
def calculate_total(expenses):
    total=0
    if len(expenses)==0:
         return total
    else:
        for expens in expenses:
                total+=expens["cost"]
        return total
def add_expense(expenses,title,category,cost):
     today=date.today()
     expens={"date":today,"title":title,"category":category,"cost":cost}
     expenses.append(expens)
def ask_for_expense(expenses):
    title=questionary.text("enter title: ").ask()
    cost=float(questionary.text("enter cost: ").ask())
    category=questionary.select(
    "Which category does it belong to??",
    choices=[
        "food",
        "travel",
        "school",
        "entertainment",
        "other"]).ask()
    add_expense(expenses,title,category,cost)
def main():
     show_expenses(expenses,calculate_total(expenses))
     add_expense=False
     while not add_expense:
        user_choice=questionary.select("do you want add an expens",choices=["yes","no"]).ask()
        if user_choice=="yes":
            ask_for_expense(expenses)
            show_expenses(expenses,calculate_total(expenses))
        else:
            add_expense=True
main()              
     
     


    
       
