/*
 * File:   main.c
 * Author: Yoham Gabriel B
 */

#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <stdlib.h>

#include <math.h>

#define TIME_TO_MOVE 3
#define M_PI 3.14159265359
#define NEWLINE "\n"

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

	// Calculate the distance, speed, and direction between the two points.
	float deltaX = pointTwoX - pointOneX;
	float deltaY = pointTwoY - pointOneY;
	float distance = sqrtf(powf(deltaX, 2) + powf(deltaY, 2));
	float speed = distance / TIME_TO_MOVE;
	float direction = atan2f(deltaY, deltaX);
	direction *= 180 / M_PI;

	// Print out Speed and Direction
	printf(NEWLINE);
	printf("Speed: %.2f", speed);
	printf(NEWLINE);
	printf("Direction: %.2f degrees", direction);


	return (EXIT_SUCCESS);
}