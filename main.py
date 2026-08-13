from datetime import *
from rich.console import Console
from rich.table import Table
console=Console()
expenses = []

def show_expenses(expenses, total):
    if len(expenses) == 0:
        console.print("No expense has been added yet.")
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
    title=input("enter title: ")
    cost=float((input("enter cost: ")))
    category=input("enter category:")
    add_expense(expenses,title,category,cost)
def main():
     show_expenses(expenses,calculate_total(expenses))
     add_expense=False
     while not add_expense:
        user_choice=int(input("enter 1 if you want enter an expens enter 2 if you dont want: "))
        if user_choice==1:
            ask_for_expense(expenses)
            show_expenses(expenses,calculate_total(expenses))
        else:
            add_expense=True
main()              
     
     


    
       
