#include <stdio.h>
#include <time.h>

// Életkor meghatározása / get age

int szev = 1987;
int szho = 01;
int szn = 7;
int e, h, n;

time_t t, tt;
time(&tt);
struct tm sznap = { 0 }, most = *localtime(&tt);

// Aktuális idő / Actual time
e = most.tm_year + 1900;
h = most.tm_mon + 1;
n = most.tm_mday;
    
// Születésnap / Birthday
sznap.tm_year = szev - 1900;
sznap.tm_mon = szho - 1;
sznap.tm_mday = szn;

t = mktime(&sznap);

// Kiíratás / Printing
double diff = difftime(tt,t) / (60*60*24*365); // különbség sec-ben évekre átszámítva / differences in seconds convert to years
printf("Ön %.0f éves!\n", diff);