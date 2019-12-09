num_list=[2,3,4,5,6,7,8,11,12,19,18,0,21]
filtered_list=list(filter(lambda num:(num>7),num_list))
print(filtered_list)
mapped_list=list(map(lambda num:num%2,num_list))
print(mapped_list)