	*** python_gui/tkinter_sample.py ***

	GUI (Graphical User Interface) helps users to add input data processing by programmes. 
	I used tkinter here to present a simple user window with some tkinter widgets e.g. labels, entries (input field), spinboxes, comboboxes etc.

	
	* Python libraries you need to import:
	
	- 'from tkinter import ttk, messagebox'

	- After the necessary imports you can see functions for the submit buttons 
		o  calling messageboxes to show values added by user 
	
	** Methods:
	
	- constructor
		o args: -
		o initialize the instances
		o adding title to the top of the window
		o index, left_column, right_column instance variables are responsible for widget ordering
		o setting radio button to default=2

	** Widgets:
	
	- after constructor you can see some tkinter widgets
		o grids are responsible for paddings & placing to rows, columns
	- placing issues
		o (index += 1) : the next (after current) widget instance will always in the next row
		o (row = index-1) : the current widget will in the same row with the former one
		o left_column = 1 : placing widgets in the first column of the grid
		o right_colum = 2 : placing widgets in the second column of the grid
	
	- after Form class
		o defining the widgets as instances one after another according to their placing parameters 
	

	** Ideas: 
		o It would be great if widget rows & columns would be more flexibile <- more control by the user
	

	
	 
	 