import os 
import math
from PIL import Image


class Analysis:

    # For all instances
    # Adding headers to the lists of results
    distSum, distPerc = ["px_found"], ["(%)"]
    fname = ["Image"]
    
    " Initialize the programme "

    def __init__(self, path,plant,sample,limit):
        self.path = path
        self.img_path = f"{self.path}images\\"
        self.plant = plant
        self.sample = sample
        self.limit = limit
        # Walking through the filenames
        self.img_files = next(os.walk(self.img_path))[2]
        
    
    def __init_image(self,fname,mode=None):
        """ Opening new image file & getting attributes. 
        Warning: After calling this, you have to close the file! """
        self.image = Image.open(fname).convert(mode)
        self.pix = self.image.load()
        self.width, self.height = self.image.size
        self.imsize = self.width*self.height
    

    " METHOD type:1 "

    " Make directory if not exists "
    
    def mkdirIfNotExists(self, folderPath):
        if os.path.exists(folderPath) == False:
            os.mkdir(folderPath)
        else:
            pass
    
    " Get percent "
    
    def percent(self, elem):
        return format(elem/self.imsize*100,'.2f')

    # You can add more method here ...


    " METHOD type:2 "
    
    " 1. Method: Euclidean distance "
    
    def __euclidean(self, px):
        res, channel = 0, 3 # R-G-B
        for i in range(channel):
            res = res + (self.sample[i]-px[i])**2
        return math.sqrt(res)

    def distance(self):
        db = 0
        for i in range(self.width):
            for j in range(self.height):
                if self.__euclidean(self.pix[i,j])<=self.limit:
                    db += 1
        return db

    # You can add more method here ...
    
    
    " RUN ANALYSIS "

    def run_analysis(self):
        
        for f in self.img_files:

            " New image "
            
            self.__init_image(self.img_path+f)

            " Execute methods "
             
            self.distSum.append(self.distance()) # amount of relevant pixels
            self.distPerc.append(self.percent(self.distance())) # %
            
            # You can add more method to run here ...
            
            " Handling image file "

            self.fname.append(f) # filename
            self.image.close()

        " lists of datas -> as columns " 

        self.res_data = (
            self.fname,
            self.distSum, 
            self.distPerc 
            
            # Add more results/list here ...
        ) 
        
        return self.result_table()
    

    " OUTPUT -> TEXTFILE "

    # Table of results
    
    def result_table(self):
        resdir = f"{self.path}\\results\\" 
        self.mkdirIfNotExists(resdir)
        tabla = f"{resdir}results.txt"
        res = open(tabla,"a+")
        res.write(f"Plant type: {self.plant}\n")
        for i in range(len(self.img_files) + 1): # + 1: for header
            for m in self.res_data:
                res.write(f"{str(m[i])}\t")
            res.write("\n")
        res.close

    # You can add here more output formats, charts etc...


if __name__ == "__main__":
    
    " Input "
    
    path = "c:\\Python\\Python38-32\\myprojects\\pixel_analysis\\class_example\\"  
    plant = "Colza"
    sample = (93,118,106)
    limit = 25
    
    " Process "

    a = Analysis(path,plant,sample,limit)
    a.run_analysis()