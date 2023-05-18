from prettytable import PrettyTable

table = PrettyTable()

list_1=['Picachu','Carmander','Squirtle']
list_2=['Electic','Fire','Water']

table.add_column('Pokemon_name',list_1)
table.add_column('Pokemon_type',list_2)

table.align='l'

print(table.align)

print(table)