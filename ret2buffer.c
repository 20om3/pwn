// sudo sysctl -w kernel.randomize_va_space=0
//gcc -m32 -z execstack -fno-stack-protector -o ret2buffer ret2buffer.c

#include <stdio.h>
#include <string.h>

void vuln_func(char** argv) {
  char buf[100] = {};  /* set all bytes to zero */
  
  printf("buf = %p\n", buf);
  strcpy(buf, argv[1]);
  puts(buf);
  
  return;
}

int main(int argc, char *argv[])
{
  vuln_func(argv);

  return 0;
}
