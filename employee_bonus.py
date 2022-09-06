def main():
    import csv
    infile = open('EmployeePay.csv','r')
    csvfile=csv.reader(infile,delimiter=',')
    
    next(csvfile)
    
    
    for record in csvfile:
        bonus = float(record[3]) * float(record[4])
        total = bonus+float(record[3])
        print(f'Employee ID: {record[0]}')
        print(f'Employee First Name: {record[1]}')
        print(f'Employee Last Name: {record[2]}')
        print(f'Employee Salary: ${record[3]}')
        print(f'Employee Bonus: $' + format(bonus,'.2f'))
        print(f'Employee Total Pay: ${total}')

        input()

main()