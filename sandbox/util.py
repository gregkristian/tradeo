from io import BytesIO
import os
from matplotlib.figure import Figure

# Create a plot from 1 dimensional list, return image url
# TODO accept panda dataframe instead
# TODO fix this
def save_plot(filename, data):
    fig = Figure()
    subplot = fig.subplots()
    subplot.plot(data)

    file_dir = '../static/' + filename
    if os.path.isfile(file_dir):
        os.remove(file_dir)

    fig.savefig(file_dir, format="png", dpi=200)
    # TODO avoid cache

    return 0
