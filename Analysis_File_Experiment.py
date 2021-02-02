# Simon Leonid Izraelit # Experiment Three Analysis File # Computer Programming for the Psychological Sciences #  


import numpy as np
import pandas as pd
from scipy import stats
from matplotlib import pyplot as plt


df = pd.read_csv('hyp_data_exp3.csv')

localized_data_frame = df[['participant','angle_distance','response_time']]
print(localized_data_frame)

# Breaking it all down into smaller data frames, easier to work with!
zero_df_rt = localized_data_frame[localized_data_frame['angle_distance']==0]
thirty_df_rt = localized_data_frame[localized_data_frame['angle_distance']==30]
sixty_df_rt = localized_data_frame[localized_data_frame['angle_distance']==60]
ninety_df_rt = localized_data_frame[localized_data_frame['angle_distance']==90]
one_hundred_twenty_df_rt = localized_data_frame[localized_data_frame['angle_distance']==120]
one_hundred_fifty_df_rt = localized_data_frame[localized_data_frame['angle_distance']==150]
one_hundred_eighty_df_rt = localized_data_frame[localized_data_frame['angle_distance']==180]



zero_rt_mean = np.mean(zero_df_rt[['response_time']])

thirty_rt_mean = np.mean(thirty_df_rt[['response_time']])

sixty_rt_mean = np.mean(sixty_df_rt[['response_time']])

ninety_rt_mean = np.mean(ninety_df_rt[['response_time']])

one_hundred_twenty_rt_mean = np.mean(one_hundred_twenty_df_rt[['response_time']])

one_hundred_fifty_rt_mean = np.mean(one_hundred_fifty_df_rt[['response_time']])

one_hundred_eighty_rt_mean = np.mean(one_hundred_eighty_df_rt[['response_time']])


print('The mean response time for a rotational distance of zero is' + str(zero_rt_mean))
print('The mean response time for a rotational distance of thirty is' +str(thirty_rt_mean))
print('The mean response time for a rotational distance of sixty is' +str(sixty_rt_mean))
print('The mean response time for a rotational distance of ninety is' +str(ninety_rt_mean))
print('The mean response time for a rotational distance of one hundred twenty is' +str(one_hundred_twenty_rt_mean))
print('The mean response time for a rotational distance of one hundred fifty is' +str(one_hundred_fifty_rt_mean))
print('The mean response time for a rotational distance of one hundred eighty is' +str(one_hundred_eighty_rt_mean))


# Simple acquisition of pearson's R in one line of code!# 
print(localized_data_frame['response_time'].corr(localized_data_frame['angle_distance']))

# The pearson's r coefficient between response time and angle difference is #
# 0.8658917641171133 #


# Creating the axes for the eventual graph
angle_differences = [0,30,60,90,120,150,180]

zero_list = list(zero_rt_mean)
thirty_list = list(thirty_rt_mean)
sixty_list = list(sixty_rt_mean)
ninety_list = list(ninety_rt_mean)
one_hundred_twenty_list = list(one_hundred_twenty_rt_mean)
one_hundred_fifty_list = list(one_hundred_fifty_rt_mean)
one_hundred_eighty_list = list(one_hundred_eighty_rt_mean)


fig = plt.figure(figsize = (10, 5)) 

the_ultimate_list = zero_list + thirty_list + sixty_list + ninety_list +one_hundred_twenty_list + one_hundred_fifty_list + one_hundred_eighty_list


plt.title('Mean Response Time versus Rotation Distance!')
plt.grid(True)
plt.xlabel('Rotational Distance (In Degrees °)')
plt.ylabel('Mean Response Times in Milliseconds')
plt.xticks(angle_differences)

plt.plot(angle_differences, the_ultimate_list)

plt.show()


# I believe that rotation distance does have an effect on response time during #
# mental rotation. Using a different stimulus might hinder the process #
# because a letter is more difficult to orient than a more familar image, #
# as in a landscape or a cat. If rotation was only in 3 directions, #
# I would presume that the two rotations that weren't right-side-up would have #
# similar response times, while the right-side-up image would have the shortest #
# response time. #

