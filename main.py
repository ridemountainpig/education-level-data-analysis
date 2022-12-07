import pandas as pd
import math

# taichung data process
# taichungData = pd.read_csv("./data/臺中市失業率.csv")
# taichungData = taichungData.drop([0, 1, 2, 3, 9]) 
# taichungData = taichungData.reset_index()
# taichungData = taichungData.drop(["index", "總計男_%", "總計女_%"], axis=1)
# taichungData["失業率-大專及以上[%]"] = (taichungData["專科男_%"] + taichungData["專科女_%"] + taichungData["大學男_%"] + taichungData["大學女_%"] + taichungData["研究所男_%"] + taichungData["研究所女_%"]) / 6
# taichungData["失業率-大專及以上[%]"] = taichungData["失業率-大專及以上[%]"].round(1)
# taichungData = taichungData.drop(["專科男_%", "專科女_%", "大學男_%", "大學女_%", "研究所男_%", "研究所女_%"], axis=1)
# taichungData["失業率-高中職[%]"] = (taichungData["高中(職)男_%"] + taichungData["高中(職)女_%"]) / 2
# taichungData["失業率-高中職[%]"] = taichungData["失業率-高中職[%]"].round(1)
# taichungData = taichungData.drop(["高中(職)男_%", "高中(職)女_%"], axis=1)
# taichungData["失業率-國中及以下[%]"] = (taichungData["國中男_%"] + taichungData["國中女_%"] + taichungData["國小及以下男_%"] + taichungData["國小及以下女_%"]) / 4
# taichungData["失業率-國中及以下[%]"] = taichungData["失業率-國中及以下[%]"].round(1)
# taichungData = taichungData.drop(["國中男_%", "國中女_%", "國小及以下男_%", "國小及以下女_%"], axis=1)

# for i in range(0, len(taichungData["年別"])):
#     taichungData["年別"][i] = taichungData["年別"][i][0:3]

# taichungData.columns = ['年度', '失業率-大專及以上[%]', '失業率-高中職[%]', '失業率-國中及以下[%]']
# taichungData.to_csv("./data/afterProcess/臺中市失業率.csv", index=False)


# kaohsiung data process
# kaohsiungData = pd.read_csv("./data/高雄市失業率.csv")

# kaohsiungData = kaohsiungData.drop(kaohsiungData.iloc[:, 1:3], axis=1)
# kaohsiungData = kaohsiungData.drop(kaohsiungData.iloc[:, 7:28], axis=1)
# kaohsiungData = kaohsiungData.drop([0, 1])
# kaohsiungData = kaohsiungData.reset_index()
# kaohsiungData = kaohsiungData.drop(["index"], axis=1)

# for i in range(0, len(kaohsiungData["年別"])):
#     kaohsiungData["年別"][i] = int(kaohsiungData["年別"][i][0:4]) - 1911

# kaohsiungData['失業率-大專及以上[%]'] = (kaohsiungData['女性失業率按教育程度別分大專及以上'] + kaohsiungData['男性失業率按教育程度別分大專及以上']) / 2
# kaohsiungData = kaohsiungData.drop(["女性失業率按教育程度別分大專及以上", "男性失業率按教育程度別分大專及以上"], axis=1)
# kaohsiungData["失業率-大專及以上[%]"] = kaohsiungData["失業率-大專及以上[%]"].round(1)

# kaohsiungData['失業率-高中職[%]'] = (kaohsiungData['女性失業率按教育程度別分高中職'] + kaohsiungData['男性失業率按教育程度別分高中職']) / 2
# kaohsiungData = kaohsiungData.drop(["女性失業率按教育程度別分高中職", "男性失業率按教育程度別分高中職"], axis=1)
# kaohsiungData["失業率-高中職[%]"] = kaohsiungData["失業率-高中職[%]"].round(1)

