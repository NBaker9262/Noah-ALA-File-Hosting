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
# Name:
# Period:
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


# ============================================================
# Q1 — Column Discovery
# ============================================================

# STUDENT ACTION (YOU MUST DO BOTH):
# 1) Set the variables (VAR_1, NAME_1, ROWS_1) and (VAR_2, NAME_2, ROWS_2)
# 2) Write the two preview(...) calls, then set Q1_DONE = "DONE"

Q1_DONE = "DONE"  # change to "DONE" when finished

# ----------------------------
# STUDENT BUILD ZONE (Q1 vars)
# REQUIRED TARGETS:
# VAR_1 = goog
# NAME_1 = "GOOG"
# ROWS_1 = 5
# VAR_2 = nflx
# NAME_2 = "NFLX"
# ROWS_2 = 5
# ----------------------------
VAR_1 = goog
NAME_1 = "GOOG"
ROWS_1 = 5

VAR_2 = nflx
NAME_2 = "NFLX"
ROWS_2 = 5

# ----------------------------
# STUDENT BUILD ZONE (Q1 calls)
# REQUIRED TARGETS:
# preview(VAR_1, NAME_1, ROWS_1)
# preview(VAR_2, NAME_2, ROWS_2)
# ----------------------------
preview(VAR_1, NAME_1, ROWS_1)
preview(VAR_2, NAME_2, ROWS_2)

if require_done(
    Q1_DONE,
    "Q1",
    'Set your variables AND calls, then type:\nQ1_DONE = "DONE"\n\nRequired:\nVAR_1 = goog\nNAME_1 = "GOOG"\nROWS_1 = 5\nVAR_2 = nflx\nNAME_2 = "NFLX"\nROWS_2 = 5\npreview(VAR_1, NAME_1, ROWS_1)\npreview(VAR_2, NAME_2, ROWS_2)'
):
    # If students completed Q1 correctly, these calls should already exist above.
    # (We do not auto-run them here to keep the “type it yourself” expectation.)
    pass

# NOTE:
# If column names differ from Open/Close/Volume in your file,
# the helper functions will tell you what's missing.


# ============================================================
# Q2 — Highest Volume Week (GOOG)
# ============================================================
goog_vol_col = find_col(goog, ["Volume", "volume", "Vol", "vol"], "Volume")

# STUDENT ACTION (YOU MUST DO BOTH):
# 1) Create q2_table using a function call
# 2) Set Q2_DONE = "DONE"

Q2_DONE = "DONE"  # change to "DONE" when finished

# ----------------------------
# STUDENT BUILD ZONE (Q2)
# REQUIRED TARGET:
# q2_table = row_of_max(goog, goog_vol_col)
# ----------------------------
q2_table = row_of_max(goog, goog_vol_col)

if require_done(Q2_DONE, "Q2", 'Type BOTH lines:\nq2_table = row_of_max(goog, goog_vol_col)\nQ2_DONE = "DONE"'):
    print("\n--- Q2: GOOG Highest Volume Week (single row) ---")
    print(q2_table.to_string(index=False))


# ============================================================
# Q3 — Top 5 GOOG Volume Weeks
# ============================================================

Q3_DONE = "DONE"

# ----------------------------
# STUDENT BUILD ZONE (Q3)
# REQUIRED TARGET:
q3_table = top_n_by_volume(goog, 5) 

# ----------------------------


if require_done(Q3_DONE, "Q3", 'Type BOTH lines:\nq3_table = top_n_by_volume(goog, 5)\nQ3_DONE = "DONE"'):
    print("\n--- Q3: GOOG Top 5 Volume Weeks ---")
    print(q3_table.to_string(index=False))


# ============================================================
# Q4 — Biggest Weekly Price Increase (GOOG)
# ============================================================

Q4_DONE = "DONE"

# ----------------------------
# STUDENT BUILD ZONE (Q4)
# REQUIRED TARGETS:
# goog_change = add_change_column(goog)
# q4_table = row_of_max(goog_change, "CloseMinusOpen")
# ----------------------------
goog_change = add_change_column(goog)
q4_table = row_of_max(goog_change, "CloseMinusOpen")

if require_done(
    Q4_DONE,
    "Q4",
    'Type ALL lines:\ngoog_change = add_change_column(goog)\nq4_table = row_of_max(goog_change, "CloseMinusOpen")\nQ4_DONE = "DONE"'
):
    print("\n--- Q4: GOOG Biggest Weekly Increase (CloseMinusOpen max) ---")
    print(q4_table.to_string(index=False))


# ============================================================
# Q5 — Highest Volume Week (NFLX)
# ============================================================
nflx_vol_col = find_col(nflx, ["Volume", "volume", "Vol", "vol"], "Volume")

Q5_DONE = "DONE"

# ----------------------------
# STUDENT BUILD ZONE (Q5)
# REQUIRED TARGET:
# q5_table = row_of_max(nflx, nflx_vol_col)
# ----------------------------
q5_table = row_of_max(nflx, nflx_vol_col)

if require_done(Q5_DONE, "Q5", 'Type BOTH lines:\nq5_table = row_of_max(nflx, nflx_vol_col)\nQ5_DONE = "DONE"'):
    print("\n--- Q5: NFLX Highest Volume Week (single row) ---")
    print(q5_table.to_string(index=False))

