#include <stdio.h>
#include <time.h>

// Aktuális dátum, rendszeridő és másodpercekben eltelt idő kiíratása

time_t kezd, veg;
time(&kezd);

//A program
for (int i = 0; i < 1000000000; i++);

time(&veg);
    
//Ciklus feldolgozása alatt eltelt másodpercek
double diff = difftime(veg,kezd);
printf("A program %.0f sec alatt futott le.\n", diff);