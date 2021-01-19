/*
 * File:   main.c
 * Author: Yoham Gabriel B.
 */

#define _CRT_SECURE_NO_WARNINGS
 
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

#define MAX_LENGTH 100

/*
 * Junior Codebreaker Programming Assignment
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
		// Add your code between this comment
		// and the comment below. You can of
		// course add more space between the
		// comments as needed
		
		int results[26];

		char let[26] = {
			'a',
			'b',
			'c',
			'd', 
			'e', 
			'f',
			'g', 
			'h', 
			'i' , 
			'j', 
			'k', 
			'l', 
			'm', 
			'n', 
			'o', 
			'p', 
			'q', 
			'r', 
			's', 
			't', 
			'u', 
			'v', 
			'w', 
			'x', 
			'y', 
			'z' 
		};

		for (int i = 0; i < 26; i++)
		{
			results[i] = 0;
		}

		for (int i = 0; i < strlen(input); i++)
		{
			char lower[1] = { tolower(input[i]) };

			if (isalpha(lower[0])) {
				
				switch (lower[0])
				{
				case 'a':
					results[0]++;
					continue;
				case 'b':
					results[1]++;
					continue;	
				case 'c':
					results[2]++;
					continue;
				case 'd':
					results[3]++;
					continue;
				case 'e':
					results[4]++;
					continue;
				case 'f':
					results[5]++;
					continue;
				case 'g':
					results[6]++;
					continue;
				case 'h':
					results[7]++;
					continue;
				case 'i':
					results[8]++;
					continue;
				case 'j':
					results[9]++;
					continue;
				case 'k':
					results[10]++;
					continue;
				case 'l':
					results[11]++;
					continue;
				case 'm':
					results[12]++;
					continue;
				case 'n':
					results[13]++;
					continue;
				case 'o':
					results[14]++;
					continue;
				case 'p':
					results[15]++;
					continue;
				case 'q':
					results[16]++;
					continue;
				case 'r':
					results[17]++;
					continue;
				case 's':
					results[18]++;
					continue;
				case 't':
					results[19]++;
					continue;
				case 'u':
					results[20]++;
					continue;
				case 'v':
					results[21]++;
					continue;
				case 'w':
					results[22]++;
					continue;
				case 'x':
					results[23]++;
					continue;
				case 'y':
					results[24]++;
					continue;
				case 'z':
					results[25]++;
					continue;
				default:
					break;
				}
			}
			else {
				continue;
			}
		}

		for (int i = 0; i < 26; i++)
		{
			if (results[i] == 0) {
				continue;
			}
			else {
				printf("%c%d ",toupper(let[i]), results[i]);
			}
		}
		
		printf("\n");

		// Don't add or modify any code below
		// this comment
		fgets(input, MAX_LENGTH, stdin);
	}

	return 0;
}