# kaohsiungData['失業率-國中及以下[%]'] = (kaohsiungData['女性失業率按教育程度別分國中及以下'] + kaohsiungData['男性失業率按教育程度別分國中及以下']) / 2
# kaohsiungData = kaohsiungData.drop(["女性失業率按教育程度別分國中及以下", "男性失業率按教育程度別分國中及以下"], axis=1)
# kaohsiungData["失業率-國中及以下[%]"] = kaohsiungData["失業率-國中及以下[%]"].round(1)

# kaohsiungData.columns = ['年度', '失業率-大專及以上[%]', '失業率-高中職[%]', '失業率-國中及以下[%]']

# kaohsiungData.to_csv("./data/afterProcess/高雄市失業率.csv", index=False)

# newTaipei data process
# newTaipeiData = pd.read_csv("./data/新北市失業率.csv")
# year = 2006
# for i in range(0, len(newTaipeiData["Field1"])):
#     newTaipeiData["Field1"][i] = str(year)
#     year += 1
#     newTaipeiData["Field1"][i] = int(newTaipeiData["Field1"][i]) - 1911

# for i in range(4, 20):
#     for j in range(0, len(newTaipeiData[f"Field{i}"])):
#         if newTaipeiData[f"Field{i}"][j] == "-":
#             newTaipeiData[f"Field{i}"][j] = 0
#         newTaipeiData[f"Field{i}"][j] = float(newTaipeiData[f"Field{i}"][j])

# newTaipeiData = newTaipeiData.drop([0, 1, 2, 3, 4, 5, 6, 7, 8, 14])
# newTaipeiData['失業率-大專及以上[%]'] = (newTaipeiData['Field14'] + newTaipeiData['Field15'] + newTaipeiData['Field16'] + newTaipeiData['Field17'] + newTaipeiData['Field18'] + newTaipeiData['Field19']) / 6
# newTaipeiData['失業率-大專及以上[%]'] = newTaipeiData['失業率-大專及以上[%]'].astype('float').round(1)
# newTaipeiData['失業率-高中職[%]'] = (newTaipeiData['Field8'] + newTaipeiData['Field9'] + newTaipeiData['Field10'] + newTaipeiData['Field11'] + newTaipeiData['Field12'] + newTaipeiData['Field13']) / 6
# newTaipeiData['失業率-高中職[%]'] = newTaipeiData['失業率-高中職[%]'].astype('float').round(1)
# newTaipeiData['失業率-國中及以下[%]'] = (newTaipeiData['Field4'] + newTaipeiData['Field5'] + newTaipeiData['Field6'] + newTaipeiData['Field7']) / 4
# newTaipeiData['失業率-國中及以下[%]'] = newTaipeiData['失業率-國中及以下[%]'].round(1)

# columnList = ["Field" + str(i) for i in range(2, 20)]
# newTaipeiData = newTaipeiData.drop(columnList, axis=1)

# newTaipeiData.columns = ['年度', '失業率-大專及以上[%]', '失業率-高中職[%]', '失業率-國中及以下[%]']

# newTaipeiData.to_csv("./data/afterProcess/新北市失業率.csv", index=False)

# taipei data process
# taipeiData = pd.read_csv("./data/臺北市失業率.csv", encoding="Big5")

# rowList = [i for i in range(111, 126, 3)]
# taipeiData = taipeiData.iloc[rowList]
# taipeiData = taipeiData.reset_index()
# taipeiData = taipeiData.drop(taipeiData.columns[[i for i in range(2, 12)]], axis=1)
# taipeiData = taipeiData.drop(["index"], axis=1)

# for i in range(1, 8):
#     for j in range(0, len(taipeiData[taipeiData.columns[[i]]])):
#         if taipeiData[taipeiData.columns[[i]][0]][j] == "-":
#             taipeiData[taipeiData.columns[[i]][0]][j] = 0
#         taipeiData[taipeiData.columns[[i]][0]][j] = float(taipeiData[taipeiData.columns[[i]][0]][j])

