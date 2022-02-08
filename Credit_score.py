# Credit scores
# Bad = 300-629
# fair = 630-689
# good = 690-719
# excellent = 720-850
credit_score = int(input('Enter your credit score!'))
if credit_score >= 720:
    print('you have excellent credit! :)')
elif credit_score >= 690:
    print('you have good credit.')
elif credit_score >= 630:
    print('you have fair credit.')
else:
    print('you have bad credit! :(')
