Acc_Bal=2000
withdraw_bal=3000
if withdraw_bal > 0:
    if withdraw_bal % 100 == 0:
        if withdraw_bal < Acc_Bal:
            if Acc_Bal >= 500:
                print(f"Withdrawal successful\n{Acc_Bal-withdraw_bal}")
        else:
         print("Withdrawal Unseccessful")
