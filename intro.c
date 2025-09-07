#include <stdio.h>
int main() {
   printf("Hello!\n");
   printf("What is your name?\n");
   char name[50];
   scanf("%s", name);
   printf("What is your favorite number?\n");
   int f;
   scanf("%d", &f);
   int numtwo = f*2;
   printf("Hi %s",name);
   printf("! Your favorite number doubled is %d", numtwo);
   printf(".\n");
   return 0;
}