import numpy as np
from scipy.signal import iirdesign, sosfilt, convolve



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
