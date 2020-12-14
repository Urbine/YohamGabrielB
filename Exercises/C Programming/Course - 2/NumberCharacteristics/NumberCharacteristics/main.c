/*
 * File:   main.c
 * Author: Yoham Gabriel B
 */

#define _CRT_SECURE_NO_WARNINGS
 
#include <stdio.h>
#include <stdlib.h>


#define MAX_LENGTH 100

/*
 * Number Characteristics Programming Assignment
 */
int main(int argc, char** argv)
{
	// IMPORTANT: Only add code in the section
	// indicated below. The code I've provided
	// makes your solution work with the 
	// automated grader on Coursera
	char input[MAX_LENGTH];
	fgets(input, MAX_LENGTH, stdin);
	while (input[0] != 'q')
	{
		int number = atoi(input);

		// Add your code between this comment
		// and the comment below. You can of
		// course add more space between the
		// comments as needed

		int valueNum;
	
		if (number < 0) {
			valueNum = -1;
		}
		else if (number == 0)
		{
			valueNum = 0;
		}
		else
		{
			valueNum = 1;
		}
	
		char evenOdd;
		
		if (number % 2 == 0) {
			printf("e %d\n", valueNum);
		}
		else
		{
			printf("o %d\n", valueNum);
		}
		
	

		// Don't add or modify any code below
		// this comment
		fgets(input, MAX_LENGTH, stdin);
	}

	return 0;
}
