import pulp

# Data: Supplier information , cost per unit (c_jk), and maximum supply
#capacity (s_jk)
suppliers = ['Supplier1', 'Supplier2', 'Supplier3']
resources = ['Toilet␣Paper', 'Liquid␣Soap', 'Detergent', 'Cloths',
'Toothpaste', 'Toothbrushes', 'Sanitary␣Pads', 'Shampoo']
# Cost and maximum supply capacity for each supplier and resource
cost_per_unit = {
('Supplier1', 'Toilet␣Paper'): (0.80, 150),
('Supplier1', 'Liquid␣Soap'): (6.40, 25),
('Supplier1', 'Detergent'): (6.80, 20),
('Supplier1', 'Cloths'): (10.00, 10),
('Supplier1', 'Toothpaste'): (2.60, 50),
('Supplier1', 'Toothbrushes'): (0.80, 50),
('Supplier1', 'Sanitary␣Pads'): (0.20, 150),
('Supplier1', 'Shampoo'): (2.30, 20),
('Supplier2', 'Toilet␣Paper'): (0.95, 100),
('Supplier2', 'Liquid␣Soap'): (3.98, 15),
('Supplier2', 'Detergent'): (4.60, 10),
('Supplier2', 'Cloths'): (11.00, 10),
('Supplier2', 'Toothpaste'): (3.00, 60),
('Supplier2', 'Toothbrushes'): (0.85, 60),
('Supplier2', 'Sanitary␣Pads'): (0.18, 100),
('Supplier2', 'Shampoo'): (1.20, 20),
('Supplier3', 'Toilet␣Paper'): (0.84, 70),
('Supplier3', 'Liquid␣Soap'): (5.50, 30),
('Supplier3', 'Detergent'): (7.50, 15),
('Supplier3', 'Cloths'): (10.50, 15),
('Supplier3', 'Toothpaste'): (2.80, 30),
('Supplier3', 'Toothbrushes'): (0.82, 30),
('Supplier3', 'Sanitary␣Pads'): (0.15, 100),
('Supplier3', 'Shampoo'): (3.00, 30)
}
# Minimum required quantities as a dataset for a shelter housing 20 people
#for one month
minimum_quantities = {
'Toilet␣Paper': 200,
'Liquid␣Soap': 40,
'Detergent': 30,
'Cloths': 20,
'Toothpaste': 100,
'Toothbrushes': 100,
'Sanitary␣Pads': 300,
'Shampoo': 40
}

model = pulp.LpProblem("Shelter_Procurement", pulp.LpMinimize)
x = pulp.LpVariable.dicts("x", (suppliers,resources), lowBound=0)
model += pulp.lpSum(cost_per_unit[(j,k)][0]*x[j][k] for j in suppliers for k in resources)

for k in resources:
    model += pulp.lpSum(x[j][k] for j in suppliers) >= minimum_quantities[k]
for j in suppliers:
    for k in resources:
        model += x[j][k] <= cost_per_unit[(j,k)][1]

model += pulp.lpSum(cost_per_unit[(j,k)][0]*x[j][k] for j in suppliers for k in resources) <= 2000

model.solve()
print("Status:", pulp.LpStatus[model.status])
for j in suppliers:
    for k in resources:
        if pulp.value(x[j][k]) > 0:
            print(j, k, pulp.value(x[j][k]))
print("Total Cost =", pulp.value(model.objective))
