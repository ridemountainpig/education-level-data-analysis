import pandas as pd
import math

# taichung data process
# taichungData = pd.read_csv("./data/臺中市失業率.csv")
# taichungData = taichungData.drop([0, 1, 2, 3])
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
# print(kaohsiungData)
# kaohsiungData.to_csv("./data/afterProcess/高雄市失業率.csv", index=False)

# newTaipei data process
newTaipeiData = pd.read_csv("./data/新北市失業率.csv")

year = 2006
for i in range(0, len(newTaipeiData["Field1"])):
    newTaipeiData["Field1"][i] = str(year)
    year += 1
    newTaipeiData["Field1"][i] = int(newTaipeiData["Field1"][i]) - 1911

for i in range(4, 20):
    for j in range(0, len(newTaipeiData[f"Field{i}"])):
        if newTaipeiData[f"Field{i}"][j] == "-":
            newTaipeiData[f"Field{i}"][j] = 0
        newTaipeiData[f"Field{i}"][j] = float(newTaipeiData[f"Field{i}"][j])

newTaipeiData = newTaipeiData.drop([0, 1, 2, 3, 4, 5, 6, 7, 8])
newTaipeiData['失業率-大專及以上[%]'] = (newTaipeiData['Field14'] + newTaipeiData['Field15'] + newTaipeiData['Field16'] + newTaipeiData['Field17'] + newTaipeiData['Field18'] + newTaipeiData['Field19']) / 6
newTaipeiData['失業率-大專及以上[%]'] = newTaipeiData['失業率-大專及以上[%]'].astype('float').round(1)
newTaipeiData['失業率-高中職[%]'] = (newTaipeiData['Field8'] + newTaipeiData['Field9'] + newTaipeiData['Field10'] + newTaipeiData['Field11'] + newTaipeiData['Field12'] + newTaipeiData['Field13']) / 6
newTaipeiData['失業率-高中職[%]'] = newTaipeiData['失業率-高中職[%]'].astype('float').round(1)
newTaipeiData['失業率-國中及以下[%]'] = (newTaipeiData['Field4'] + newTaipeiData['Field5'] + newTaipeiData['Field6'] + newTaipeiData['Field7']) / 4
newTaipeiData['失業率-國中及以下[%]'] = newTaipeiData['失業率-國中及以下[%]'].round(1)

columnList = ["Field" + str(i) for i in range(2, 20)]
newTaipeiData = newTaipeiData.drop(columnList, axis=1)

newTaipeiData.columns = ['年度', '失業率-大專及以上[%]', '失業率-高中職[%]', '失業率-國中及以下[%]']
newTaipeiData.to_csv("./data/afterProcess/新北市失業率.csv", index=False)

print(newTaipeiData)

# tainan data process
# tainanData = pd.read_csv("./data/臺南市失業率.csv")
# for i in range(0, len(tainanData["年度"])):
#     tainanData["年度"][i] = tainanData["年度"][i] - 1911
# tainanData = tainanData.drop(6)
# tainanData = tainanData.drop(["失業率[%]"], axis=1)

# tainanData.to_csv("./data/afterProcess/臺南市失業率.csv", index=False)


#
