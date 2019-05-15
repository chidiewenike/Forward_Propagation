import numpy as np, matplotlib.pyplot as plt, sys

lines = [line.rstrip('\n').split() for line in open(sys.argv[1])]
layer_marker = 0
layers = []
for i in range(int(lines[0][0])):
    layer = np.array([float(k) for k in (lines[1:])[(2*i)+2+layer_marker]])
    for j in range((2 * i) + 3 + layer_marker, ((2*i)+2+layer_marker) + 
                   int((lines[1:])[(2 * i) + 1 + layer_marker][0])):
        layer=np.vstack((layer,np.array([float(k) for k in(lines[1:])[j]])))
    layers.append(layer)
    layer_marker += int((lines[1:])[(2 * i) + 1 + layer_marker][0])
input_data=[np.array(line.rstrip('\n').split()).astype(float) 
            for line in sys.stdin.readlines()]

output = []
for data in input_data:
    curr_pred = data[len(data)-2:len(data)]
    for layer in layers:
        curr_pred = np.heaviside(np.dot(layer,np.append(curr_pred,1.0)),0)
    output.append(curr_pred)

for i in range (len(input_data)):
    print(str(int(output[i])) + " " + 
          str(float(input_data[i][len(input_data[0])-2])) + " " + 
          str(float(input_data[i][len(input_data[0])-1])))