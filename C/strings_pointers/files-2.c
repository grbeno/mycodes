// File pointer - 2 

#define VALTO 1024

// Fájlméret / size of file
float fmeret(FILE *fp) {
    float res;
    int pos = ftell(fp);
    fseek(fp, 0L, SEEK_END);
    res = (float)ftell(fp);
    fseek(fp, pos, SEEK_SET);
 
 return res / VALTO;

}