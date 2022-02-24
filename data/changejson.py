import json

with open('annotations.json') as f:
    data = json.load(f)

print(len(data["annotations"]))

tem = data["annotations"]

# 요한오빠 수정본에서 쓸 것
#tem=list()


#######################################################
        #category id 가 2인것 지우기 (basejack)
#######################################################

#for i in range(4468):
#    k=4468-i

#    if data["annotations"][k]["category_id"]==2:
#        del tem[k]



#######################################################
        #category id 가 2인것 지우기 (basejack) - 요한오빠 수정 
#######################################################

#for j in range(len(data["annotations"])):
#     print(j)
#     print(data["annotations"][j]["category_id"]==0)

#     if data["annotations"][j]["category_id"]==0:
#         tem.append(j)

#for idx in sorted(tem, reverse = True):
#     del data["annotations"][idx]

#print("List after removing values at index 0, 2 and 5: ", data["annotations"])

######################################################3##
        # 카테고리 아이디 바꾸기
#########################################################

for i in range(len(data["annotations"])):
#    k=30061-i

    if data["annotations"][i]["category_id"]==3:
        data["annotations"][i]["category_id"]=0



with open('annotations.json', 'w', encoding='utf-8') as make_file:
    json.dump(data, make_file, indent='\t')
f.close()
