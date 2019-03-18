# training configuration
NUM_EPOCHS = 250
LEARNING_RATE = 1
REG_CONST = 0
NUMERICAL_DELTA = 0.1
FAKE_SAMPLE_SIZE = 20

# network architecture configuration
IMAGE_SIZE = 28 * 28
HIDDEN_UNITS = 32
LAYERS_UNITS = [IMAGE_SIZE, HIDDEN_UNITS, 10]
LAYERS_NUM = len(LAYERS_UNITS)
