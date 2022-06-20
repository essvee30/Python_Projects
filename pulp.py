from pulp import *
import pandas as pd
import numpy as np

n_warehouses = 2
n_customers = 4

# Cost Matrix(Cost of shipping of each object to each customer from warehouses 1 & 2
cost_matrix = np.array([[1, 3, 0.5, 4], [2.5, 5, 1.5, 2.5]])

# Demand Matrix
cust_demand = np.array([35000, 22000, 18000, 30000])

# Supply Matrix
warehouse_supply = np.array([60000, 80000])

# Model Initialization
model = LpProblem(["Supply-Demand-Problem", LpMinimize])

# Defining the decision variables
variable_names = [str(i) + str(j) for j in range(1, n_customers + 1) for i in range(1, n_warehouses + 1)]
variable_names.sort()

print("Variable Indices are = ", variable_names)

# Declaring Decision Variables
DV_variables = LpVariable.matrix("X", variable_names, cat="Integer", lowBound=0)

allocation = np.array(DV_variables).reshape(2, 4)

print("Decision Variable/Allocation Matrix: ")

print(allocation)

# Objective Function

obj_func = lpSum(allocation * cost_matrix)

print(obj_func)

model += obj_func

#print(model)

# Supply Constraints
print("Supply Constraints")

for i in range(n_warehouses):
    print(lpSum(allocation[i][j] for j in range(n_customers)) <= warehouse_supply[i])
    model += lpSum(allocation[i][j] for j in range(n_customers)) <= warehouse_supply[i], "Supply Constraints " + str(i)

print("\n")
print("Customer Constraints")
# Demand Constraints
for j in range(n_customers):
    print(lpSum(allocation[i][j] for i in range(n_warehouses)) >= cust_demand[j])
    model += lpSum(allocation[i][j] for i in range(n_warehouses)) >= cust_demand[j] , "Demand Constraints " + str(j)


