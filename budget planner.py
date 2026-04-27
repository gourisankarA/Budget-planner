import pandas as pd

lst1 = [100, 200, 300, 400, 500]  # income
lst2 = [70, 150, 200, 250, 300]   # expense

df = pd.DataFrame({'income': lst1, 'expense': lst2})
df['saving'] = df['income'] - df['expense']  # auto calculated

print(df)
print("\nTotal Income:", df['income'].sum())
print("Total Expense:", df['expense'].sum())
print("Total Savings:", df['saving'].sum())

if df['expense'].sum() > df['income'].sum():
    print("⚠️ WARNING: You are overspending!")
elif df['expense'].sum() == df['income'].sum():
    print("⚡ Break even point")
else:
    print("✅ Good job! You are saving money")
    # Savings percentage
savings_pct = (df['saving'].sum() / df['income'].sum()) * 100
print(f"Savings Rate: {savings_pct:.1f}%")

if savings_pct >= 20:
    print("🔥 Excellent! You're on track for wealth")
elif savings_pct >= 10:
    print("👍 Decent. Try to save more")
else:
    print("⚠️ Savings too low. Cut expenses")

# Export
df.to_csv('budget.csv', index=False)
print("\nBudget saved to budget.csv!")