#include <stdio.h>
#include <stdlib.h>

int main(){

srand(1337);
int i = rand();
printf("%i",i);
int a = 0xcafebabe - 1337331 ^ i;
printf("%i",a);



return 0;

}
