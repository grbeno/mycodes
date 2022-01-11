#include <stdio.h>
#include <stdlib.h>

#define M 5
#define N 3

int main() {
    
    int **arr, i, j;
    
    // Memória foglalás / Allocate memory
    arr = malloc(sizeof(int*) * M); // sorok / rows
    for (i = 0; i < M; i++)
        arr[i] = malloc(sizeof(int) * N); // oszlopok / columns
    
    // Értékadás, kiíratás / values & printing
    for (i = 0; i < M; i++) {
        for (j = 0; j < N; j++) {
            arr[i][j] = j + i;
            printf("%d ", arr[i][j]);
        }
        printf("\n");
    }
    
    // Memória felszabadítás / Freeing memory
    for (i = 0; i < M; i++)
        free(arr[i]);
    free(arr);
    
    return 0;
}