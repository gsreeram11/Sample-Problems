# House Hunting

annual_salary = int(input ("Enter yout annual salary:"))
portion_saved = float(input ("Enter the percent of your salary to save:"))
total_cost = int(input ("Enter cost of your dream home:"))
portion_down_payment = 0.25*(total_cost) 
monthly_saved = (annual_salary/12.0)*portion_saved
current_savings = 0 
r = 0.04
months = 0
while current_savings < portion_down_payment:
    months += 1
    monthly_saving = current_savings*(r/12)
    current_savings += monthly_saving + monthly_saved
    print("Number of months:",months)
