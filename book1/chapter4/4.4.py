'''
편미분 기울기 계산
'''

import numpy as np

def numerical_gradient(f, x):
    h = 1e-4 # 0.0001
    grad = np.zeros_like(x)
    
    it = np.nditer(x, flags=['multi_index'], op_flags=['readwrite'])
    while not it.finished:
        idx = it.multi_index
        tmp_val = x[idx]
        x[idx] = float(tmp_val) + h
        fxh1 = f(x) # f(x+h)
        
        x[idx] = tmp_val - h 
        fxh2 = f(x) # f(x-h)
        grad[idx] = (fxh1 - fxh2) / (2*h)
        
        x[idx] = tmp_val # 값 복원
        it.iternext()   
        
    return grad

def gradient_descent(f, init_x, lr = 0.01, step_num = 100) :
    x = init_x

    for i in range(step_num) :
        grad = numerical_gradient(f, x)
        x -= lr * grad

    return x

def function_2(x) :
    return x[0]**2 + x[1]**2

# init_x = np.array([-3.0, 4.0])
# print(gradient_descent(function_2, init_x, lr=0.1, step_num=100))

def softmax(a) :
    c = np.max(a)
    exp_a = np.exp(a-c)
    sum_exp_a = np.sum(exp_a)
    y = exp_a/sum_exp_a

    return y

def cross_entropy_error(y, t) :
    if y.ndim == 1 :
        t = t.reshape(1, t.size)
        y = y.reshape(1, y.size)

    batch_size = y.shape[0]
    return -np.sum(t*np.log(y, t + 1e-7)) / batch_size

class simpleNet :
    def __init__(self) :
        self.W = np.random.randn(2, 3)

    def predict(self, x) :
        return np.dot(x, self.W)

    def loss(self, x, t) : 
        z = self.predict(x)
        y = softmax(z)
        loss = cross_entropy_error(y, t)

        return loss

net = simpleNet()
# print(net.W)
x = np.array([0.6, 0.9])
# p = net.predict(x)
# print(p)
# print(np.argmax(p))
t = np.array([0, 0, 1])
# print(net.loss(x, t))

def f(W) :
    return net.loss(x, t)

dW = numerical_gradient(f, net.W)
print(dW)