from persistence import *

def main():
    #TODO: implement
    activities=repo.execute_command("SELECT product_id, quantity, activator_id, date FROM activities ORDER by date")
    print("Activities")
    for activity in activities : 
      activity = tuple(x.decode() if isinstance(x, bytes) else x for x in activity)
      print(activity)
      
   
    branches=repo.execute_command("SELECT id, location, number_of_employees FROM branches ORDER by id")
    print("Branches")
    for branche in branches:
      branche = tuple(x.decode() if isinstance(x, bytes) else x for x in branche)
      print(branche)
     
    employees=repo.execute_command("SELECT * FROM employees ORDER BY id")
    print("Employees")
    for employee in employees:
        employee = tuple(x.decode() if isinstance(x, bytes) else x for x in employee)
        print(employee)
    
    products = repo.execute_command("SELECT * FROM products ORDER BY id")
    print("Products")
    for product in products:
        product = tuple(x.decode() if isinstance(x, bytes) else x for x in product)
        print(product)
        
        


    suppliers = repo.execute_command("SELECT * FROM suppliers ORDER BY id")
    print("Suppliers")
    for supplier in suppliers:
        supplier = tuple(x.decode() if isinstance(x, bytes) else x for x in supplier)
        print(supplier)

    
    employeeRep=repo.execute_command("""SELECT employees.name, employees.salary, branches.location, ABS(IFNULL(SUM(activities.quantity * products.price), 0)) AS total_sales_income
    FROM employees
    LEFT JOIN branches ON employees.branche = branches.id
    LEFT JOIN activities ON employees.id = activities.activator_id
    LEFT JOIN products ON activities.product_id = products.id
    GROUP BY employees.name, employees.salary, branches.location;""")

    print("\nEmployees report")
    for record in employeeRep:
        record = tuple(x.decode() if isinstance(x, bytes) else x for x in record)
        tempa=""
        for x in record:
            tempa=tempa+(x.__str__()+" ")
        print(tempa)



    activityRep=repo.execute_command("""SELECT activities.date, products.description, activities.quantity, 
    CASE WHEN activities.quantity < 0 THEN employees.name  END AS 'name of seller',
    CASE WHEN activities.quantity > 0 THEN suppliers.name END AS 'name of the supplier'
    FROM activities
    JOIN products ON activities.product_id = products.id
    LEFT JOIN employees ON activities.activator_id = employees.id AND activities.quantity < 0
    LEFT JOIN suppliers ON activities.activator_id = suppliers.id AND activities.quantity > 0
    ORDER BY activities.date;""")

    print("\nActivities report")
    for record in activityRep:
        record = tuple(x.decode() if isinstance(x, bytes) else x for x in record)
        print(record)    
 
    pass

if __name__ == '__main__':
    main()