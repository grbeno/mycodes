// File pointer - 1

FILE *fp;

fp = fopen("teszt.txt","r");
if(!fp){
 perror("");
 return fp;
}

/* Műveletek fájlokkal / file handling */

fclose(fp);