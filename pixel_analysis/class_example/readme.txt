	*** pixel_analysis/class_example/class_sample.py ***

	This is one of my first effort to create python code using oo paradigm.
	With this code I would like to presenting an example for a self-created 'analysis class'.
	There are a lot of image processing methods in the universe and later can be tricky extending the class with new ones.
	The only method applied here is euclidean distance measuring between pixel (image) and sample (object) rgb values.
	Input images are about agricultural objects, flowering (colza in this case), other plant phenophases, diseases etc.
	/* I hope this class will be really extendable and maintainable. */


	* Python libraries you need to import:
	
	- os, math
	- you need to download & install with pip or something like that: 
		o PIL -> Image
	
	** Methods:

	- constructor
		o args: path <- path of image, plant <- type of plant on the image, sample <- typical rgb of the object, limit <- max. distance from the sample  
		o initialize the instances
	- init_image
		o args: fname <- name of the image file, mode <- None by default, or L(greyscaled), RGB etc.
		o open new image file, prepare image attributes for the instances: pixels, width, height, size 
	
	* Methods for technical issues -> "METHOD type:1"
	
	- mkdirIfNotExists
		o args: folderPath <- path of new folder
		o create new folder if not exists (called for the results.txt later in the code)
	- percent
		o args: elem <- amount of relevant pixels
		o returns relative appearances of the relevant pixels
	
	* Methods for image anlysing issues -> "METHOD type:2" 
	
	- euclidean
		o args: px <- pixel of the image in rgb to compare with sample rgb
		o returns distances of pixel rgbs and sample rgb
		o limit is for max. distances from the sample rgb <- (there is no object (flower, leaf etc.) represented by only one rgb value)
	- distance
		o args: -
		o euclidean method applied on every pixels!
	
	* Run the methods:

	- run_analysis
		o args: -
		o iterating over the image files
		o calling the init_image to open image and get image attributes
		o calling the type2 methods to analyse images
		o closing the current image 
		o appending the results of type2 methods to lists	
	
	* Get the results:

	- result_table
		o args: -
		o writing the lists of results to txt file in table format

	

