import matplotlib
matplotlib.rcParams.update({'font.size': 22})

import matplotlib.pyplot as plt # matlab-like plot library



def plot_ecog(ecog):
    n_samples, n_channels = ecog.shape

    fig = plt.figure(figsize=(50, 5*n_channels))
    ax = fig.subplots()

    axs = fig.subplots(nrows=n_channels,
                       ncols=1, 
                       sharex=True,
                       sharey=True)

    for i in range(n_channels):
        axs[i].plot(ecog[:,i])
        axs[i].set_ylabel(f'Channel {i}')

