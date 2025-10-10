#include <stdio.h>
#include "puzzles.h"

int gcd(int a, int b) {
	if(b == 0){
		return a;
	}
	return gcd(b, a % b);
}

int factorial(int n){
	if(n <= 1){
		return 1;
	}
	return n*factorial(n - 1);
}

int fibonacci(int n){
	if (n <= 1){
		return n;
	}
	return fibonacci(n - 1) + fibonacci(n - 2);
}

int sum_digits(int n){
	if(n == 0){
		return 0;
	}
	return (n % 10) + sum_digits(n / 10);
}	 
