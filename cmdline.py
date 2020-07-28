import sqlite3 as sql
import datetime
from time import strftime, localtime
import sys

def AddTransaction(date: str, time: str, why: str, typer: bool, amount: float) -> int:
    try:
        conn = sql.connect("record.db")
        conn.execute("INSERT INTO transactions VALUES (?, ?, ?, ?, ?);", [date, time, why, typer, amount])
        conn.commit()
    except SystemError:
        pass

def PrintTransactions():
    database = sql.connect("record.db")
    conn = database.cursor()
    conn.execute("SELECT * FROM transactions")
    transactions = conn.fetchall()

    for i in transactions:
        print(f"[{i[0]} : {i[1]}]: {'+' if i[3] == '0' else '-'}{i[4]/10}   {i[2]}")

def main():
    print("Transaction Tracker v.0.1.1\nType <Ctrl-c> to quit.\n")

    operation = input("1: Input Transaction\n2: Get transaction log\n> ")
    if operation == "1":
        date = input("Please input the date the transaction occured (\"0\" for current date.)\n")
        if date == "0":
            date = str(datetime.date.today())
        time = input("What was the time (HH:MM) when the transaction occured? (\"0\" for right now.)\n")
        if time == "0":
            time = str(strftime("%H:%M", localtime()))
        elif len(time) > 5:
            print("That is not a valid time.")
            sys.exit(1)
        why = input("Describe the transaction in a few words.\n>")
        typer = int(input("Was it a deposit (0) or withdrawal (1)?"))
        amount = input("Please input the amount of money transacted (leave out the \"$\", please.)\n> ")
        if "$" in amount:
            print("I thought I told you to leave out that dollar sign!")
            sys.exit(1)
        else:
            amount = int(float(amount)*100)
        AddTransaction(date, time, why, typer, amount)

    elif operation == "2":
        PrintTransactions()

if __name__ == "__main__":
    main()