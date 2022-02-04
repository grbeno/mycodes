// File pointer - 2 

#define VALTO 1024
FILE *fp;

fp = fopen("teszt.txt","r");
if(!fp){
 perror("");
 return fp;
}

// Fájlméret / size of file
float fmeret(FILE *fp) {
    float res;
    int pos = ftell(fp);
    fseek(fp, 0L, SEEK_END);
    res = (float)ftell(fp);
    fseek(fp, pos, SEEK_SET);
 
 return res /VALTO;

}

fclose(fp);