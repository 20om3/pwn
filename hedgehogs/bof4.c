//gcc -m32 -no-pie -o bof4 bof4.c

#include <stdio.h>
#include <string.h>

void vuln(){
    char msg[] = "Hello\n";
    char buf[32];
    write(1, msg, strlen(msg));
    read(0, buf, 128);
    return;
}

int main(int argc, char *argv[]) {
    vuln();	
    return 0;

}
