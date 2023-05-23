# need to import at least 3 things to make your
# bokeh plots work
from bokeh.plotting import figure, show, output_file
import SelaEx19

# we specify an HTML file where the output will go
output_file("plot.html")
x = []
y = []
# load our x and y data
ourdic = SelaEx19.months("dictionar.json")
for v in ourdic.keys():
    x.append(int(v))
for z in ourdic.values():
    y.append(int(z))

# create a figure
p = figure()

# create a histogram
p.vbar(x=x, top=y, width=0.5)
#{'3': 1, '1': 2, '12': 1, '6': 2, '2': 1}
# render (show) the plot
show(p)