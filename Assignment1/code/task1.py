# TASK 1 
from collections import defaultdict
import csv
# =============================================================================================================================

# READING DATA FROM VAERSVAX TO EXTRACT VAERSID THAT IS ONLY RELATED WITH COVID
def vaersIDHashmapCovid(filepath):
    # CREATING A HASMAP
    vaersHashmap = defaultdict(list)
    # ENCODING ISO-8859-1
    r = open(filepath, "r", encoding="ISO-8859-1")
    reader = csv.reader(r)
    i=0
    # TO STORE THE HEADING
    headinglist = []
    for x in reader:
        # each row will be in the form of an array
        # for the first iteration i will get the heading row. Storing heading row in headling list array
        if i==0:
            # excluding the first element
            headinglist=x[1:]
            i+=1
        singlelinearray = x
        # checking if my singlelinearray has COVID19 in its second position or not
        if singlelinearray[1]=="COVID19" or singlelinearray[1]=="COVID19-2":
            # if True i will store the entire row from [1:], i am excluding vaers id 
            vaersHashmap[int(singlelinearray[0])].append(singlelinearray[1:])
    # returnning [hasmap and heading list]
    return [vaersHashmap, headinglist]

#
vaersVaxCOVIDID2020Both =vaersIDHashmapCovid("../dataset/2020Vaers/2020VAERSVAX.csv")
vaersVaxCOVIDID2020 = vaersVaxCOVIDID2020Both[0]
vaersVaxHeading = vaersVaxCOVIDID2020Both[1]
vaersVaxCOVIDID2021 =vaersIDHashmapCovid("../dataset/2021Vaers/2021VAERSVAX.csv")[0]
vaersVaxCOVIDID2022 =vaersIDHashmapCovid("../dataset/2022Vaers/2022VAERSVAX.csv")[0]
vaersVaxCOVIDID2023 =vaersIDHashmapCovid("../dataset/2023Vaers/2023VAERSVAX.csv")[0]
vaersVaxNonDomestics =vaersIDHashmapCovid("../dataset/NonDomestics/NONDomesticVAERSVAX.csv")[0]
print(len(vaersVaxCOVIDID2020)+len(vaersVaxCOVIDID2021)+len(vaersVaxCOVIDID2022)+len(vaersVaxCOVIDID2023)+len(vaersVaxNonDomestics))
# ================================================================================================================================
# def vaersSymptomsHashmapCovid(hasmap, filepath):
#     # creating a hasmap
#     vaersSymptomsHasmap = defaultdict(list)
#     r = open(filepath, "r", encoding="ISO-8859-1")
#     reader = csv.reader(r)
#     headinglist = []
#     i=0
#     for x in reader:
#         if i==0:
#             headinglist = x[1:]
#             i+=1
        
#         singlelinearray = x
        
#         if singlelinearray[0] in hasmap:
           
#             vaersSymptomsHasmap[singlelinearray[0]].append(singlelinearray[1:])
#     return [vaersSymptomsHasmap, headinglist]


# vaersSymptomCovid2020Both =vaersSymptomsHashmapCovid(vaersVaxCOVIDID2020,"../dataset/2020Vaers/2020VAERSSYMPTOMS.csv")
# vaersSymptomCovid2020 = vaersSymptomCovid2020Both[0]
# vaersSymptomHeading = vaersSymptomCovid2020Both[1]
# vaersSymptomCovid2021 =vaersSymptomsHashmapCovid(vaersVaxCOVIDID2021,"../dataset/2021Vaers/2021VAERSSYMPTOMS.csv")[0]
# vaersSymptomCovid2022 =vaersSymptomsHashmapCovid(vaersVaxCOVIDID2022,"../dataset/2022Vaers/2022VAERSSYMPTOMS.csv")[0]
# vaersSymptomCovid2023 =vaersSymptomsHashmapCovid(vaersVaxCOVIDID2023,"../dataset/2023Vaers/2023VAERSSYMPTOMS.csv")[0]
# vaersNonDomesticsSymptoms =vaersSymptomsHashmapCovid(vaersVaxNonDomestics,"../dataset/NonDomestics/NonDomesticVAERSSYMPTOMS.csv")[0]
# # Assignment1/dataset/NonDomestics/NonDomesticVAERSSYMPTOMS.csv

# # # # ============================================================================================================================
# def vaersDataHashmapCovid(hasmap, filepath):
#     i = 0
#     vaersDataHasmap = {}
#     r = open(filepath, "r", encoding="ISO-8859-1")
#     reader = csv.reader(r)
#     headinglist = []
    
#     for x in reader:
        
#         if i==0:
#             headinglist =x
#             i+=1
#         singllinearray =x
#         if singllinearray[0] in hasmap:
#             vaersDataHasmap[singllinearray[0]] = singllinearray
#     return [vaersDataHasmap, headinglist]


# vaersDataCovid2020Both =vaersDataHashmapCovid(vaersVaxCOVIDID2020,"../dataset/2020Vaers/2020VAERSDATA.csv")
# vaersDataCovid2020 = vaersDataCovid2020Both[0]
# vaersDataHeading = vaersDataCovid2020Both[1]
# vaersDataCovid2021 =vaersDataHashmapCovid(vaersVaxCOVIDID2021,"../dataset/2021Vaers/2021VAERSDATA.csv")[0]
# vaersDataCovid2022 =vaersDataHashmapCovid(vaersVaxCOVIDID2022,"../dataset/2022Vaers/2022VAERSDATA.csv")[0]
# vaersDataCovid2023 =vaersDataHashmapCovid(vaersVaxCOVIDID2023,"../dataset/2023Vaers/2023VAERSDATA.csv")[0]
# vaersNonDomesticsDataCovid =vaersDataHashmapCovid(vaersVaxNonDomestics,"../dataset/NonDomestics/NonDomesticVAERSDATA.csv")[0]


