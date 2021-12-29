import csv
import random
import plotly_express as px
import plotly.figure_factory as ff
import statistics
import plotly.graph_objects as go
count= []
dice_result= []

for i in range(0,1000):
    dice1 =random.randint(1,6)
    dice2 = random.randint(1,6)
    dice_result.append(dice1+dice2)

    count.append(i)
  #  print(i,dice_result)
mean=sum(dice_result)/1000
standard_deviation = statistics.stdev(dice_result)

median= statistics.median(dice_result)
mode= statistics.mode(dice_result)

first_std_dev_start,first_std_dev_end = mean-standard_deviation,mean+standard_deviation
second_std_dev_start,second_std_dev_end = mean-(2*standard_deviation),mean+(2*standard_deviation)
third_std_dev_start,third_std_dev_end = mean-(3*standard_deviation),mean+(3*standard_deviation)

list_of_data_withing_one_standard_deviation = [result for result in dice_result 
if result>first_std_dev_start and result<first_std_dev_end]

print("{}% of data lies within one standard deviation".format(len(list_of_data_withing_one_standard_deviation)*100.0/len(dice_result)))

list_of_data_withing_two_standard_deviation = [result for result in dice_result 
if result>second_std_dev_start and result<second_std_dev_end]

print("{}% of data lies within two standard deviation".format(len(list_of_data_withing_two_standard_deviation)*100.0/len(dice_result)))

list_of_data_withing_three_standard_deviation = [result for result in dice_result 
if result>third_std_dev_start and result<third_std_dev_end]

print("{}% of data lies within three standard deviation".format(len(list_of_data_withing_three_standard_deviation)*100.0/len(dice_result)))
print(mean,mode,median,standard_deviation)

#fig = px.bar(x= dice_result,y = count)
fig = ff.create_distplot([dice_result],["result"])
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[first_std_dev_start, first_std_dev_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1"))
fig.add_trace(go.Scatter(x=[first_std_dev_end, first_std_dev_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1"))
fig.add_trace(go.Scatter(x=[second_std_dev_start, second_std_dev_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2"))
fig.add_trace(go.Scatter(x=[second_std_dev_end, second_std_dev_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2"))
fig.show()