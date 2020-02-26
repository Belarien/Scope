import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

path_CSV = '/home/philipp/Documents/Code/Python/Scope/17_02_2020_MiniSampler_RFID/RFID12_1.csv'
read_data = np.genfromtxt(path_CSV, delimiter=',', skip_header=2)
read_header = np.genfromtxt(path_CSV, delimiter=',', skip_header=1, skip_footer=np.shape(read_data)[0])

data = np.delete(read_data, 2, 1)
time_offset = read_header[2]
time_increment = read_header[3]
number_DataPoints = data[:,0].size
data[:, 0] = time_increment * data[:, 0] + time_offset

data_fft =  np.fft.rfft(data[:,1])
frequency_spectrum = np.fft.rfftfreq(number_DataPoints, d=time_increment)

figure = plt.figure()
subplot_1 = figure.add_subplot(211)
subplot_2 = figure.add_subplot(212)

subplot_1.plot(data[:,0]*1E9, data[:,1], color = 'b', label = 'Output voltage')
subplot_1.set_xlim(data[0, 0]*1E9, data[number_DataPoints-1, 0]*1E9)
subplot_1.legend(loc = 'upper left')
subplot_1.set_ylabel('Amplitude (V)', fontsize = 15)
subplot_1.set_xlabel('Time (ns)', fontsize = 15)
subplot_1.grid(True)

subplot_2.plot(frequency_spectrum/1E6, abs(data_fft)/max(abs(data_fft)), color = 'r', label = 'Output voltage')
subplot_2.set_xlim(frequency_spectrum[0]/1E6, frequency_spectrum[100]/1E6)
subplot_2.legend(loc = 'upper left')
subplot_2.set_ylabel('abs(fft)', fontsize = 15)
subplot_2.set_xlabel('Frequency (MHz)', fontsize = 15)
subplot_2.grid(True)

plt.show()