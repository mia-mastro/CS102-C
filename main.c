#include <stdio.h>
#include "puzzles.h"

int main(){
	int puzzleNum = 0;
	int numOne;
	int numTwo;

	while(puzzleNum != 5){
		printf("~~~ Recursive Puzzle Solver ~~~\n");
		printf("1. Calculate GCD\n");
		printf("2. Factorial\n");
		printf("3. Fibonacci\n");
		printf("4. Digit Sum\n");
		printf("5. Quit\n\n");
		printf("Choose puzzle (1 - 5): \n");
		scanf("%d", &puzzleNum);
	
		if(puzzleNum == 1){
			printf("Enter first number:\n");
			scanf("%d", &numOne);
			printf("Enter second number:\n");
			scanf("%d", &numTwo);
		}else if(puzzleNum < 5){
			printf("Enter number:\n");
			scanf("%d", &numOne);
		}else if(puzzleNum == 5){
			printf("Thank you for using the Puzzle Solver!\n");
		}else{
			printf("Invalid puzzle selected\n");
			main();
		}
	
		switch(puzzleNum){
			case 1:
				printf("GCD of %d and %d = %d\n", numOne, numTwo, gcd(numOne, numTwo));
				break;
			case 2:
				printf("Factorial of %d = %d\n", numOne, factorial(numOne));
				break;
			case 3:
				printf("The %dth term of Fibonacci = %d\n", numOne, fibonacci(numOne));
				break;
			case 4:
				printf("The sum of the digits of %d = %d\n", numOne, sum_digits(numOne));
				break;
		}
	}
	return 0;
}
