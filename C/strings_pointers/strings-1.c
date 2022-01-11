#include <stdio.h>
#include <locale.h>
#include <windows.h>

#define F 3
#define N 3 

// Karakterláncot elforgat / Rotate string
char *forgat(char s[], int f) {
    
    int len = strlen(s);
    char *p = &s[len - f];
    char *res = (char*)malloc(len+1);
    strcpy(res,p);
    s[len - f] = '\0';
    strcat(res,s);
    strcpy(s, res); // átalakított legyen az eredeti helyén! <- globálisan megváltoztatja / modify string only locally!
    
    return res;
}

int main() {

    setlocale(LC_ALL, "Hungarian_Hungary.1250");
    
    // Karakterlánc elforgatása többször / Roate string more than once
    char s[] = "HelloWorld";
    printf("Elforgatandó szó: %s\nMennyivel: %d\nHányszor: %d\n\n", s,F,N);
    int i;
    for (i = 0; i < N; i++) {
        char *forg = forgat(s, F);
        printf("%d. Elforgatás: %s\n", i+1,forg);
        free(forg);
    }
    
    return 0;
}