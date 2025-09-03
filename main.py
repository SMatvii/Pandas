import pandas as pd
data = {
	'Name': ['Alex', 'Bella', 'Chris'],
	'Age': [30, 25, 35],
	'City': ['Kyiv', 'Lviv', 'Odesa']
}
df = pd.DataFrame(data)
print(df)

df['Salary'] = [50000, 60000, 55000]
print(df)

df = df.drop('Age', axis=1)
print(df)

new_row = pd.DataFrame([{'Name': 'Diana', 'City': 'Dnipro', 'Salary': 58000}])
df = pd.concat([df, new_row], ignore_index=True)
print(df)

df = df.drop(0, axis=0).reset_index(drop=True)
print(df)

df['Department'] = 'Sales'
print(df)

df = df.drop('Salary', axis=1)
print(df)

data = {
	'Product': ['Book', 'Pen', 'Notebook'],
	'Price': [15, 2, 5],
	'Stock': [100, 500, 200]
}
df = pd.DataFrame(data)
print(df)


df['Discount'] = '10%'
print(df)

df = df.drop('Stock', axis=1)
print(df)

new_row = pd.DataFrame([{'Product': 'Pencil', 'Price': 1, 'Discount': '5%'}])
df = pd.concat([df, new_row], ignore_index=True)
print(df)

df = df.drop(1, axis=0).reset_index(drop=True)
print(df)

df['Supplier'] = 'Co.'
print(df)

df = df.drop(2, axis=0).reset_index(drop=True)
print(df)

data = {
	'Employee': ['John', 'Emma', 'Oliver'],
	'Department': ['HR', 'Finance', 'IT'],
	'Salary': [50000, 70000, 60000],
	'Age': [28, 34, 29]
}
df = pd.DataFrame(data)
print(df)

df['Bonus'] = df['Salary'] * 0.1
print(df)

df = df.drop('Age', axis=1)
print(df)

new_row = pd.DataFrame([{'Employee': 'Sophia', 'Department': 'Marketing', 'Salary': 65000, 'Bonus': 6500}])
df = pd.concat([df, new_row], ignore_index=True)
print(df)

df = df.drop(0, axis=0).reset_index(drop=True)
print(df)

df = df.drop('Bonus', axis=1)
print(df)

