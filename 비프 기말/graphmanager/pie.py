import matplotlib.pyplot as plt

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
sizes = [15, 30, 45, 10]
explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')
i=0
while True:
        plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
                shadow=True, startangle=i%360)
        i+=30
        plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

        plt.draw()
        plt.pause(1)
        plt.clf()