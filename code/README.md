# capstone-starter-project

The main code used for this project is Cortex_Code.ipynb.  It is a jupyter notebook file that
runs python 3.  Make sure you have pandas version 0.24.2 installed to load the
data. Additionally, you'll need 2 pieces of data to run our code.  They can
be found in the data folder of this repository.  The data files include
Color Group.csv and the Full_Cortex_Dataset.zip.  The zip file contains the 
pickle file of the entire data set that we made.  The Color Group.csv is a data
set that takes all the we colors and renames them as a simpler color.  

Most of the code will run on its own without manually entering values, but 
there are a few spots where manual entry is used in our code.  The first is in
the binning section of the code.  We need to print the top and bottom 
engagement rates and manually enter those values later on.  There is also the 
constant printing of the regressions to get the column name.  You may possiby be
able to loop over all the column headers and just send to a list the ones that 
don't equal 0.  

All together, the data cleaning code takes the longest at just about 8 hours of
run time.  This is why we included the pickle file of our complete data set.  Next the readability
section runs super quickly and is fully automated (a few minutes max to run).  The 
readablity section is also were you can find the code to read in the complete 
data set, instead of remaking yourself.  Then comes the binning section.  
This section also runs in a few minutes time at max.  The last section is the 
double lasso section.  This one takes the longest to run, at maybe 15 minutes.
