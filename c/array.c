/* Read input from STDIN. Print your output to STDOUT*/
#include<stdio.h>
#include<string.h>
#define MAXT 10
#define MAXN 1001
#define MAXLINE 1000

void input(t, n, line);
void getstr(line);
void dublicates();
void single();

int main(int argc, char *a[])
{
	int i;
	for (i = 1; i < argc; i++)
		printf("%s%s", a[i], (i < argc-1) ? " " : "");
	printf("\n");
return 0;
}

void input()
{

}
