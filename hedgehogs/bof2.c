#include <stdio.h>

int main(int argc, char *argv[]) {
    char buffer[10];
    int zero = 0;

    fgets(buffer, 64, stdin);
    printf("zero = %x\n", zero);
    if (zero == 0x12345678) {
        printf("Congratulations !!\n");
    }
    return 0;
}
