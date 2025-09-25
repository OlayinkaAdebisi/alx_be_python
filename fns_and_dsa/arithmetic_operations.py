#stores the operation signs in a Tuple
operation = ("add","subtract","multiply","divide")
def perform_operation(num1,num2,operation: str(operation)):
#use the match statement to correctly assign the operator
    match operation:
        case "add":
            return num1+num2
        case "subtract":
            return num1-num2
        case "multiply":
            return num1*num2
        case "divide":
            if num2==0:
                print("Error division by zero")
            else:
                return num1/num2
        case None:
            print("Input correct operator: 'add','subtract','multiply','divide'")