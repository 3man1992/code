#phy template-gui params.py - params.py is contained within the znas kilosort file
import numpy as np

#Change variables to match the data to analyse
spike_times = '/Users/laurence/Desktop/Neuroscience/mproject/Ephys/spike_times.npy'
amplitudes = '/Users/laurence/Desktop/Neuroscience/mproject/Ephys/amplitudes.npy'

#Load files
spike_times = np.load(spike_times)
amplitudes = np.load(amplitudes)

#Print data
print("Here are the spike times", spike_times)
print("Here are the amplitudes", amplitudes)
