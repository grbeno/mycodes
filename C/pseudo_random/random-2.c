#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <locale.h>
#include <windows.h>
#include <stdbool.h>

#define ELEM 5
#define MAX 10 //leghosszabb előforduló név

int main() {

    setlocale(LC_ALL, "Hungarian_Hungary.1250");
    
    // Adatok kiiíratása random sorrendben
    
    char *nevek[] = { "Béla","Mária","Józsi","Anna","Baltazár" };
    int i, r;
    
    srand(time(NULL));
    int arr[ELEM] = { 0 };

    //random sorrend... random order
    printf("Véletlen sorrendben: ");
    for (i = 0; i < ELEM; i++) {
        r = rand() % ELEM;
        if (!arr[r])
            printf("%s ", nevek[r]);
        else
            i--;
        arr[r] = 1;
    }
    memset(arr, 0, sizeof(arr));

    //memória foglalás... allocate memory
    char **nevsor = malloc(sizeof(char*)*ELEM);
    for (i = 0; i < ELEM; i++) {
        nevsor[i] = malloc(MAX); //másoláskor változóak a méretek, 2.megoldás: realloc() a rendező függvényben!
        strcpy(nevsor[i], nevek[i]);
    }
    
    //rendezés ábécé sorrendbe... to alphabetical order
    int j, k;
    char *temp;
    for (j = 0; j < ELEM; j++) {
        for (k = j + 1; k < ELEM; k++) {
            if (strcmp(nevsor[j], nevsor[k]) > 0) { //magyar ábécére nem jó!
                temp = malloc(strlen(nevsor[j])+1);
                strcpy(temp, nevsor[j]);
                strcpy(nevsor[j], nevsor[k]);
                strcpy(nevsor[k], temp);
                free(temp);
            }
        }
    }
    
    //kiíratás ábécé sorrendben... print
    printf("\nÁbécé sorrendben: ");
    for (i = 0; i < ELEM; i++)
        printf("%s ", nevsor[i]);
    
    //memória felszabadítás... free memory
    for (i = 0; i < ELEM; i++)
        free(nevsor[i]);
    free(nevsor);
    

    return 0;
}