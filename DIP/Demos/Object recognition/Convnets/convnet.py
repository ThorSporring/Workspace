#!/usr/bin/env python
# coding: utf-8

# # Convnet exercise
# 
# In this exercise you will be implementing a (pretty slow) convnet! 

# ## Preliminaries

# In[1]:


import numpy as np
import scipy.signal
import matplotlib.pyplot as plt
import matplotlib


# ## Feedforward network


def onehot(t, num_classes):
    out = np.zeros((t.shape[0], num_classes))
    for row, col in enumerate(t):
        out[row, col] = 1
    return out

def linear(x):
    return x

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def tanh(x):
    return (np.exp(x)-np.exp(-x)) / (np.exp(x)+np.exp(-x))

def relu(x):
    return np.maximum(0, x)

def softplus(x):
    return np.log(np.exp(x) + 1)

class LinearLayer():
    def __init__(self, num_inputs, num_units, scale=0.01):
        self.num_units = num_units
        self.num_inputs = num_inputs
        self.W = np.random.normal(size=(num_inputs, num_units), scale=scale)
        self.b = np.zeros(num_units)

    def __str__(self): 
        return "LinearLayer(%i, %i)" % (self.num_inputs, self.num_units)

    def fprop(self, x, *args):
        self.x = x
        self.a = np.dot(x, self.W) + self.b
        return self.a
        
    def bprop(self, delta_in):
        x_t = np.transpose(self.x)
        self.grad_W = np.dot(x_t, delta_in)
        self.grad_b = delta_in.sum(axis=0)
        W_T = np.transpose(self.W)
        self.delta_out = np.dot(delta_in,W_T)
        return self.delta_out
        
    def update_params(self, lr):
        self.W = self.W - self.grad_W*lr
        self.b = self.b - self.grad_b*lr
        
class SigmoidActivationLayer():
    def __str__(self): 
        return "Sigmoid()"
    
    def fprop(self, x, train=True):
        self.a = 1.0 / (1+np.exp(-x))
        return self.a
        
    def bprop(self, delta_in):
        delta_out = self.a * (1 - self.a)*delta_in
        return delta_out
        
    def update_params(self, lr):
        pass
    
class TanhActivationLayer():
    def __str__(self): 
        return "Tanh()"
    
    def fprop(self, x, train=True):
        self.a = (np.exp(x)-np.exp(-x)) / (np.exp(x)+np.exp(-x))
        return self.a

    def bprop(self, delta_in):
        delta_out = (1 - ((np.exp(self.a)-np.exp(-self.a)) / (np.exp(self.a)+np.exp(-self.a))))*delta_in
        return delta_out
        
    def update_params(self, lr):
        pass

class ReluActivationLayer():
    def __str__(self): 
        return "ReLU()"

    def fprop(self, x, train=True):
        self.a = np.maximum(0, x)
        return self.a
        
    def bprop(self, delta_in):
        return delta_in * (self.a > 0).astype(self.a.dtype)
        
    def update_params(self, lr):
        pass

    
class SoftmaxActivationLayer():
    def __str__(self): 
        return "Softmax()"
    
    def fprop(self, x, train=True):
        x_exp = np.exp(x)
        normalizer = x_exp.sum(axis=-1, keepdims=True)
        self.a = x_exp / normalizer
        return self.a
        
    def bprop(self, delta_in):
        return delta_in
        
    def update_params(self, lr):
        pass

class MeanSquaredLoss():
    def __str__(self): 
        return "MeanSquaredLoss()"
    
    def fprop(self, x, t):
        num_batches = x.shape[0]
        cost = 0.5 * (x-t)**2 / num_batches
        return np.mean(np.sum(cost, axis=-1))
        
    def bprop(self, y, t):
        num_batches = y.shape[0]
        delta_out = (1./num_batches) * (y-t)
        return delta_out
        
    def update_params(self):
        pass

class CrossEntropyLoss():
    def __str__(self): 
        return "CrossEntropyLoss()"
    
    def fprop(self, x, t):
        tol = 1e-8
        return np.mean(np.sum(-t * np.log(x + tol), axis=-1))
        
    def bprop(self, y, t):
        num_batches = y.shape[0]
        delta_out = (1./num_batches) * (y-t)
        return delta_out
        
    def update_params(self):
        pass


# ## Convolution layer
# 
# 

# In[5]:


