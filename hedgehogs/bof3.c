// gcc -m32 -fno-stack-protector -no-pie -o bof3 bof3.c


#include <stdio.h>
#include <string.h>

char buffer[32];

void vuln(){
    char local[32];
    printf("buffer: 0x%x\n", &buffer);
    fgets(local, 128, stdin);
    strcpy(buffer, local);
    return ;
}

int main(int argc, char *argv[]) {
    vuln();
    return 0;
}
