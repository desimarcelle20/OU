# import urllib library
from urllib.request import urlopen
#import json
import json

#Help Functions

#This function open json file from url and returns a list object
def openData(url_data):
# Opening JSON file
    f = urlopen(url_data)
    data_string = json.loads(f.read())
# Converting the data string into a python list
    data_list = json.loads(data_string)
# Closing file
    f.close()
    return data_list

#This function prints emplyee with related task    
def printFullNameAndTask (lastName, firstName, task):
   fullNameTask = '   ' + lastName + ', ' + firstName + ' - ' + task
   print(fullNameTask)
  
#This function split due to only keep the format yyyy-mm-dd
def parseDate (DueDate):
    result = DueDate.split('T', 1)[0]
    print(result)

# ______________________________________________Question 1-----------------------------------------
# - Retrieve the collection of employees from the API. 
# - Find all the employees who do not have a badge number.
 
#Reading Json employee file from url
employeeList =  openData('https://mhealthtechinterview.azurewebsites.net/api/employees')
print('--------- Employees without Badges ---------')
for employee in employeeList:
    if employee.get('BadgeNumber') is None:
        id = employee.get('Id')
        lastName = employee.get('LastName')
        firstName = employee.get('FirstName')
        comma = ', '
        space = ' - '
        print(str(id) + space + lastName + comma + firstName)

# ______________________________________________Question 2-----------------------------------------
# Retrieve the collection of employees and departments from the API. Map the employees by department
      
#Reading Json department file from url
department_list = openData('https://mhealthtechinterview.azurewebsites.net/api/departments')
print(department_list)
# Defining all department as a list
accounting_dpt =[]
engineering_dpt = []
sales_dpt = []
shipping_dpt = []
admin_dpt = []
legal_dpt = []
hr_dpt = []
quality_dpt = []
marketing_dpt = []
#Mapping employee to department
for employee in employeeList:
    if employee.get('DepartmentId') == 1:
        accounting_dpt += [employee]
    elif employee.get('DepartmentId') == 2:
        engineering_dpt += [employee]
    elif employee.get('DepartmentId') == 3:
        sales_dpt += [employee]
    elif employee.get('DepartmentId') == 4:
        shipping_dpt += [employee]
    elif employee.get('DepartmentId') == 5:
        admin_dpt += [employee]
    elif employee.get('DepartmentId') == 6:
        legal_dpt += [employee]
    elif employee.get('DepartmentId') == 7:
        hr_dpt += [employee]
    elif employee.get('DepartmentId') == 8:
        quality_dpt += [employee]
    elif employee.get('DepartmentId') == 9:
        marketing_dpt += [employee]   
print ('--------- Employees by Department ---------')
for department in department_list:
    if department.get('Name') == 'Accounting':
        print(department.get('Name'))
        for employee in accounting_dpt:
            lastName = employee.get('LastName')
            firstName = employee.get('FirstName')
            comma = ', '
            print('   ' + lastName + comma + firstName)
    
    elif department.get('Name') == 'Engineering':
        print(department.get('Name'))
        for employee in engineering_dpt:
            lastName = employee.get('LastName')
            firstName = employee.get('FirstName')
            comma = ', '
            print('   ' + lastName + comma + firstName)
    
    elif department.get('Name') == 'Sales':
        print(department.get('Name'))
        for employee in sales_dpt:
            lastName = employee.get('LastName')
            firstName = employee.get('FirstName')
            comma = ', '
            print('   ' + lastName + comma + firstName)
    elif department.get('Name') == 'Shipping':
        print(department.get('Name'))
        for employee in shipping_dpt:
            lastName = employee.get('LastName')
            firstName = employee.get('FirstName')
            comma = ', '
            print('   ' + lastName + comma + firstName)
    
    elif department.get('Name') == 'Administration':
        print(department.get('Name'))
        for employee in admin_dpt:
            lastName = employee.get('LastName')
            firstName = employee.get('FirstName')
            comma = ', '
            print('   ' + lastName + comma + firstName)
    
    elif department.get('Name') == 'Legal':
        print(department.get('Name'))
        for employee in legal_dpt:
            lastName = employee.get('LastName')
            firstName = employee.get('FirstName')
            comma = ', '
            print('   ' + lastName + comma + firstName)
    
    elif department.get('Name') == 'Human Resources':
        print(department.get('Name'))
        for employee in hr_dpt:
            lastName = employee.get('LastName')
            firstName = employee.get('FirstName')
            comma = ', '
            print('   ' + lastName + comma + firstName)
    
    elif department.get('Name') == 'Quality Assurance':
        print(department.get('Name'))
        for employee in quality_dpt:
            lastName = employee.get('LastName')
            firstName = employee.get('FirstName')
            comma = ', '
            print('   ' + lastName + comma + firstName)
    
    elif department.get('Name') == 'Marketing':
        print(department.get('Name'))
        for employee in marketing_dpt:
            lastName = employee.get('LastName')
            firstName = employee.get('FirstName')
            comma = ', '
            print('   ' + lastName + comma + firstName)
# ______________________________________________Question 3-----------------------------------------
#Retrieve the collection of employees and todos from the API. Iterate through the todos and generate a new object type
#which contains the due date, description of the todo and the first and last name of the employee who is assigned to the
#todo (Todo.AssigneeId).  
          
 # Opening JSON todo file         
todos_list = openData('https://mhealthtechinterview.azurewebsites.net/api/todos')
#Mapping employee to their tasks
for employee in employeeList:
  for todos in todos_list:
    if(employee.get('Id')== todos.get('AssigneeId')):
      parseDate(todos.get('DueDate'))
      printFullNameAndTask(employee.get('LastName'), employee.get('FirstName'), todos.get('Description'))
      
  
  


      
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
  
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