def conv_bc01(imgs, filters, padding):
    batch_size, n_channels_img, img_h, img_w = imgs.shape
    n_filters, n_channels, win_h, win_w = filters.shape
    pad_y, pad_x = padding
    if n_channels != n_channels_img:
        raise ValueError('Mismatch in # of channels')

    # Create output array
    out_h = (img_h - win_h + 2*pad_y) + 1
    out_w = (img_w - win_w + 2*pad_x) + 1
    out_shape = (batch_size, n_filters, out_h, out_w)
    out = np.zeros(out_shape)

    # Pad input images
    imgs = np.pad(imgs, ((0, 0), (0, 0), padding, padding), mode='constant')

    # Perform convolution
    for b in range(batch_size):
        for f in range(n_filters):
            for c in range(n_channels):
                out[b, f] += scipy.signal.convolve(imgs[b, c], filters[f, c], mode='valid')
    return out
    

class ConvLayer():
    def __init__(self, n_channels, n_filters, filter_size=5, scale=0.01,
                 border_mode='same'):
        self.n_channels = n_channels
        self.n_filters = n_filters
        self.filter_size = filter_size
        w_shape = (n_filters, n_channels, filter_size, filter_size)
        self.W = np.random.normal(size=w_shape, scale=scale)
        self.b = np.zeros((1, n_filters, 1, 1))
        if border_mode == 'valid':
            self.padding = 0
        elif border_mode == 'same':
            self.padding = filter_size // 2
        elif border_mode == 'full':
            self.padding = filter_size - 1
        else:
            raise ValueError('Invalid border_mode: %s' % border_mode)
        self.padding = (self.padding, self.padding)

        
    def __str__(self): 
        return ("ConvLayer(%i, %i, %i)"
                % (self.n_channels, self.n_filters, self.filter_size))

    def fprop(self, x, *args):
        '''
        Input:
            x: Array of shape (batch_size, n_channels, img_height, img_width)
        Output:
            Array of shape (batch_size, n_filters, out_height, out_width)
        '''
        # Store x for brop()
        self.x = x

        # Perform convolution
        y = conv_bc01(x, self.W, self.padding)
        
        # Add bias
        y = y + self.b
        return y
        
    def bprop(self, dy):
        # Flip weights
        w = self.W[:, :, ::-1, ::-1]
        # Transpose channel/filter dimensions of weights
        w = np.transpose(w, (1, 0, 2, 3))

        # Propagate gradients to x
        dx = conv_bc01(dy, w, self.padding)
        
        # Propagate gradients to weights
        x = np.pad(self.x, ((0, 0), (0, 0), self.padding, self.padding), mode='constant')

        self.grad_W = np.zeros_like(self.W)
        for b in range(dy.shape[0]):
            for f in range(self.W.shape[0]):
                for c in range(self.W.shape[1]):
                    self.grad_W[f, c] += scipy.signal.convolve(x[b, c], dy[b, f], mode='valid')
        self.grad_W = self.grad_W[:, :, ::-1, ::-1]

        # Propagate gradients to bias
        self.grad_b = np.sum(dy, keepdims=True, axis=(0, 2, 3))
        return dx
        
    def update_params(self, lr):
        self.W = self.W - self.grad_W*lr
        self.b = self.b - self.grad_b*lr

    def params(self):
        return self.W, self.b

    def grads(self):
        return self.grad_W, self.grad_b



# ## Pooling layer
# 

# In[6]:


class PoolLayer():
    def __init__(self, win_size=3, stride=2):
        self.win_size = win_size
        self.stride = stride
        self.padding = self.win_size // 2

    def __str__(self): 
        return "PoolLayer(%i, %i)" % (self.win_size, self.stride)

    def fprop(self, imgs, *args):
        '''
        Input:
            x: Array of shape (batch_size, n_channels, img_height, img_width)
        Output:
            Array of shape (batch_size, n_channels, out_height, out_width)
        '''
        batch_size, n_channels, img_h, img_w = imgs.shape

        # Store x for brop()
        self.imgs = imgs

        # Create output array
        out_h = (img_h - self.win_size + 2*self.padding) // self.stride + 1
        out_w = (img_w - self.win_size + 2*self.padding) // self.stride + 1
        out = np.zeros((batch_size, n_channels, out_h, out_w))
        
        # Perform average pooling
        imgs = imgs / self.win_size**2
        for b in range(batch_size):
            for c in range(n_channels):
                for y in range(out_h):
                    y_ = y * self.stride
                    for x in range(out_w):
                        x_ = x * self.stride
                        win = imgs[b, c, max(y_, 0):y_+self.win_size,
                                   max(x_, 0):x_+self.win_size]
                        out[b, c, y, x] = np.sum(win)
        return out
        
    def bprop(self, dy):
        dx = np.zeros_like(self.imgs)
        dy = dy / self.win_size**2
        for i in range(dx.shape[0]):
            for c in range(dx.shape[1]):
                for y in range(dy.shape[2]):
                    y_ = y * self.stride
                    for x in range(dy.shape[3]):
                        x_ = x * self.stride
                        dx[i, c, y_:y_+self.win_size, x_:x_+self.win_size] += dy[i, c, y, x]
        return dx

    def update_params(self, lr):
        pass

    def params(self):
        return []

    def grads(self):
        return []




