#include <stdio.h>
#include <stdlib.h>
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
