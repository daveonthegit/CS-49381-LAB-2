
#include <stdio.h>
#include <unistd.h>

int main_good(){
    fprintf(stdout, "This function does something good.\n");
    fprintf(stdout, "Something good is happening.\n");
    fflush(stdout);
    return 0;
}

int main_evil(){
    fprintf(stdout,"This function does something bad.\n");
    fprintf(stdout,"Something bad is happening.\n");
    fflush(stdout);
    return 0;
}