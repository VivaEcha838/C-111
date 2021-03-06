import pandas as pd
import plotly.figure_factory as ff
import statistics
import random
import plotly.graph_objects as go

df = pd.read_csv("studentMarks.csv")

data = df["Math_score"].tolist()

math_mean = statistics.mean(data)
math_stdev = statistics.stdev(data)

print(math_mean)
print(math_stdev)

fig = ff.create_distplot([data],["math scores"],show_hist=False)
#fig.show()

def random_set_of_means(counter):
    dataset = []
    for i in range(0,counter):
        random_index = random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

mean_list = []
for i in range(0,1000):
    set_of_means = random_set_of_means(100)
    mean_list.append(set_of_means)

sample_mean = statistics.mean(mean_list)
sample_stdev = statistics.stdev(mean_list)

print(sample_mean)
print(sample_stdev)

stdev_1st_start = sample_mean-sample_stdev
stdev_1st_end = sample_mean+sample_stdev

stdev_2nd_start = sample_mean-(sample_stdev *2)
stdev_2nd_end = sample_mean+(sample_stdev*2)

stdev_3rd_start = sample_mean-(sample_stdev*3)
stdev_3rd_end = sample_mean+(sample_stdev*3)

print(stdev_1st_end)

fig = ff.create_distplot([mean_list],["Student Marks"], show_hist=False)

fig.add_trace(go.Scatter(x=[sample_mean , sample_mean],y=[0,0.2],mode = "lines", name = "Mean"))
fig.add_trace(go.Scatter(x=[stdev_1st_start , stdev_1st_start],y=[0,0.2],mode = "lines", name = "Standard Deviation 1st Start"))
fig.add_trace(go.Scatter(x=[stdev_1st_end , stdev_1st_end],y=[0,0.2],mode = "lines", name = "Standard Deviation 1st End"))
fig.add_trace(go.Scatter(x=[stdev_2nd_start , stdev_2nd_start],y=[0,0.2],mode = "lines", name = "Standard Deviation 2nd Start"))
fig.add_trace(go.Scatter(x=[stdev_2nd_end , stdev_2nd_end],y=[0,0.2],mode = "lines", name = "Standard Deviation 2nd End"))
fig.add_trace(go.Scatter(x=[stdev_3rd_start , stdev_3rd_start],y=[0,0.2],mode = "lines", name = "Standard Deviation 3rd Start"))
fig.add_trace(go.Scatter(x=[stdev_3rd_end , stdev_3rd_end],y=[0,0.2],mode = "lines", name = "Standard Deviation 3rd End"))

#fig.show()



df = pd.read_csv("data1.csv")
data = df["Math_score"].tolist()

mean_of_samp_1 = statistics.mean(data)
print(mean_of_samp_1)

fig = ff.create_distplot([data],["Student Marks 1st intervention"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean_of_samp_1 , mean_of_samp_1],y=[0,0.2],mode = "lines", name = "Mean of 1st Intervention"))
fig.add_trace(go.Scatter(x=[stdev_1st_end , stdev_1st_end],y=[0,0.2],mode = "lines", name = "Standard Deviation 1st End"))
fig.add_trace(go.Scatter(x=[sample_mean, sample_mean],y=[0,0.2],mode="lines", name = "Sample Mean"))

#fig.show()

df = pd.read_csv("data2.csv")
data = df["Math_score"].tolist()

mean_of_samp_2 = statistics.mean(data)
print(mean_of_samp_2)

fig = ff.create_distplot([data],["Student Marks 2nd intervention"],show_hist=False)
fig.add_trace(go.Scatter(x=[stdev_1st_end , stdev_1st_end],y=[0,0.2],mode = "lines", name = "Standard Deviation 1st End"))

fig.add_trace(go.Scatter(x=[mean_of_samp_2 , mean_of_samp_2],y=[0,0.2],mode = "lines", name = "Mean of 2nd Intervention"))
fig.add_trace(go.Scatter(x=[stdev_2nd_end , stdev_2nd_end],y=[0,0.2],mode = "lines", name = "Standard Deviation 2nd End"))
fig.add_trace(go.Scatter(x=[sample_mean, sample_mean],y=[0,0.2],mode="lines", name = "Sample Mean"))

#fig.show()

df = pd.read_csv("data3.csv")
data = df["Math_score"].tolist()

mean_of_samp_3 = statistics.mean(data)
print(mean_of_samp_3)

fig = ff.create_distplot([data],["Student Marks 3rd intervention"],show_hist=False)
fig.add_trace(go.Scatter(x=[stdev_1st_end , stdev_1st_end],y=[0,0.2],mode = "lines", name = "Standard Deviation 1st End"))
fig.add_trace(go.Scatter(x=[stdev_3rd_end , stdev_3rd_end],y=[0,0.2],mode = "lines", name = "Standard Deviation 3rd End"))
fig.add_trace(go.Scatter(x=[mean_of_samp_3 , mean_of_samp_3],y=[0,0.2],mode = "lines", name = "Mean of 3rd Intervention"))
fig.add_trace(go.Scatter(x=[stdev_2nd_end , stdev_2nd_end],y=[0,0.2],mode = "lines", name = "Standard Deviation 2nd End"))
fig.add_trace(go.Scatter(x=[sample_mean, sample_mean],y=[0,0.2],mode="lines", name = "Sample Mean"))

fig.show()

z_score1 = (mean_of_samp_1 - sample_mean)/sample_stdev
print(z_score1)
z_score2 = (mean_of_samp_2 - sample_mean)/sample_stdev
print(z_score2)
z_score3 = (mean_of_samp_3 - sample_mean)/sample_stdev
print(z_score3)