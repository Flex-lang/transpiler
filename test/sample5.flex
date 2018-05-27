Main() {
    operator is char
    firstNumber,secondNumber are double
    print "Enter an operator (+, -, *, /): "
    get operator		
    display "Enter two operands: "
    input firstNumber,secondNumber
    switch operator
        case '+' ->
	    display "Addition = "
            output firstNumber+secondNumber
	case '-' ->
	    display "Subtraction = "
            output firstNumber-secondNumber
	case '*' ->
	    display "Multiplication = "
            output firstNumber*secondNumber
	case '/' ->
	    display "Division = "
            output firstNumber/secondNumber
        // operator is doesn't match any case constant (+, -, *, /)
        default:
            print "Error! operator is not correct"

