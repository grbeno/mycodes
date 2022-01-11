#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define BUF 256

// How many rows do we have?

int sorok(FILE *fp) {
    int sor = 0, aktpoz = ftell(fp);
    char *fbuf = malloc(BUF);
    fseek(fp, 0L, SEEK_SET);
    while (fgets(fbuf, BUF, fp) != NULL)
        sor++;
    fseek(fp, aktpoz, SEEK_SET);
    free(fbuf);
    return sor;
}

int main() {

    FILE *fp = fopen("teszt.txt","r");
    if (!fp) {
        perror("");
        return fp;
    }

    char fbuf[BUF], **adat, *temp;
    int sorsz = sorok(fp);
    adat = malloc(sizeof(char*)*sorsz);
    
    // Adatok tömbbe mentése - egy sor egy adatot tartalmaz / Datas to arrays - one row is one data
    int m = 0;
    while (fgets(fbuf, BUF, fp) != NULL) {
        fbuf[strlen(fbuf) - 1] = '\0';
        adat[m] = malloc(strlen(fbuf) + 1);
        strcpy(adat[m], fbuf);
        m++;
    }
    
    // Ábécé sorrend / Alphabetical order
    for (int i = 0; i < m; i++)
        for (int j = i + 1; j < m; j++) {
            if (strcmp(adat[i], adat[j]) > 0) {
                temp = malloc(strlen(adat[i]) + 1);
                strcpy(temp, adat[i]);
                adat[i] = realloc(adat[i], strlen(adat[j]) + 1);
                strcpy(adat[i], adat[j]);
                adat[j] = realloc(adat[j], strlen(temp) + 1);
                strcpy(adat[j], temp);
                free(temp);
            }
        }

    // Rendezett sorrend kiíratása / Printing ordered data
    for (int i = 0; i < m; i++) {
        printf("%d.%s\n", i + 1, adat[i]);
        free(adat[i]);
    }
    free(adat);

    fclose(fp);

    return 0;
}