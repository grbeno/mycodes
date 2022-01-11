#include <stdio.h>
#include <time.h>

// Két dátum között eltelt idő mérése / elapsed time between two dates

// Mettől? / From?
int ev1 = 2001;
int ho1 = 11;
int na1 = 30;

// Meddig? / To
int ev2 = 2020;
int ho2 = 3;
int na2 = 11;

time_t t, tt;
struct tm kezd = { 0 }, veg = { 0 };

// Kezdő dátum / Start date
kezd.tm_year = ev1 - 1900;
kezd.tm_mon = ho1 - 1;
kezd.tm_mday = na1;

t = mktime(&kezd);

// Vég dátum / End date
veg.tm_year = ev2 - 1900;
veg.tm_mon = ho2 - 1;
veg.tm_mday = na2;
    
tt = mktime(&veg);

// A különbség kiíratása a képernyőre napokban számolva / Printing the difference in days
double diff = difftime(tt/(60*60*24),t/(60*60*24));
printf("A két dátum között eltel napok száma: %.0f nap\n", diff);

// Ha kikötöttük, hogy egésszel kell visszatérnie a függvénynek, akkor / Return result in integer
int kezd_ = t / (60*60*24);
int veg_ = tt / (60*60*24);
int diff_ = veg_ - kezd_;
printf("A két dátum között eltel napok száma: %d nap\n", diff_);