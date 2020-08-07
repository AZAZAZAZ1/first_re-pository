
#We will import the following libraries.

import pandas as pd
from bokeh.plotting import figure, output_file, show,output_notebook
output_notebook()

# In this section, we define the function make_dashboard. You don't have to know how the function works, you should only care about the inputs. The function will produce a dashboard as well as an html file. You can then use this html file to share your dashboard. If you do not know what an html file is don't worry everything you need to know will be provided in the lab.


def make_dashboard(x, gdp_change, unemployment, title, file_name):
    output_file(file_name)
    p = figure(title=title, x_axis_label='year', y_axis_label='%')
    p.line(x.squeeze(), gdp_change.squeeze(), color="firebrick", line_width=4, legend="% GDP change")
    p.line(x.squeeze(), unemployment.squeeze(), line_width=4, legend="% unemployed")
    show(p)


#The dictionary links contain the CSV files with all the data. The value for the key GDP is the file that contains the GDP data. The value for the key unemployment contains the unemployment data.
    
links={'GDP':'https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/projects/coursera_project/clean_gdp.csv',\
       'unemployment':'https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/projects/coursera_project/clean_unemployment.csv'}


#_______________________________________________________________


#Create a dataframe that contains the GDP data and display using the method head() and take a screen shot.

# Create a dataframe that contains the unemployment data. Display the first five rows of the dataframe using the method head() and take a screen shot.

# Display a dataframe where unemployment was greater than 8.5% . Take a screenshot

# Us the function make_dashboard to make a dashboard, then take a screen shot.

# input the link for your notebook generated from Watson Studio .