# # # # ===========================================================================================================================================================================
# # # merging 3 different hasmap into single hasmap
# def singleYearCovidData(hasmapVaersData, hasmapVaersSymptoms, hasmapVaersCovid):
#     vaerSingleYearcovid = {}
#     for x in hasmapVaersData:
#         vaerSingleYearcovid[x]=[hasmapVaersData[x],hasmapVaersSymptoms[x],hasmapVaersCovid[x]]
#     return vaerSingleYearcovid


# covidAllthree2020 = singleYearCovidData(vaersDataCovid2020,vaersSymptomCovid2020,vaersVaxCOVIDID2020 ) 
# covidAllthree2021 = singleYearCovidData(vaersDataCovid2021,vaersSymptomCovid2021,vaersVaxCOVIDID2021 ) 
# covidAllthree2022 = singleYearCovidData(vaersDataCovid2022,vaersSymptomCovid2022,vaersVaxCOVIDID2022 ) 
# covidAllthree2023 = singleYearCovidData(vaersDataCovid2023,vaersSymptomCovid2023,vaersVaxCOVIDID2023 ) 
# covidAllthreeNonDomestics = singleYearCovidData(vaersNonDomesticsDataCovid,vaersNonDomesticsSymptoms,vaersVaxNonDomestics)

# # # merging 4 hasmap into single hasmap
# covidAllthree2020.update(covidAllthree2021)
# covidAllthree2020.update(covidAllthree2022)
# covidAllthree2020.update(covidAllthree2023)
# covidAllthree2020.update(covidAllthreeNonDomestics)
# allthreeYearsCovid = covidAllthree2020

# # # # =============================================================================================================================
# # # # vaersID 1106890 = does not have any symptoms

# # # # using allthreeYearsCovid to create a new csv file

# outputfilename = "VAERS_COVID_DataAugust2023.csv"
# r = open(outputfilename,"w")
# writer = csv.writer(r)
# heading = vaersDataHeading+vaersVaxHeading+vaersSymptomHeading

# writer.writerow(heading)
# for x in allthreeYearsCovid:
   
#      # mergingintosingleline
#      currentVaersId = x
#      currentVaersData = allthreeYearsCovid[currentVaersId]
#      vaersData = currentVaersData[0]
#      vaersSympt = currentVaersData[1]
#      vaersType = currentVaersData[2]
#      newvaersSympt=[]
#      if len(vaersSympt)==0:
#         #  vaersID 1106890 = does not have any symptoms
#          newvaersSympt=["-","-","-","-","-","-","-","-","-","-","-"]
#      else:
       
#          for y in range(len(vaersSympt[0])):
#              combinetxt=""
#              for x in range(len(vaersSympt)):
#                  combinetxt += vaersSympt[x][y]+" "
#              newvaersSympt.append(combinetxt)
#      vaersSympt=newvaersSympt


#      newvaersType=[]
   
#      for c in range(len(vaersType[0])):
#          combinetxt=""
#          for d in range(len(vaersType)):
#              combinetxt+=vaersType[d][c]+" "
#          newvaersType.append(combinetxt)
#      vaersType = newvaersType
#      row = vaersData+vaersType+vaersSympt
#      writer.writerow(row)

# # # # # //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# # # # # TASK2
# # # # # VAERS_ID, AGE_YRS, SEX, VAX_NAME, RPT_Date, SYMPTOM, DIED, DATEDIED,
# headinglist2  = ["VAERS_ID","AGE_YRS","SEX","VAX_NAME","RPT_Date","SYMPTOM","DIED","DATEDIED","SYMPTOMS TEXT"]

# # # # vaersid = [0]
# # # # ageyears= [3]
# # # # sex     = [6]
# # # # vaxname = [6]
# # # # rptdate = [7]
# # # # can have upto 5 symptoms = [0,2,4,6,8]
# # # # died    = [9]
# # # # datedied= [10]
# # # # symptomtext = [8]

# outputfilename2 = "SYMPTOMDATA.csv"
# r2 = open(outputfilename2,"w")
# writer = csv.writer(r2)
# writer.writerow(headinglist2)

# def task2datasetYearly(vaersData, vaersSymptoms, vaersVax):
#     for x in vaersSymptoms:
#         for y in vaersSymptoms[x]:
#             i=0
#             for z in y:
#                 if i>len(y)-1:
#                     break
#                 if len(y[i])==0:
#                     break

#                 if len(y[i])>1:
#                     vaersId = vaersData[x][0]
#                     ageyrs = vaersData[x][3]
#                     sex = vaersData[x][6]
#                     vaxname = vaersVax[x][0][6]
#                     rptdate = vaersData[x][7]
#                     symptom = y[i]
#                     died = vaersData[x][9]
#                     datedied = vaersData[x][10]
#                     symptomstext= vaersData[x][8]
#                     row=[vaersId, ageyrs, sex, vaxname, rptdate, symptom, died, datedied,symptomstext]
#                     writer.writerow(row)

#                 i+=2

      
# a = task2datasetYearly(vaersDataCovid2020, vaersSymptomCovid2020, vaersVaxCOVIDID2020)
# b = task2datasetYearly(vaersDataCovid2021, vaersSymptomCovid2021, vaersVaxCOVIDID2021)
# c = task2datasetYearly(vaersDataCovid2022, vaersSymptomCovid2022, vaersVaxCOVIDID2022)
# d = task2datasetYearly(vaersDataCovid2023, vaersSymptomCovid2023, vaersVaxCOVIDID2023)
# e = task2datasetYearly(vaersNonDomesticsDataCovid,vaersNonDomesticsSymptoms,vaersVaxNonDomestics)



# # # # 1145662