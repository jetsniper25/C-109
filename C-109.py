import pandas as pd
import csv
import statistics

df=pd.read_csv("data.csv")
heightList=df["Height"].to_list()
weightList=df["Weight"].to_list()

hmean=statistics.mean(heightList)
wmean=statistics.mean(weightList)

hmedian=statistics.median(heightList)
wmedian=statistics.median(weightList)

hmode=statistics.mode(heightList)
wmode=statistics.mode(weightList)

hstdev=statistics.stdev(heightList)
wstdev=statistics.stdev(weightList)

print("Mean {},Median {}, Mode {}, Stdev {} for height".format(hmean,hmedian, hmode, hstdev))
print("Mean {},Median {}, Mode {}, Stdev {} for weight".format(wmean,wmedian, wmode, wstdev))

#height first standard deviation start, end
hfss, hfse=hmean-hstdev,hmean+hstdev
hsss, hsse=hmean-2*hstdev, hmean+2*hstdev

wfss, wfse=wmean-wstdev,wmean+wstdev
wsss, wsse=wmean-2*wstdev, wmean+2*wstdev

htss, htse=hmean-3*hstdev,hmean+3*hstdev
print("Firt range is {} between {}".format(hfss, hfse))
print("Second range is {} between {}".format(hsss, hsse))
print("Third range is {} between {}".format(htss, htse))

wtss, wtse=wmean-3*wstdev,wmean+3*wstdev
print("Firt range is {} between {}".format(wfss, wfse))
print("Second range is {} between {}".format(wsss, wsse))
print("Third range is {} between {}".format(wtss, wtse))

height_list_of_data_within_firststdev=[result for result in heightList if result>hfss and result<hfse]
height_list_of_data_within_secondstdev=[result for result in heightList if result>hsss and result<hsse]
height_list_of_data_within_thirdstdev=[result for result in heightList if result>htss and result<htse]
print("{}% of data for height lies within First range".format(len(height_list_of_data_within_firststdev)*100.0/len(heightList)))
print("{}% of data for height lies within Second range".format(len(height_list_of_data_within_secondstdev)*100.0/len(heightList)))
print("{}% of data for height lies within Third range".format(len(height_list_of_data_within_thirdstdev)*100.0/len(heightList)))

weight_list_of_data_within_firststdev=[result for result in weightList if result>wfss and result<wfse]
weight_list_of_data_within_secondstdev=[result for result in weightList if result>wsss and result<wsse]
weight_list_of_data_within_thirdstdev=[result for result in weightList if result>wtss and result<wtse]
print("{}% of data for weight lies within First range".format(len(weight_list_of_data_within_firststdev)*100.0/len(weightList)))
print("{}% of data for weight lies within Second range".format(len(weight_list_of_data_within_secondstdev)*100.0/len(weightList)))
print("{}% of data for weight lies within Third range".format(len(weight_list_of_data_within_thirdstdev)*100.0/len(weightList)))