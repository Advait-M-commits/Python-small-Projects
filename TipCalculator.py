print("Hellew~~, welcome to Python-based tip calculator!!!")
bill = float(input("What is your bill??:\n"))
tip = int(input("How much tip would you like to give?: "))
split = int(input("How many people to split the bill?: "))
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount 
bill_per_person = total_bill / split
final_amount = round(bill_per_person, 2)
print(f"Each person should pay: ${final_amount}")