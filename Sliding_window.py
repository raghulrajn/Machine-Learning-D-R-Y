def sliding_window(arr:np.ndarray, window_size:int = 1, step:int=0)->np.ndarray:
    """Assuming a time series with time advancing along dimension 0,
	window the time series with given size and step.

    :param arr : input array.
    :type arr: numpy.ndarray
    :param window_size: size of sliding window.
    :type window_size: int
    :param step: step size of sliding window. If 0, step size is set to obtain 
        non-overlapping contiguous windows (that is, step=window_size). 
        Defaults to 0.
    :type step: int

    :return: array 
    :rtype: numpy.ndarray
    """
    n_obs = arr.shape[0]
    # validate arguments
    if window_size > n_obs:
        raise ValueError(
            "Window size must be less than or equal "
            "the size of array in first dimension."
        )
    if step < 0:
        raise ValueError("Step must be positive.")

    n_windows = 1 + int(np.floor( (n_obs - window_size) / step))

    obs_stride = arr.strides[0]
    windowed_row_stride = obs_stride * step

    new_shape = (n_windows, window_size) + arr.shape[1:]
    new_strides = (windowed_row_stride, ) + arr.strides

    strided = np.lib.stride_tricks.as_strided(
        arr,
        shape=new_shape,
        strides=new_strides,
    )
    return strided


# data = sliding_window(dataframe.to_numpy(),window_size = 130, step = 130)
