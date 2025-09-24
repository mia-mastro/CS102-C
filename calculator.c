#include <stdio.h>

double add(double a, double b){
	return a + b;
}

double subtract(double a, double b){
	return a - b;
} 

double multiply(double a, double b){
	return a * b;
}

double divide(double a, double b){
	return a / b;
}

double power(double a, double b){
	double c = a;
	while(b > 1){
		a *= c;
		b -= 1;
	}
	return a;
}

int main(){

	//initialize doubles to store user input values 
	double numOne;
	double numTwo;

	//initialize char to store user input for operation
	char operation;

	//greeting and introduction to the program
	printf("Welcome to the Calculator!\nAdd, subtract, multiply, divide, or exponentiate numbers of your choosing.\nEnter first number:\n");
	
	//take in user input for numbers
	scanf("%lf", &numOne);
	printf("Enter second number:\n");
	scanf("%lf", &numTwo);

	//figure out which operation is requested
	printf("Enter desired calculation (+, -, *, /, ^):\n");
	scanf(" %c", &operation);

	//return appropriate calculated value
	if(operation == '+'){
		printf("Result: %f + %f = %f\n", numOne, numTwo, add(numOne, numTwo));
	}else if(operation == '-'){
		printf("Result: %f - %f = %f\n", numOne, numTwo, subtract(numOne, numTwo));
	}else if(operation == '*'){
		printf("Result: %f * %f = %f\n", numOne, numTwo, multiply(numOne, numTwo));
	}else if(operation == '/'){
		printf("Result: %f / %f = %f\n", numOne, numTwo, divide(numOne, numTwo));
	}else if(operation == '^'){
		printf("Result: %f ^ %f = %f\n", numOne, numTwo, power(numOne, numTwo));
	}else{
		printf("Invalid operation entered\n");	//if the user doesn't enter +, -, *, or /, the program recognizes it as invalid
		return 0;
	}
}
