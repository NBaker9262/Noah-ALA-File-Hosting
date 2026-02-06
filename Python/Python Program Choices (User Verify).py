#3rd Period
#Noah Baker

# ============================================================
# CTE APP DESIGN — DATA TABLES LAB (GOOG vs NFLX)
# Unit: Python Foundations (Functions + Using Existing Resources)
#
# IN-CLASS EXPECTATIONS
# - Submit: 1 complete .py file (NO screenshots)
# - You are expected to TYPE the required lines (copy/paste is not the goal)
#
# HOW THIS FILE WORKS
# - "DO NOT EDIT" sections are the engine
# - Each question has:
#   1) STUDENT BUILD ZONE (you type 1+ function calls)
#   2) a DONE flag you must set to "DONE"
# - If you don’t complete a question, the program will NOT crash.
#   It will print what you need to type and move on.
#
# Name: Noah Baker
# Period: 3rd
# ============================================================

import pandas as pd

# ============================================================
# DO NOT EDIT — Dataset links (teacher-provided)
# ============================================================
GOOG_URL = "https://raw.githubusercontent.com/coltonsharp-dev/python-class-data-hub/main/GOOG.csv"
NFLX_URL = "https://raw.githubusercontent.com/coltonsharp-dev/python-class-data-hub/main/NFLX.csv"

goog = pd.read_csv(GOOG_URL)
nflx = pd.read_csv(NFLX_URL)

# ============================================================
# DO NOT EDIT — Helper functions (students CALL these)
# ============================================================

def preview(df, name, n=5):
    if not isinstance(n, int) or n <= 0:
        n = 5
    if not isinstance(name, str) or name.strip() == "":
        name = "DATASET"
    print(f"\n===== {name} PREVIEW =====")
    print("Columns:", list(df.columns))
    print(df.head(n).to_string(index=False))


def find_col(df, candidates, purpose):
    for c in candidates:
        if c in df.columns:
            return c
    raise KeyError(f"Missing column for {purpose}. Tried {candidates}. Found {list(df.columns)}")


def add_change_column(df):
    open_col = find_col(df, ["Open", "open"], "Open")
    close_col = find_col(df, ["Close", "close", "Adj Close", "AdjClose", "adj_close"], "Close")
    out = df.copy()
    out["CloseMinusOpen"] = out[close_col] - out[open_col]
    return out


def add_abs_change_column(df):
    out = add_change_column(df)
    out["AbsChange"] = out["CloseMinusOpen"].abs()
    return out


def top_n_by_volume(df, n=5):
    vol_col = find_col(df, ["Volume", "volume", "Vol", "vol"], "Volume")
    return df.sort_values(by=vol_col, ascending=False).head(n).copy()


def row_of_max(df, col_name):
    return df.loc[df[col_name].idxmax()].to_frame().T


def safe_mean(df, col_name):
    return float(df[col_name].mean())


def require_done(flag, q_label, what_to_type):
    if flag != "DONE":
        print(f"\n[{q_label}] NOT COMPLETED YET")
        print("To complete this question, type:")
        print(what_to_type)
        return False
    return True

def get_number(prompt):
    while True:
        s = input(prompt).strip()
        if s == "":
            print("Please type something.")
            continue
        try:
            n = int(s)
        except ValueError:
            print("Enter a whole number like -5, 0, or 12.")
            continue
        if abs(n) > 10000000:
            print("Number too big. Keep it between -10000000 and 10000000.")
            continue
        return n


def main():
    name = ""
    while not name:
        name = input("What is your name? ").strip()
        if not name:
            print("Name cannot be blank.")

    while True:
        num1 = get_number("Enter a number: ")
        num2 = get_number("Enter another number: ")

        print("\n--- Results ---")
        print("Hello", name)
        print("First number:", num1)
        print("Second number:", num2)
        print("Sum:", num1 + num2)
        print("Difference:", num1 - num2)
        print("Product:", num1 * num2)
        if num2 == 0:
            print("Cannot divide by zero.")
        else:
            print("Quotient:", num1 / num2)
            print("Remainder:", num1 % num2)


if __name__ == "__main__":
    main()