import sys
from matplotlib.transforms import Bbox
import numpy as np
import matplotlib.pyplot as plt
from numpy.lib.function_base import median


def main(filename):
    print(filename)
    dataset = np.loadtxt(filename, delimiter=';', skiprows=1)
    labels = open(filename).readlines()[0].rstrip().split(';')

    np.set_printoptions(precision=4)

    for i in range(len(labels)):
        fig1, ax1 = plt.subplots()
        ax1.set_title(labels[i])
        ax1.boxplot(dataset[:,i])
        
        np.set_printoptions(precision=4)
        text = "min = " + str(min(dataset[:,i])) + "\nmax = " + str(max(dataset[:,i])) + "\nmean = " + str(np.round(np.average(dataset[:,i]), 4)) + "\nmedian = " + str(np.round(median(dataset[:,i]),4))
        box = dict(boxstyle='round', facecolor='white', alpha=0.5)
        ax1.text(0.03,0.8,text, transform=ax1.transAxes, bbox=box)
        ax1.set_xlabel('dataset')

        if(i<8):
            ax1.set_ylabel('nanoseconds')
        if(i == 8):
            ax1.set_ylabel('packets')
        if(i == 9):
            ax1.set_ylabel('packets')
        if(i == 10):
            ax1.set_ylabel('bytes')
        if(i == 11):
            ax1.set_ylabel('bytes')
        if(i == 12):
            ax1.set_ylabel('files')

        plt.savefig(labels[i]+".png")
        if i >= 6 and i <=8:
            fig2, ax2 = plt.subplots()
            ax2.plot(dataset[:,i])
            ax2.set_title(labels[i])
            ax2.text(0.03,0.8,text, transform=ax1.transAxes, bbox=box)
            ax2.set_xlabel('datapoint')

            if(i<8):
                ax2.set_ylabel('nanoseconds')
            if(i == 8):
                ax2.set_ylabel('packets')
            plt.savefig(labels[i]+"_time.png")




main(sys.argv[1])
