income = int(input("Enter your monthly income: "))
expenses = int(input("Enter your monthly income: "))
m_savings = income - expenses
projected_savings = int(m_savings * 12 + (m_savings * 12 * 0.05)) 

print("Your monthly savings are ${}.".format(m_savings))
print("Projected savings after one year, with interest, is: ${}.".format(projected_savings))