
var_1 = "This is a test"
var_2 = var_1.startswith("Th")
print(var_2)

var_1 = "This is a test"
var_2 = var_1.startswith("is",2)
print(var_2)

var_1 = "This is a test"
var_2 = var_1.startswith("is",5)
print(var_2)

var_1 = "This is a test"
var_2 = var_1.startswith("tes",-4,-1)
print(var_2)

print("")
print("")
print("")


var_1 = "This is a test"
var_2 = var_1.endswith("st")
print(var_2)

var_1 = "This is a test"
var_2 = var_1.endswith("a test",-6)
print(var_2)

var_1 = "This is a test"
var_2 = var_1.startswith("test",-4)
print(var_2)

var_1 = "This is a test"
var_2 = var_1.startswith("is",-9,-7)
print(var_2)