# taipeiData["失業率-大專及以上[%]"] = (taipeiData["失業率/研究所[%]"] + taipeiData["失業率/大學[%]"] + taipeiData["失業率/專科[%]"]) / 3
# taipeiData["失業率-大專及以上[%]"] = taipeiData["失業率-大專及以上[%]"].astype('float').round(1)
# taipeiData["失業率-高中職[%]"] = (taipeiData["失業率/高中[%]"] + taipeiData["失業率/高職[%]"]) / 2
# taipeiData["失業率-高中職[%]"] = taipeiData["失業率-高中職[%]"].astype('float').round(1)
# taipeiData["失業率-國中及以下[%]"] = (taipeiData["失業率/國中[初職][%]"] + taipeiData["失業率/國小以下[%]"]) / 2
# taipeiData["失業率-國中及以下[%]"] = taipeiData["失業率-國中及以下[%]"].astype('float').round(1)

# taipeiData = taipeiData.drop(["失業率/研究所[%]", "失業率/大學[%]", "失業率/專科[%]", "失業率/高中[%]", "失業率/高職[%]", "失業率/國中[初職][%]", "失業率/國小以下[%]"], axis=1)
# for i in range(0, len(taipeiData["年平均別"])):
#     taipeiData["年平均別"][i] = taipeiData["年平均別"][i][0:3]

# taipeiData.columns = ['年度', '失業率-大專及以上[%]', '失業率-高中職[%]', '失業率-國中及以下[%]']

# taipeiData.to_csv("./data/afterProcess/臺北市失業率.csv", index=False)

# # taoyuan data process
# taoyuanData = pd.read_csv("./data/桃園市失業率.csv")
# taoyuanData = taoyuanData.iloc[[i for i in range(22, 27)]]
# taoyuanData = taoyuanData.reset_index()
# taoyuanData = taoyuanData.drop(["index"], axis=1)
# taoyuanData["失業率-大專及以上[%]"] = (taoyuanData["大專及以上－男性"] + taoyuanData["大專及以上－女性"]) / 2
# taoyuanData["失業率-大專及以上[%]"] = taoyuanData["失業率-大專及以上[%]"].astype('float').round(1)
# taoyuanData["失業率-高中職[%]"] = (taoyuanData["高中高職－男性"] + taoyuanData["高中高職－女性"]) / 2
# taoyuanData["失業率-高中職[%]"] = taoyuanData["失業率-高中職[%]"].astype('float').round(1)
# taoyuanData["失業率-國中及以下[%]"] = (taoyuanData["國中及以下－男性"] + taoyuanData["國中及以下－女性"]) / 2
# taoyuanData["失業率-國中及以下[%]"] = taoyuanData["失業率-國中及以下[%]"].astype('float').round(1)
# taoyuanData = taoyuanData.drop(["全體－男性","全體－女性" , "大專及以上－男性", "大專及以上－女性", "高中高職－男性", "高中高職－女性", "國中及以下－男性", "國中及以下－女性"], axis=1)
# taoyuanData.columns = ['年度', '失業率-大專及以上[%]', '失業率-高中職[%]', '失業率-國中及以下[%]']

# taoyuanData.to_csv("./data/afterProcess/桃園市失業率.csv", index=False)

# tainan data process
# tainanData = pd.read_csv("./data/臺南市失業率.csv")
# for i in range(0, len(tainanData["年度"])):
#     tainanData["年度"][i] = tainanData["年度"][i] - 1911
# tainanData = tainanData.drop([5, 6])
# tainanData = tainanData.drop(["失業率[%]"], axis=1)

# tainanData.to_csv("./data/afterProcess/臺南市失業率.csv", index=False)

# # credit card data process
# creditCardData = pd.read_csv("./data/教育程度信用卡消費.csv")
# for i in range(0, len(creditCardData["年月"])):
#     creditCardData["年月"][i] = int(str(creditCardData["年月"][i])[0:4]) - 1911

