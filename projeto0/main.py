import numpy as np

def randomization(n):
    """
    Arg:
      n - an integer
    Returns:
      A - a randomly-generated nx1 Numpy array.
    """
    return np.ones([n,1])

def operations(h, w):
    """
    Takes two inputs, h and w, and makes two Numpy arrays A and B of size
    h x w, and returns A, B, and s, the sum of A and B.

    Arg:
      h - an integer describing the height of A and B
      w - an integer describing the width of A and B
    Returns (in this order):
      A - a randomly-generated h x w Numpy array.
      B - a randomly-generated h x w Numpy array.
      s - the sum of A and B.
    """
    A = np.random.rand(h,w)
    B = np.random.rand(h,w)
    s = A+B

    return A, B, s

def norm(A, B):
    """
    Takes two Numpy column arrays, A and B, and returns the L2 norm of their
    sum.

    Arg:
      A - a Numpy array
      B - a Numpy array
    Returns:
      s - the L2 norm of A+B.
    """
    s = np.linalg.norm(A+B)
    return s

def neural_network(inputs, weights):
    """
     Takes an input vector and runs it through a 1-layer neural network
     with a given weight matrix and returns the output.

     Arg:
       inputs - 2 x 1 NumPy array
       weights - 2 x 1 NumPy array
     Returns (in this order):
       out - a 1 x 1 NumPy array, representing the output of the neural network
    """
    """out = np.array([np.tanh(weights, inputs)])"""
    out = np.tanh(np.dot(weights.T, inputs))
    return out

def scalar_function(x, y):
    """
    Returns the f(x,y) defined in the problem statement.
    """
    if(x <= y):
        return x*y
    else:
        return x/y

def vector_function(x, y):
    """
    Make sure vector_function can deal with vector input x, y
    """
    def scalar_func(x, y):
        return x * y if x <= y else x / y

    vectorized_op = np.vectorize(scalar_func)  # Aplica a função elemento a elemento
    return vectorized_op(x, y)


if __name__ == "__main__":
    print(randomization(5))
    print("----------------")
    print(operations(2, 3))
    print("----------------")
    print(norm(np.array([1,2]), np.array([3,4])))
    print("----------------")
    print(neural_network(np.array([1,2]), np.array([3,4])))
    print("----------------")
    print(scalar_function(2, 3))
    print("----------------")
    print(vector_function(np.array([1,2]), np.array([3,4])))
