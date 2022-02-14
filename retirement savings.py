
income = int(input("what is your yearly income"))
age = int(input("what is your age"))
retirement = int(input("what age do you want to retire"))
saving = int(input("what percent of income are you saving"))
bank = int(input("how much money do you have saved"))
years = retirement - age + 1
contribution = income * (saving / 100)
bank += contribution
bank *= 1.06
print("year\t\t\tincome\t\tcontribution\t\t\t\ttotal")
print(format(1, '4,.0f'), format(income, '10,.0f'), format(contribution, '12,.0f'), format(bank, '13,.0f'), sep='\t\t')
for year in range(2, years):
    income *= 1.03
    contribution = income * (saving / 100)
    bank += contribution
    bank *= 1.06
    print(format(year, '4,.0f'), format(income, '10,.0f'), format(contribution, '12,.0f'), format(bank, '13,.0f'), sep='\t\t')
