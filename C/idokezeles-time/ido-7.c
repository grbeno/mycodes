#include <stdio.h>
#include <time.h>

// Dátum és idő formázása / Formating date and time

time_t t;
time(&t);
struct tm most = *localtime(&t);

char buff[100];

strftime(buff,100,"Dátum/idő: %Y.%m.%d - %H:%M:%S",&most);

/* Dátum/idő: 2020.05.14 - 14:51:42
%A -> nap: pl.: csütörtök / Day eg. Thursday
%a -> nap pl.: cs / Day eg. Th
%c -> dátum és idő együtt: Dátum/idő: 2020. 05. 14. 14:58:15 / Date and time together
A helyi beállítás setlocale() befolyásolja a kimenetet / local settings [ Hungary ]
%x -> ha nincs setlocale: HH/NN/EE, ha van: EEEE.HH.NN / without local settings
%B -> hónap név: May, ha setlocale: május
%b -> hónap név: May, ha setlocale: máj.
%I -> 01-12 óra formátum
%H -> 00-23 óra formátum
%j -> az év hányadik napja 001-366 */