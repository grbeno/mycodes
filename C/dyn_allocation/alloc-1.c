#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <locale.h>
#include <windows.h>

#define BUF 256

// Input buffer

int getline(char s[], int lim) {
    int c, i;
    for (i = 0; i < lim && (c = getchar()) != EOF && c != '\n'; ++i)
        s[i] = c;
    s[i] = '\0';
    while (c != EOF && c != '\n')
        getchar();
    return(i);
}

int main() {
    
    setlocale(LC_ALL,"Hungarian_Hungary.1250");

    char **str, input[BUF];
    int n = 5, i = 0;
    
    // Memória foglalás: hány karakterláncra lesz szükség / Allocation - How many strings do we need?
    str = malloc(sizeof(char*)*n);
    printf("Adjon meg karakterláncokat!\n");
    while (getline(input, BUF)) {
        /*
            validáló függvény helye / Place for validation function
        */
        // Memória foglalás: hány karakterből fog állni / Allocation - How many chars do we need for the strings?
        str[i] = malloc(strlen(input) + 1);
        strcpy(str[i], input);
        i++;
        if (i == n)
            break;
    }
    if (i < n) // ha üres sorral korábban ugrik ki / if it jumps out with empty row
        n = i;
    
    // Teszt
    printf("A megadott karakterláncok:\n");
    for (i = 0; i < n; i++)
        printf("%s\n", str[i]);
    
    // Memória felszabadítás / freeing memory
    for (i = 0; i < n; i++)
        free(str[i]);
    free(str);
    
    return 0;
}