# areaList = [63000000, 64000000, 65000000, 66000000, 67000000, 68000000]
# creditCardData = creditCardData.drop(creditCardData[creditCardData["年月"] > 108].index)
# creditCardData = creditCardData.drop(creditCardData[creditCardData["年月"] < 104].index)

# creditCardData = creditCardData[creditCardData["地區"].isin(areaList)]
# creditCardData = creditCardData.reset_index()
# creditCardData = creditCardData.drop(["index"], axis=1)
# creditCardData["地區"][creditCardData[creditCardData["地區"] == 63000000].index] = "臺北市"
# creditCardData["地區"][creditCardData[creditCardData["地區"] == 64000000].index] = "高雄市"
# creditCardData["地區"][creditCardData[creditCardData["地區"] == 65000000].index] = "新北市"
# creditCardData["地區"][creditCardData[creditCardData["地區"] == 66000000].index] = "臺中市"
# creditCardData["地區"][creditCardData[creditCardData["地區"] == 67000000].index] = "臺南市"
# creditCardData["地區"][creditCardData[creditCardData["地區"] == 68000000].index] = "桃園市"
# creditCardData = creditCardData.drop(["信用卡交易筆數", "產業別"], axis=1)
# creditCardData = creditCardData.groupby(["年月", "地區", "教育程度類別"]).agg({"年月": "first", "地區": "first", "教育程度類別": "first", "信用卡交易金額[新台幣]": "sum"})
# creditCardData = creditCardData.drop(creditCardData[creditCardData["教育程度類別"] == "其他"].index)

# print(creditCardData)

# creditCardData.to_csv("./data/afterProcess/教育程度信用卡消費.csv", index=False)

newTaipeiData = pd.read_csv("./data/afterProcess/新北市失業率.csv")
newTaipeiData['地區'] = ['新北市' for i in range(0, len(newTaipeiData['年度']))]
taipeiData = pd.read_csv("./data/afterProcess/臺北市失業率.csv")
taipeiData['地區'] = ['臺北市' for i in range(0, len(taipeiData['年度']))]
taichungData = pd.read_csv("./data/afterProcess/臺中市失業率.csv")
taichungData['地區'] = ['臺中市' for i in range(0, len(taichungData['年度']))]
kaohsiungData = pd.read_csv("./data/afterProcess/高雄市失業率.csv")
kaohsiungData['地區'] = ['高雄市' for i in range(0, len(kaohsiungData['年度']))]
taoyuanData = pd.read_csv("./data/afterProcess/桃園市失業率.csv")
taoyuanData['地區'] = ['桃園市' for i in range(0, len(taoyuanData['年度']))]
tainanData = pd.read_csv("./data/afterProcess/臺南市失業率.csv")
tainanData['地區'] = ['臺南市' for i in range(0, len(tainanData['年度']))]

creditCardData = pd.read_csv("./data/afterProcess/教育程度信用卡消費.csv")

AllCityData = pd.concat([newTaipeiData, taipeiData, taichungData, kaohsiungData, taoyuanData, tainanData])
AllCityData = AllCityData.iloc[:,[0, 4, 1, 2, 3]]
AllCityData = AllCityData.reset_index()
AllCityData = AllCityData.drop(["index"], axis=1)
phd = pd.concat([creditCardData[creditCardData["教育程度類別"] == "博士"], creditCardData[creditCardData["教育程度類別"] == "碩士"], creditCardData[creditCardData["教育程度類別"] == "大學"], creditCardData[creditCardData["教育程度類別"] == "專科"]])
phd = phd.drop(["教育程度類別"], axis=1)
# AllCityData["信用卡交易金額[新台幣]-大專及以上"] = phd["信用卡交易金額[新台幣]"]

print(AllCityData)
print(phd)
