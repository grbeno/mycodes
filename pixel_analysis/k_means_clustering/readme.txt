	
	*** pixel_analysis/k_means_clustering/clustering.py ***

	This python code is an implementation of k-means clustering. 
	The goal of this python class is to applying color measurement on images.
	My input image is a white masked infrared image made by satellite.
	Before clustering the dominant colors this programme filter and delete the white background from the centers. 
	/* My idea was k-means clusters could represent the dominant colors of the images. */

	* Python libraries you need to import:
	
	- os 
	- you need to download & install with pip or something like that: 
		o cv2(OpenCV), numpy, sklearn, matplotlib
	
	* Methods:
	
	- constructor
		o args: path <- path of image, clusters <- numbers of clusters
		o initialize the instances
		o open and prepare image for the instances

	- cluster_input_correction
		o args: clusters
		o set minimum cluster(=1) on case (n<1, added by user)
		/* By the way, this is just a poor input validation :( */

	- distance
		o args: pix <- current color, color <- color to compare with
		o measure distance from background color (mask) to tackle possible blurs

	- center_find
		o args: ndarr <- center , bcolor <- background color (mask)
		o find the center which represents background

	- get_cldatas
		o args: color <- color to find and delete , centers <- contains the color, clt_labels <- contains the color
		o delete background center from the centers
		o delete background labels from the labels
 		o update centers & labels

	- clustering
		o args: -
		o clustering the input image without background color (mask)
		o measure relative appearances of the labels
		o create & save a pie diagram of the results


	detected incompletion:
		* poor input validation already mentioned
		* for more images : looping -> processing
		
		

