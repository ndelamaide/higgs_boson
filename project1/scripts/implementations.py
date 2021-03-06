import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def gradient_logistic(tx, y, w):
    """Computes the gradient for Logistic Regression"""
    """INPUTS : vector with data (tx, y), the weights w"""
    """OUTPUTS : the gradient"""
    h = sigmoid(tx.dot(w))
    return np.matmul(tx.T, (h - y))

def loss_logistic(tx, y, w):
    """Computes the loss for Logistic Regression"""
    """INPUTS : vector with data (tx, y), the weights w"""
    """OUTPUTS : the loss"""
    y[y < 0] = 0
    epsilon = 1e-5
    h = sigmoid(tx.dot(w))
    return - (np.matmul(y.T, np.log(h + epsilon)) + np.matmul((1 - y).T, np.log(1 - h + epsilon)))

def logistic_regression(y, tx, initial_w, max_iters, gamma):
    """Computes Logistic Regression with Gradient Descent"""
    """INPUTS : vector with data (tx, y), the initial w, the maximum number of iterations and the learning rate gamma"""
    """OUTPUTS : the weights w of the model and the loss"""

    y[y < 0] = 0

    # We add the offset term w0
    w0 = np.ones((y.shape[0], 1))
    initial_w = np.zeros(initial_w.shape[0] + 1)
    tx = np.hstack((tx, w0)) # We add to the data a column of 1 because of the added offset w0

    w = initial_w
    loss = 0

    for n_iter in range(max_iters):

        grad = gradient_logistic(tx, y, w)
        loss = loss_logistic(tx, y, w)

        w = w - gamma * grad

    return w, loss

def reg_logistic_regression(y, tx, lambda_, initial_w, max_iters, gamma):
    """Computes regularized Logistic Regression with Gradient Descent"""
    """INPUTS : vector with data (tx, y), the penalty coefficient lambda, the initial w, the maximum number of iterations and the learning rate gamma"""
    """OUTPUTS : the weights w of the model and the loss"""

    y[y < 0] = 0

    w0 = np.ones((y.shape[0], 1))
    initial_w = np.zeros(initial_w.shape[0] + 1)
    tx = np.hstack((tx, w0))

    w = initial_w
    loss = 0

    for n_iter in range(max_iters):

        grad = gradient_logistic(tx, y, w)
        loss = loss_logistic(tx, y, w) + lambda_ * np.squeeze(w.T.dot(w)) # L2 regularization

        w = w - gamma * (grad + 2 * lambda_ * w)

    return w, loss

def least_squares_GD(y, tx, w_initial, max_iters, gamma):
    """Compute Least Squares with Gradient Descent"""
    """INPUTS : vector with data (tx, y), the initial w, the maximum number of iterations and the learning rate gamma"""
    """OUTPUTS : the weights w of the model and the loss"""
    N = len(y)
    w = w_initial
    for i in range(max_iters) :
        mse_grad_loss = (-1/N)*np.matmul(tx.T, (y-np.dot(tx,w)))
        w = w - gamma*mse_grad_loss
    loss = (1/(2*N))*np.sum(np.square(y-np.dot(tx,w)))
    return (w, loss)

def least_squares_SGD(y, tx, w_initial, max_iters, gamma):
    """Compute Least Squares with Stochastic Gradient Descent"""
    """INPUTS : vector with data (tx, y), the initial w, the maximum number of iterations and the learning rate gamma"""
    """OUTPUTS : the weights w of the model """
    N = len(y)
    w = w_initial
    for i in range(max_iters) :
        j = np.random.randint(0,N)
        mse_grad_loss = - np.dot(tx[j].T, (y[j]-np.dot(tx[j], w)))
        w = w - gamma*mse_grad_loss
    loss = (1/(2*N))*np.sum(np.square(y-np.dot(tx,w)))
    return (w, loss)

def least_squares(y, tx):
    """Compute Least Squares with normal equations"""
    """INPUTS : vector with data (tx, y)"""
    """OUTPUTS : the weights w of the model """
    w =  np.linalg.solve(np.matmul((tx.T), tx), np.matmul((tx.T), y))
    N = len(y)
    loss = (1/(2*N))*np.sum(np.square(y-np.dot(tx,w)))
    return (w, loss)

def ridge_regression(y, tx, lambda_):
    """Compute Ridge Regresssion with normal equations"""
    """INPUTS : vector with data (tx, y) and penalty parameter lambda_"""
    """OUTPUTS : the weights w of the model """
    N = len(y)
    w =  np.matmul(np.linalg.solve((np.matmul((tx.T), tx)+lambda_*2*N*np.identity(tx.shape[1])),(tx.T)), y)
    loss = (1/(2*N))*np.sum(np.square(y-np.dot(tx,w))) + lambda_*np.sum(np.square(w))
    return (w, loss)

