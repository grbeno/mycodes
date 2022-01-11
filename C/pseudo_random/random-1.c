#include <stdio.h>
#include <time.h>
#include <locale.h>
#include <windows.h>
#include <stdbool.h>

#define UPPER 35
#define LOWER 1
#define INTV (UPPER - LOWER + 1) + LOWER // ebben az intervallumban //+1 = benne van az upper is! (interval)
#define LOTTO 7
#define N 2

int main() {

    setlocale(LC_ALL, "Hungarian_Hungary.1250");
    
    // Random
    time_t t;
    srand((unsigned)time(&t));
    int i, j, k, r, temp = 0;
    
    printf("Random sorok ismétlésekkel\n");
    for (j = 0; j < N; j++) {
        printf("%d. sor: ", j + 1);
        for (i = 0; i < LOTTO; i++) {
            r = rand() % INTV;
            printf("%d ", r);
        }
        printf("\n");
    }
    
    // Ne legyen ismétlődés... avoid repetition
    bool arr[INTV] = {0};
    int szamok[N][LOTTO];
    printf("\nRandom sorok ismétlések nélkül\n");
    for (j = 0; j < N; j++) {
        printf("%d. sor: ", j+1);
        for (i = 0; i < LOTTO; i++) {
            r = rand() % INTV;
            if (!arr[r]) {
                szamok[j][i] = r;
                printf("%d ", r);
            }
            else
                i--;
            arr[r] = 1;
        }
        memset(arr, 0, sizeof(arr));
        printf("\n");
    }

    // Emelkedő sorrendbe... ascending order
    printf("Emelkedő sorrendben:\n");
    for (k=0;k<N;k++) {
        for (i=0;i<LOTTO;i++) {
            for (j = i + 1; j<LOTTO;j++) {
                if (szamok[k][i] > szamok[k][j]) {
                    temp = szamok[k][i];
                    szamok[k][i] = szamok[k][j];
                    szamok[k][j] = temp;
                }
            }
        }
    }
    
    // Kiíratás... print
    for (i = 0; i < N; i++) {
        printf("%d. sor: ", i + 1);
        for (j = 0; j < LOTTO; j++)
            printf("%d ", szamok[i][j]);
        printf("\n");
    }
    
    return 0;
}