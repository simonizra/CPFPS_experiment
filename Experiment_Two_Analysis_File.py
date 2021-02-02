# Simon Leonid Izraelit # Experiment 2 Analysis File #

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from scipy import stats


# What is the mean accuracy of each set die face? #

special_data_frame = pd.read_csv('hyp_esp_data_6.csv')

print(special_data_frame.head(50))

data_frame_one_set_die_face = special_data_frame[special_data_frame['die_face']==1]
data_frame_two_set_die_face = special_data_frame[special_data_frame['die_face']==2]
data_frame_three_set_die_face = special_data_frame[special_data_frame['die_face']==3]
data_frame_four_set_die_face = special_data_frame[special_data_frame['die_face']==4]
data_frame_five_set_die_face = special_data_frame[special_data_frame['die_face']==5]
data_frame_six_set_die_face = special_data_frame[special_data_frame['die_face']==6]


mean_accuracy_for_one_set_die_face = np.mean(data_frame_one_set_die_face[['exp_key_resp1.corr']])
mean_accuracy_for_two_set_die_face = np.mean(data_frame_two_set_die_face[['exp_key_resp1.corr']])
mean_accuracy_for_three_set_die_face = np.mean(data_frame_three_set_die_face[['exp_key_resp1.corr']])
mean_accuracy_for_four_set_die_face = np.mean(data_frame_four_set_die_face[['exp_key_resp1.corr']])
mean_accuracy_for_five_set_die_face = np.mean(data_frame_five_set_die_face[['exp_key_resp1.corr']])
mean_accuracy_for_six_set_die_face = np.mean(data_frame_six_set_die_face[['exp_key_resp1.corr']])

print('the mean accuracy of the one face of the die is' + str(mean_accuracy_for_one_set_die_face))
print('the mean accuracy of the two face of the die is' + str(mean_accuracy_for_two_set_die_face))
print('the mean accuracy of the three face of the die is' + str(mean_accuracy_for_three_set_die_face))
print('the mean accuracy of the four face of the die is' + str(mean_accuracy_for_four_set_die_face))
print('the mean accuracy of the five face of the die is' + str(mean_accuracy_for_five_set_die_face))
print('the mean accuracy of the six face of the die is' + str(mean_accuracy_for_six_set_die_face))



# Preparing for the eventual graph #
set_sizes = [1,2,3,4,5,6]

one_list = list(mean_accuracy_for_one_set_die_face)
two_list = list(mean_accuracy_for_two_set_die_face)
three_list = list(mean_accuracy_for_three_set_die_face)
four_list = list(mean_accuracy_for_four_set_die_face)
five_list = list(mean_accuracy_for_five_set_die_face)
six_list = list(mean_accuracy_for_six_set_die_face)


extremely_important_list = one_list + two_list + three_list + four_list + five_list + six_list

fig = plt.figure(figsize = (10, 5)) 

plt.bar(set_sizes,extremely_important_list, color ='maroon',width = 0.7) 

plt.xlabel('Die faces 1 - 6') 
plt.ylabel('Mean accuracy') 


plt.axis([0,7,0,1])
plt.title('ESP -- will the participant correctly guess what side die will come up?')
plt.legend(loc = 'upper left')
plt.show()


# Loops to append the values to the lists ! #
list_obvs = []
list_exp = []

for value in special_data_frame['resp']:
    list_obvs.append(value)
    
for value in special_data_frame['die_face']:
    list_exp.append(value)

print(stats.chisquare(f_obs = list_obvs , f_exp= list_exp))


# CHI SQUARED RESULTS : Power_divergenceResult(statistic=505.1166666666667, pvalue=0.9895934096301547) #


# There is no proof whatsoever of ESP in these results. There is no significance. 
# I cannot conceive of a way to change the experiment to effectively detect
# ESP in participants. It's a tad too sensational, no? 


