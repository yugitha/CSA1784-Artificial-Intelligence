def decision_tree(age, income):

    if age > 30:
        if income > 50000:
            return "Customer will Buy the Product"
        else:
            return "Customer will Not Buy the Product"
    else:
        return "Customer will Not Buy the Product"

# User Input
age = int(input("Enter Age: "))
income = int(input("Enter Income: "))

result = decision_tree(age, income)

print("\nPrediction:")
print(result)
