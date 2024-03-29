import numpy as np

# sliding window around all the data without stride configuration
def sliding_window(np_array,window_length):
    return [np_array[i:i+window_length,:] for i in range(0,(len(np_array)+1)-window_length,window_length)]

def stride_sliding_window(np_array,window_length,window_stride):
    w_list = []
    n_records = np_array.shape[0]
    remainder = (n_records-window_length) % window_stride
    num_windows = 1 + int((n_records-window_length-remainder)/window_stride)
    for i in range (num_windows):
        w_list.append(np_array[i*window_stride:window_length-1+i*window_stride+1])
    return np.array(w_list)

# np.random.seed(10101)
# np_array = np.random.rand(50,2)
# print(np_array)
# sliding_array = stride_sliding_window(np_array,6,3)
# print(sliding_array.shape)

features_delete = np.array([0])
features_delete = np.concatenate([features_delete,np.arange(46,50)])
features_delete = np.concatenate([features_delete, np.arange(59,63)])
features_delete = np.concatenate([features_delete, np.arange(72,76)])
features_delete = np.concatenate([features_delete, np.arange(85,89)])
features_delete = np.concatenate([features_delete, np.arange(98,102)])
features_delete = np.concatenate([features_delete, np.array([117])])
features_delete = np.concatenate([features_delete, np.arange(133,243)])
features_delete = np.concatenate([features_delete, np.arange(244,249)])
print (features_delete,features_delete.shape)