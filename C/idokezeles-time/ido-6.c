#include <stdio.h>
#include <time.h>

// Hány nap van hátra karácsonyig? / How many days until Christmas?

int ev = 2020;
int ho = 12;
int nap = 24;
time_t t, tt;
time(&t);
struct tm most = *localtime(&t), akkor = { 0 };

// Christmas
akkor.tm_year = ev - 1900;
akkor.tm_mon = ho - 1;
akkor.tm_mday = nap;
akkor.tm_hour = most.tm_hour; // pontosság miatt
akkor.tm_min = most.tm_min;
akkor.tm_sec = most.tm_sec;
tt = mktime(&akkor);
double diff = difftime(tt, t) / (60 * 60 * 24);
printf("%.0f nap van még karácsonyig!\n", diff); 