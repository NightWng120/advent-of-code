#include <stdio.h>
#include <string.h>
#include <stdlib.h>
/*
 * Should probably do depth first search and return he number of nodes visited
 *
*/
int ROW = 99;
int COL = 99;
int MAP[99][99];


int heights(){
	int row = 1;
	int col = 1;
	int height = 0;
	int total = 1;
	int up = 0;
	int down = 0;
	int left = 0;
	int right = 0;
	for(int i = 0; i < ROW; i++){
		for(int j = 0; j < COL; j++){

			while(i - row >= 0){
				if(MAP[i][j] > MAP[i - row][j]){
					up += 1;
					row++;
				}
				else{
					up += 1;
					break;
				}
			}                

			row = 1;
			total *= up;
                             
			while(i + row < ROW){
				if(MAP[i][j] > MAP[i + row][j]){
					down += 1;
					row++;
				}
				else{
					down += 1;
					break;
				}
			}

			row = 1;
			total *= down;

			while(j - col >= 0){
				if(MAP[i][j] > MAP[i][j - col]){
					left += 1;
					col++;
				}
				else{
					left += 1;
					break;
				}
			}

			col = 1;
			total *= left;

			while(j + col < COL){
				if(MAP[i][j] > MAP[i][j + col]){
					right += 1;
					col++;
				}
				else{
					right += 1;
					break;
				}
			}

			col = 1;
			total *= right;

			if(total > height){
				height = total;
				printf("New height at {%d, %d} with current tree height of %d\n", i + 1, j + 1,MAP[i][j]);
				printf("New total is %d\n", height);
				printf("Up: %d\nDown: %d\nLeft: %d\nRight: %d\n", up, down, left, right);
			}

			total = 1;
			up = 0;
			down = 0;
			left = 0;
			right = 0;

		}
	}

	return height;

}

char * fileRead(char * name){
	char* output;
	FILE*fp = fopen(name, "r");
	int length;
	char c;
	int i = 0;

	if(fp == NULL) return NULL;

	fseek(fp, 0, SEEK_END);
	length = ftell(fp);
	fseek(fp, 0, SEEK_SET);

	output = malloc(sizeof(char) * (length + 1));
	// Need + 1 to length to account for string null terminator, '\0'

	while((c = fgetc(fp)) != EOF){
		output[i] = c;
		i++;
	}

	output[i] = '\0';
	fclose(fp);

	return output;
}

int main(){
	char * file = fileRead("data.txt");
	char * begin = file;
	int ctr = 0;
	for(int i  = 0; i < ROW; i++){
		ctr = 0;
		while(*file != '\n'){
			MAP[i][ctr] = *file - '0';
			ctr++;
			file++;
		}
		file++;
	}
	printf("Answer: %d\n", heights());
	printf("%d\n", MAP[0][0]);
}
