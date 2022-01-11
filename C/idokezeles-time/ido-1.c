#include <stdio.h>
#include <time.h>

// Aktuális dátum, rendszeridő és másodpercekben eltelt idő kiíratása / Actual date, systime and elapsed time in seconcds

time_t t;
time(&t);
struct tm aktualis_ido = *localtime(&t);
    
char buff[100];

// Kiírja a dátumot és a rendszeridőt a képernyőre / Printing the date and sytime on the screen
strftime(buff,64,"Dátum: %Y.%m.%d - rendszer idő: %H:%M:%S", &aktualis_ido);
printf("%s\n", buff);
    
// Másodpercekben eltelt idő <- 1970. január 1-je óta számolja / Elapsed time in seconds from 01.01.1970
printf("%d másodperc telt el 1970 óta!\n", t);
printf("%d év telt el 1970 óta!\n", t / (60 * 60 * 24 * 365));