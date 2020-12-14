/*
 * File:   main.c
 * Author: Yoham Gabriel B
 */

#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <stdlib.h>

#include <math.h>

 /* 
  * 
  * Calculate the distance between two points X and Y
  * 
  */
int main(int argc, char** argv)
{
	float pointOneX;
	float pointOneY;
	float pointTwoX;
	float pointTwoY;

	// Prompt for and get user input.
	printf("Enter X for first point: ");
	scanf("%f", &pointOneX);
	printf("Enter Y for first point: ");
	scanf("%f", &pointOneY);
	printf("Enter X for second point: ");
	scanf("%f", &pointTwoX);
	printf("Enter Y for second point: ");
	scanf("%f", &pointTwoY);

	// Calculate and print the distance between the two points.
	float distance = sqrtf(powf(pointOneX - pointTwoX, 2)
		+ powf(pointOneY + pointTwoY, 2));
	printf("\n");
	printf("Distance between the two points is: %.2f", distance);

	return (EXIT_SUCCESS);
}
