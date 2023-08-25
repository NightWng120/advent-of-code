#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>
#include "../commons.c"
#define num 1
#define COLS 2 
#ifdef num
#define FILE "sample.txt"
#define ROWS 16
#endif
#ifndef num
#define FILE "input.txt"
#define ROWS 2000
#endif

bool TAIL[5][6], HEAD[5][6], VISITED[5][6];

union Moves{
	int size;
	char arr[ROWS * COLS];
	char map[ROWS][COLS];
};

void step(int direction, int steps, bool axis){
	int j;
	int row = 4;
	int col = 0;
	for(j = 1; j < steps; j++){
		if(axis){
			HEAD[row + j][col] = false;
			HEAD[row + j + 1][col] = true;
			TAIL[row + j][col] = false;
			TAIL[row + j + 1][col] = true;
		}
		else{
			HEAD[row][col + j] = false;
			HEAD[row][col + j + 1] = true;
			TAIL[row][col + j] = false;
			TAIL[row][col + j + 1] = true;
		}
			
	}
}

void move(union Moves * moves){
	TAIL[4][0] = true;
	HEAD[4][0] = true;
	int direction = 0;
	bool axis = false;
	for(int i = 0; i < (strlen(moves->arr)/COLS); i++){
		if(true == TAIL[4][0]){
			HEAD[4][0] = false;
			HEAD[4][1] = true;
		}
		switch(moves->map[i][0]){
			case 'L':
				direction = 0;
				axis = false;
			case 'R':
				direction = 1;
				axis = false;
			case 'U':
				direction = 2;
				axis = true;
			case 'D':
				direction = 3;
				axis = true;

			default:
				break;
		}
		step(direction, moves->map[i][1] - '0', axis);
	}
}

void printBoard(){
	for(int i = 0; i < 5 ; i++){
		for(int j = 0; j < 5; j++){


		}
	}
}

void part1(){
	char * file = fileRead(FILE);
	int ctr = 0;
	printf("%ld\n", strlen(file));
	union Moves moves;

	char * token;
	while((token = strtok_r(file, " \n", &file))){
		for(int i = 0; i < strlen(token); i++){
			moves.arr[ctr] = *token;
			ctr++;
		}
	}

	move(&moves);
}

void part2(){
}

int main(){
	part1();
}
