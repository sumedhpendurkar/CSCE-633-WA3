import mnist_loader
import network

training_data, validation_data, test_data = mnist_loader.load_data_wrapper()

## dimensions [size][x/y][784][1]
#n = ### YOUR CODE HERE ###
net = net.Network([784, n, 10])
net.SGD(training_data, 30, 10, 3.0, test_data=test_data)
