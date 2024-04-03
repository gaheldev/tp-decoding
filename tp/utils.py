import numpy as np
from scipy.signal import iirdesign, sosfilt, convolve
from librosa.util import frame




def buffering_power(X, win_size=1000, hop=40, n_buffer=1):
    """
        Compute signal's power over overlapping frames of length 'win_size'
        with hop length of 'hop'

        if n_buffer > 1, each resulting timestep concatenates the n_buffer previous frames to the features
        
        return an array of size (trials, features) with features=n_buffer*n_channels
    """
    n_channels = X.shape[1]
    X_buffer = pad(np.power(X, 2), frame_length=win_size, hop=hop)
    X_buffer = frame(X_buffer, frame_length=win_size, hop_length=hop, axis=0)
    n_trials = X_buffer.shape[0]
    return np.mean(X_buffer.reshape(n_trials,
                                    n_buffer,
                                    win_size//n_buffer,
                                    n_channels),
                   axis=2
                   ).reshape(n_trials,
                             n_buffer*n_channels)

def buffering(X, win_size=1000, hop=40, n_buffer=1):
    """
        Compute signal's power over overlapping frames of length 'win_size'
        with hop length of 'hop'

        if n_buffer > 1, each resulting timestep concatenates the n_buffer previous frames to the features
        
        return an array of size (trials, features) with features=n_buffer*n_channels
    """
    n_channels = X.shape[1]
    X_buffer = pad(X, frame_length=win_size, hop=hop)
    X_buffer = frame(X_buffer, frame_length=win_size, hop_length=hop, axis=0)
    n_trials = X_buffer.shape[0]
    return X_buffer.reshape(n_trials,
                                    n_buffer,
                                    win_size//n_buffer,
                                    n_channels)

def common_average_reference(X, axis=1):
    average = np.mean(X, axis=axis).reshape(-1,1) # we need an extra empty axis to repeat along it
    return X - np.repeat(average, X.shape[axis], axis=axis)



def compute_band_filters(bands, fs=1000):
    def ws(wp):
        return (0.9 * wp[0],
                1.1 * wp[1]
               )
    return [iirdesign(wp, ws(wp), 1, 60, analog=False, fs=fs, output='sos') for wp in bands]



def pad(X, frame_length=200, hop=40):
    return np.pad(X, [(frame_length-hop, 0), (0, 0)])



def power(frame):
    """ computes signal's power on frame of shape (samples, features) """
    return np.array([np.sum(frame[:,i]**2) for i in range(frame.shape[1])])



def lag(X, n, axis=0, keep_length=True):
    """ 
        add n samples of lag to an axis of X by duplicating first or last sample

        X: numpy array
        axis: axis on which to apply the lag
        keep_length: strip the extra samples 
    """
    axis_pad = (n,0) if n >= 0 else (0,-n)
    pad_width = tuple([axis_pad if ax == axis else (0,0) for ax in range(X.ndim)])
    new_X = np.pad(X, pad_width ,'constant')
    
    if keep_length:
        slices = [slice(0,N) for N in X.shape]
        slices[axis] = slice(0,-n) if n > 0 else slice(-n, new_X.shape[axis])

        return new_X[tuple(slices)]
    else:
        return new_X
