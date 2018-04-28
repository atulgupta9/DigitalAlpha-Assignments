import numpy as np

def output_through_sigmoid(var_list):
    output_list = []
    for i in var_list:
       output_list.append(1/(1 + np.exp(-i)))
    return output_list
    
input_matrix = [0.05,0.10]
weight_matrix_1 = [[0.15,0.2],[0.25,0.3]]
weight_matrix_2 = [[0.40,0.45],[0.50,0.55]]
bias_1 =[0.35,0.35]
bias_2 = [0.6,0.6]
net_h_layer_matrix = np.matmul(weight_matrix_1,input_matrix) + bias_1
out_h_layer_matrix = output_through_sigmoid(net_h_layer_matrix)

net_o_layer_matrix = np.matmul(weight_matrix_2,out_h_layer_matrix) + bias_2
out_o_layer_matrix = output_through_sigmoid(net_o_layer_matrix)

target_matrix = [0.01,0.99]
error_o1 = 0.5 *( (target_matrix[0]- out_o_layer_matrix[0])**2)
error_o2 = 0.5 *( (target_matrix[1]- out_o_layer_matrix[1])**2)
error_total = error_o1 + error_o2

 