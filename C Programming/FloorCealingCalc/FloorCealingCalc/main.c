/*
 * File:   main.c
 * Author: Yoham Gabriel B
 */

#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <stdlib.h>

#include <math.h>

 /*
  * Calculates the Floor and Ceiling.
  * 
  * Only works for positive numbers.
  * Only works to two decimal places.
  *
  */
int main(int argc, char** argv)
{
	float x;

	// Prompt for and get user input
	printf("Enter floating point number: ");
	scanf_s("%f", &x);
	printf("\n");

	// Calculate and print Floor
	printf("Floor: %d\n", (int)x);

	// Calculate and print Ceiling
	printf("Ceiling: %d\n", (int)(x + 0.99));

	// Calculate and print Floor and Ceiling using math.h
	printf("\n");
	printf("Floor using math.h: %d\n", (int)floorf(x));

	printf("Ceiling using math.h: %d\n", (int)ceilf(x));

	printf("\n");
	return (EXIT_SUCCESS);
}