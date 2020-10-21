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
	
	typedef struct Vector Vector;
	struct Vector
	{
		float x;
		float y;
	};
	
	
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

	// Calculate deltas.
	float deltaX = pointTwoX - pointOneX;
	float deltaY = pointTwoY - pointOneY;

	// Calculate and print out velocity vector.
	Vector velocity;
	velocity.x = deltaX / TIME_TO_MOVE;
	velocity.y = deltaY / TIME_TO_MOVE;
	printf("Velocity vector: (%.2f, %.2f)", velocity.x, velocity.y);
	printf(NEWLINE);

	// Calculate the distance, speed, and direction between the two points.
	float distance = sqrtf(powf(deltaX, 2) + powf(deltaY, 2));
	float speed = distance / TIME_TO_MOVE;
	float direction = atan2f(deltaY, deltaX);
	direction *= 180 / M_PI;

	// Calculate a unit direction vector.
	Vector unitDirection;
	unitDirection.x = deltaX;
	unitDirection.y = deltaY;
	float length = sqrtf(powf(unitDirection.x, 2) 
		+ powf(unitDirection.y, 2));
	unitDirection.x /= length;
	unitDirection.y /= length;

	// Print and calculate unit direction vector
	// This is the second method
	velocity.x = unitDirection.x * speed;
	velocity.y = unitDirection.y * speed;
	printf("Unit direction vector: (%.2f, %.2f)", velocity.x, velocity.y);
	printf(NEWLINE);


	// Print out Speed and Direction
	printf(NEWLINE);
	printf("Speed: %.2f", speed);
	printf(NEWLINE);
	printf("Direction: %.2f degrees", direction);


	return (EXIT_SUCCESS);
}