# ============================================================
# Q6 — Worst Week for NFLX (most negative CloseMinusOpen)
# ============================================================

Q6_DONE = "DONE"

# ----------------------------
# STUDENT BUILD ZONE (Q6)
# REQUIRED TARGETS:
# nflx_change = 
# q6_table = 
# ----------------------------
nflx_change = add_change_column(nflx)
q6_table = nflx_change.sort_values(by="CloseMinusOpen", ascending=True).head(1)

if require_done(
    Q6_DONE,
    "Q6",
    'Type ALL lines:\nnflx_change = add_change_column(nflx)\nq6_table = nflx_change.sort_values(by="CloseMinusOpen", ascending=True).head(1)\nQ6_DONE = "DONE"'
):
    print("\n--- Q6: NFLX Worst Week (CloseMinusOpen min) ---")
    print(q6_table.to_string(index=False))


# ============================================================
# Q7 — Compare highest-volume weeks: GOOG vs NFLX
# ============================================================

Q7_DONE = "DONE"

# ----------------------------
# STUDENT BUILD ZONE (Q7)
# REQUIRED TARGETS:
# goog_top1 = 
# nflx_top1 = 
# goog_max_vol = 
# nflx_max_vol = 
# ----------------------------
goog_top1 = row_of_max(goog, goog_vol_col)
nflx_top1 = None
goog_max_vol = None
nflx_max_vol = None

if require_done(
    Q7_DONE,
    "Q7",
    'Type ALL lines:\ngoog_top1 = row_of_max(goog, goog_vol_col)\nnflx_top1 = row_of_max(nflx, nflx_vol_col)\ngoog_max_vol = float(goog_top1[goog_vol_col].iloc[0])\nnflx_max_vol = float(nflx_top1[nflx_vol_col].iloc[0])\nQ7_DONE = "DONE"'
):
    bigger = "GOOG" if goog_max_vol > nflx_max_vol else "NFLX"
    diff = abs(goog_max_vol - nflx_max_vol)

    print("\n--- Q7: Highest Volume Comparison ---")
    print("GOOG max volume:", goog_max_vol)
    print("NFLX max volume:", nflx_max_vol)
    print("Higher:", bigger)
    print("Difference:", diff)


# ============================================================
# Q8 — Average Volume Comparison
# ============================================================

Q8_DONE = "CHANGE_ME"

# ----------------------------
# STUDENT BUILD ZONE (Q8)
# REQUIRED TARGETS:

# ----------------------------
goog_avg_vol = None
nflx_avg_vol = None

if require_done(
    Q8_DONE,
    "Q8",
    'Type ALL lines:\ngoog_avg_vol = safe_mean(goog, goog_vol_col)\nnflx_avg_vol = safe_mean(nflx, nflx_vol_col)\nQ8_DONE = "DONE"'
):
    bigger_avg = "GOOG" if goog_avg_vol > nflx_avg_vol else "NFLX"

    print("\n--- Q8: Average Volume Comparison ---")
    print("GOOG average volume:", goog_avg_vol)
    print("NFLX average volume:", nflx_avg_vol)
    print("Higher average:", bigger_avg)


# ============================================================
# Q9 — Volatility Proxy: abs(Close - Open)
# ============================================================

Q9_DONE = "CHANGE_ME"

# ----------------------------
# STUDENT BUILD ZONE (Q9)
# REQUIRED TARGETS:

# ----------------------------
goog_abs = None
nflx_abs = None
goog_avg_abs = None
nflx_avg_abs = None

if require_done(
    Q9_DONE,
    "Q9",
    'Type ALL lines:\ngoog_abs = add_abs_change_column(goog)\nnflx_abs = add_abs_change_column(nflx)\ngoog_avg_abs = safe_mean(goog_abs, "AbsChange")\nnflx_avg_abs = safe_mean(nflx_abs, "AbsChange")\nQ9_DONE = "DONE"'
):
    more_volatile = "GOOG" if goog_avg_abs > nflx_avg_abs else "NFLX"

    print("\n--- Q9: Volatility Comparison (mean AbsChange) ---")
    print("GOOG mean AbsChange:", goog_avg_abs)
    print("NFLX mean AbsChange:", nflx_avg_abs)
    print("More volatile (by this measure):", more_volatile)


# ============================================================
# Q10 — Data-Backed Summary (write as comments)
# ============================================================

# Q10_DONE is optional (teacher choice). If you want a strict check, use it.
Q10_DONE = "CHANGE_ME"  # change to "DONE" after writing your comment summary

# STUDENT ACTION:
# Write 2–4 sentences as Python comments using your results from Q7–Q9.
# - Which stock is more actively traded? (volume evidence)
# - Which stock is more volatile? (AbsChange evidence)
#
# Write your answer below:
#
# # My conclusion:
# # ...
# # ...
# # ...
#
# Then set:
# Q10_DONE = "DONE"

if require_done(Q10_DONE, "Q10", 'Write your 2–4 sentence comment conclusion, then type:\nQ10_DONE = "DONE"'):
    print("\n--- Q10: Comment-based conclusion completed. ---")