# ## Flatten layer
# 

# In[7]:


class FlattenLayer():
    def __str__(self): 
        return "Flatten()"

    def fprop(self, x, *args):
        '''
        Input:
            x: Array of shape (batch_size, n_channels, img_height, img_width)
        Output:
            Array of shape (batch_size, n_channels * img_height * img_width)
        '''

        # Store shape for brop()
        self.shape = x.shape
        y = np.reshape(x, (x.shape[0], -1))
        return y

    def bprop(self, delta_in):
        return np.reshape(delta_in, self.shape)

    def update_params(self, lr):
        pass


# ## Load dataset

# In[24]:


data = np.load('mnist.npz')
num_classes = 10
x_train = data['X_train']
targets_train = data['y_train']
x_train = np.reshape(x_train, (-1, 1, 28, 28))

# Show random samples
targets_train[0]
fig, axes = plt.subplots(4, 4)
randsamples = np.random.randint(0,50000,16)
for i, ax in zip(randsamples, axes.ravel()):
    ax.matshow(x_train[i,0,:,:], cmap='gray')
    ax.set_title(targets_train[i])
    ax.set_xticks(())
    ax.set_yticks(())
plt.tight_layout()
plt.show()

#one hot encoding
targets_train = onehot(targets_train, num_classes)

#Normalize the data
mean = np.mean(x_train)
std = np.std(x_train)
x_train -= mean
x_train /= std


# ## A pretty lousy convnet!
# 
# Unfortunately, The implementation is too slow to be useful. However, lets train a small network on MNIST:
# 
# Run the code and verify that you get an accuracy above 0.2 after 150 gradient updates.

# In[11]:


num_samples, n_channels, img_h, img_w = x_train.shape


# Network architecture
layers = [
     ConvLayer(n_channels=1, n_filters=6, filter_size=5, scale=0.1),
     PoolLayer(win_size=2, stride=2),
     ReluActivationLayer(),
     ConvLayer(n_channels=6, n_filters=16, filter_size=5, scale=0.1),
     PoolLayer(win_size=2, stride=2),
     ReluActivationLayer(),
     FlattenLayer(),
     LinearLayer(1024, 64, scale=0.1),
     ReluActivationLayer(),
     LinearLayer(64, num_classes, scale=0.1),
     SoftmaxActivationLayer(),
 ]




LossLayer = CrossEntropyLoss()

def forward(x):
    for ix, layer in enumerate(layers):
        #print(ix)
        x = layer.fprop(x)
    return x

def backward(y_probs, targets):
    d = LossLayer.bprop(y_probs, targets)
    for layer in reversed(layers):
        d = layer.bprop(d)
    
def update(learning_rate):
    for layer in layers:
        layer.update_params(learning_rate)


from confusionmatrix import ConfusionMatrix
batch_size = 8
num_epochs = 1
learning_rate = 0.05
num_samples = x_train.shape[0]
num_batches = num_samples // batch_size

# Lets train the network
n_updates = 0
for epoch in range(num_epochs):
    print('epoch', epoch)
    confusion = ConfusionMatrix(num_classes)
    for i in range(num_batches):
        n_updates += 1
        idx = range(i*batch_size, (i+1)*batch_size)
        x_batch = x_train[idx]
        target_batch = targets_train[idx]
        y_probs = forward(x_batch)
        loss = LossLayer.fprop(y_probs, target_batch)
        backward(y_probs, target_batch)
        update(learning_rate)
        confusion.batch_add(target_batch.argmax(-1), y_probs.argmax(-1))
        
        if n_updates % 25 == 0:
            curr_acc = confusion.accuracy()
            print("Update %i/%i : Loss %f Train acc %f" % (n_updates, num_batches, loss, curr_acc))
    
    #decrease learning rate
        if n_updates % 400 == 0:
            learning_rate = learning_rate*0.9
            print('New Learning rate:', learning_rate)


# In[ ]:


#NB! These samples are sampled from the training data. 
#You cannot use that performance to tell anything about the real performance, since the network has allready seen the samples

# classify 16 random samples
targets_train[0]
fig, axes = plt.subplots(4, 4)
randsamples = np.random.randint(0,50000,16)

for i, ax in zip(randsamples, axes.ravel()):
    y_probs = forward(x_train[i:i+1,:,:,:])
    ax.matshow(x_train[i,0,:,:], cmap='gray')
    ax.set_title(np.argmax(y_probs))
    ax.set_xticks(())
    ax.set_yticks(())
plt.tight_layout()
plt.show()
