from nnet.converters.nnet2onnx import nnet2onnx

# nnet file to convert to onnx
nnetFile = "models/TestNetwork.nnet"

# ONNX file
onnxFile = 'output/TestNetwork.onnx'

# Convert the file
nnet2onnx(nnetFile, onnxFile)


# nnet file to convert to onnx
nnetFile = "models/TestNetwork2.nnet"

# ONNX file
onnxFile = 'output/TestNetwork2.onnx'

# Convert the file
nnet2onnx(nnetFile, onnxFile)