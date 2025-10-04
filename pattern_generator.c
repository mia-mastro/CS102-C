#include <stdio.h>

void rightTriangle(int size){
	printf("Right Triangle:");
	int temp = 0;
	for(int i = size + 1; i > 0; i--){
		for(int j = 0; j < temp; j ++){
			printf("*");
		}
		printf("\n");
		temp ++;
	}
}

void upsideDownTriangle(int size){
	printf("Upside Down Triangle:\n");
	int temp = size;
	for(int i = size; i > 0; i--){
		for(int j = temp; j > 0; j --){
			printf("*");
		}
		printf("\n");
		temp --;
	}	
}

void diamond(int size){
	printf("Diamond:\n");
	for(int i = 1; i <= size; i ++){
		for(int j = 1; j <= size - i; j ++){
			printf(" ");
		}
		for(int k = 1; k < 2 * i - 1; k ++){
			printf("*");
		}
		printf("\n");
	}
	for(int i = size - 1; i >= 1; i --){
		for(int j = 1; j <= size - i; j ++){
			printf(" ");
		}	
		for(int k = 1; k < 2 * i - 1; k ++){
			printf("*");
		}
		printf("\n");
	}
	

}

void pascal(int size){
	printf("Pascal's Triangle:\n");
	for(int i = 0; i < size; i ++){
		for(int j = 0; j < size - i - 1; j ++){
			printf(" ");
		}
		
		int temp = 1;
		for(int k = 0; k <= i; k ++){
			printf("%4d", temp);
			temp = temp * (i - k) / (k + 1);
		}
		printf("\n");
	}
}

void multiplicationTable(int size){
	printf("Multiplication Table:\n");
	for(int i = 1; i <= size; i ++){
		for(int j = 1; j <= size; j ++){
			printf("%d\t", i * j);
		}
		printf("\n");
	}
	
}

void checkerboard(int size){
	printf("Checkerboard:\n");
	for(int i = 0; i < size; i++){
		for(int j = 0; j < size; j++){
			if((i + j) % 2 == 0){
				printf("*");
			}else{
				printf(" ");
			}
		}
		printf("\n");
	}
}

int main(){
	int patternNum, patternSize;
	char next;

	//menu print statement and user selections
	printf("~~~Pattern Generator~~~\n1. Right Triangle\n2. Upside Down Triangle\n3. Diamond\n4. Pascal's Triangle\n5. Multiplication Table\n6. Checkerboard\nChoose a pattern (1-6):\n");
	scanf("%d",&patternNum);
	printf("Enter size:\n");
	scanf("%d", &patternSize);

	//determine which pattern to print and print it
	switch(patternNum){
		case 1:{
			rightTriangle(patternSize); 
			break;
		}case 2:{
			upsideDownTriangle(patternSize);
			break;
		}case 3:{
			diamond(patternSize);
			break;
		}case 4:{
			pascal(patternSize);
			break;
		}case 5:{
			multiplicationTable(patternSize);
			break;
		}case 6:{
			checkerboard(patternSize);
			break;
		}default:{
			printf("Invalid pattern requested\n");	
			break;
		}
	}
	printf("Print another pattern? (y/n):\n");
	scanf(" %c", &next);	
	
	if(next == 'y'){
		main();
	}	
	
	printf("Program end. Thanks for using the pattern generator!\n");

	return 0;
}
