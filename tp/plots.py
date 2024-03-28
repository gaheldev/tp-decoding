import matplotlib
matplotlib.rcParams.update({'font.size': 22})

import matplotlib.pyplot as plt # matlab-like plot library



def plot_ecog(ecog, channel_selection=None):
    """
        plot ecog channels

        ecog is expected of shape (samples, channels)
        channel_selection is an optional array-like of the indexes of channels to display
    """
    if channel_selection is None:
        channel_selection = list(range(ecog.shape[1]))

    n = len(channel_selection)

    fig = plt.figure(figsize=(50, 5*n))

    axs = fig.subplots(nrows=n,
                       ncols=1, 
                       sharex=True,
                       sharey=True)

    if n ==1:
        axs = [axs] # axs is not a list if n=1

    for i, c in enumerate(channel_selection):
        axs[i].plot(ecog[:,c])
        axs[i].set_ylabel(f'Channel {c}')

