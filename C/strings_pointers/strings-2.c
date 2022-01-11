#include <stdio.h>
#include <locale.h>
#include <windows.h>

// Fájlnév érvényesség / Filename is valid?
int fval(char *s, char *kit) {
    
    char *ptr = strchr(s, '.') + 1;
    if (strcmp(ptr, kit) != 0)
        return 1;
    
    return 0;
}

int main() {
    
    // Magyar nyelvű konzol / Hungarian language in console
    setlocale(LC_ALL, "hun");
    
    char *fnev = "pelda.txt", *kit = "txt";
    printf("Ellenőrzi, hogy a fájlnév %s kiterjesztésű-e?\n", kit);
    if (fval(fnev, kit) == 0)
        printf("A %s: Helyes fájlnév!\n", fnev);
    else
        printf("A %s: Helytelen fájlnév\n", fnev);
    
    return 0;
}