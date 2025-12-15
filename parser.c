#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "csv_parser.h"

void removeEndOfLine(char *str){
	char *p = str;
	while (*p != '\0'){
		if(*p == '\n'){
			*p = '\0';
			break;
		}else if(*p == '\r'){
			*p = '\0';
			break;
		}
		p ++;
	}
}

char *breakApart(char *str, char commas){
	static char *nextChar = NULL;
	if(str != NULL)
		nextChar = str;
	if(nextChar == NULL)
		return NULL;

	char *first = nextChar;
	while(*nextChar != '\0' && *nextChar != commas){
		nextChar ++;
	}
	
	if(*nextChar == '\0')
		nextChar = NULL;
	else{
		*nextChar = '\0';
		nextChar ++;
	}

	return first;
}

void parse(char *fileName){
	FILE *file = fopen(fileName, "r");
	printf("~~~CSV Parser~~~\n");
	printf("CSV Preview:\n");
	char line[256];
	
	while(fgets(line,sizeof(line), file)){
		removeEndOfLine(line);
		printf("%s\n", line);
	}

	rewind(file);
	printf("\n-----------------------\n");
	printf("Student Records:\n\n");

	while(fgets(line, sizeof(line), file)){
		removeEndOfLine(line);
		
		if(line[0] == '\0')
			continue;

		char *p = line;
		
		char *name = breakApart(p, ',');
		printf("Name: %s\n", name);
		
		printf("Grades: ");
		char *piece;
		double sum = 0;
		int count = 0;
		int one = 1;
		
		while((piece = breakApart(NULL, ',')) != NULL){
			double grade = atof(piece);
			sum += grade;
			count ++;
			if(!one)
				printf(", ");
			printf("%.0f", grade);
			one = 0;
		}
		double avg = (count > 0) ? (sum / count) : 0.0;
		printf("\nAverage: %.2f\n\n", avg);
	}
	fclose(file);
}

//collect command line argument
int getFile(int argc, char *argv[]){
	for(int i = 1; i < argc; i++)
		printf("%s%s", argv[i], (i < argc - 1) ? " " : "");
	printf("\n");
	return 0;
}
