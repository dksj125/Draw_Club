import random
import pandas as pd

# 각 작업실의 최대 정원을 입력 받습니다.
Team_X_Max = int(input("이번 팀엑스 정원은 몇명입니까?: "))
#Small_Space_Max = int(input("이번 작공 정원은 몇명입니까?: "))
#Space_Place_Max = int(input("이번 공장 정원은 몇명입니까?: "))
#Mu_Max = int(input("이번 뮤 정원은 몇명입니까?: "))
#Sof_Max = int(input("이번 소프 정원은 몇명입니까?: "))
#Arch = int(input("이번 아키 정원은 몇명입니까?: "))

# 각 작업실별 딕션너리를 선언
Team_X = {}
Small_Space = {}
Space_Place = {}
Mu = {}
Sof = {}
Arch = {}
Nothing = {}


# 각 작업실별에 특정 키값을 선언해 딕셔너리를 선언
Club = {0 : "Team_X", 1 : "Small_Space" , 2 : "Space_Place", 3 : "Mu", 4 : "Sof", 5 : "Arch", 6 : "Nothing"}


# 신입생들이 지원한 작업실데이터를 불러옴
New_Students = pd.read_excel('D:/Coding/Python/Recommend_date/New_Student.xlsx')


# 판다스 데이터 프레임을 리스트로 변환
New_Students_List = New_Students.values.tolist()


#1지망을 각 작업실 딕셔너리에 저장 키는 학번, 이름은 밸류
for i in New_Students_List:

    #1지망이 팀엑스인 사람들을 팀엑스 딕셔너리에
    if i[2] == Club[0]:
        Team_X[i[1]] = i[0]
    
    #1지망이 작공인 사람들을 작공 딕셔너리에 저장
    elif i[2] == Club[1]:
       Small_Space[i[1]] = i[0]
    
    #1지망이 공장인 사람들을 공장 딕셔너리에 저장
    elif i[2] == Club[2]:
        Space_Place[i[1]] = i[0]

    #1지망이 뮤인 사람들을 뮤 딕셔너리에 저장
    elif i[2] == Club[3]:
        Mu[i[1]] = i[0]
        
    #1지망이 소프인 사람들을 소프 딕셔너리에 저장
    elif i[2] == Club[4]:
        Sof[i[1]] = i[0]

    #1지망이 아키인 사람들을 아키 딕셔너리에 저장
    elif i[2] == Club[5]:
        Arch[i[1]] = i[0]

    #1지망이 비작인 사람들을 비작 딕셔너리에 저장
    elif i[2] == Club[6]:
        Nothing[i[1]] = i[0]


# 각 작업실별로 정원에 알맞게 들어 갔는지 확인 그렇지 않다면 무작위로 추출하여 학번으로 리스트를 만듬

# 팀엑스 인원 초과시 작동
if Team_X_Max < len(Team_X):
    Team_X_Key_List = list(Team_X.keys())       #팀엑스 딕셔너리에서 키값만 리스트로 Team_X_Key_List에 저장
    Team_X_Pop_List = random.sample(Team_X_Key_List, len(Team_X) -Team_X_Max)   # 무작위로 골라내어 제거될 학번만 Team_X_Pop_List에 리스트로 저장

# 작공 인원 초과시 작동
if Small_Space_Max < len(Small_Space):
    Small_Space_Key_List = list(Small_Space.keys())
    Small_Space_Pop_List = random.sample(Small_Space_Key_List, len(Small_Space) - Small_Space_Max)

# 공장 인원 초과시 작동
if Space_Place_Max < len(Space_Place):
    Space_Place_Key_List = list(Space_Place.keys())
    Space_Place_Pop_List = random.sample(Space_Place_Key_List, len(Space_Place) - Space_Place_Max)

# 뮤 인원 초과시 작동
if Mu_Max < len(Mu):
    Mu_Key_List = list(Mu.keys())
    Mu_Pop_List = random.sample(Mu_Key_List, len(Mu) - Mu_Max)

# 소프 인원 초과시 작동
if Sof_Max < len(Sof):
    Sof_Key_List = list(Sof.keys())
    Sof_Pop_List = random.sample(Sof_Key_List, len(Sof) - Sof_Max)

# 아키 인원 초과시 작동
if Arch_Max < len(Arch):
    Arch_Key_List = list(Arch.keys())
    Arch_Pop_List = random.sample(Arch_Key_List, len(Arch) - Arch_Max)


#키값(학번)을 비교하여 딕셔너리 내에서 삭제

#팀엑스 딕셔너리
for i in Team_X_Pop_List:
    if i in Team_X:
        del Team_X[i]

#작공 딕셔너리
for i in Small_Space_Pop_List:
    if i in Small_Space:
       del Small_Space[i]

#공장 딕셔너리
for i in Space_Place_Pop_List:
    if i in Space_Place:
       del Space_Place[i]

#뮤 딕셔너리
for i in Mu_Pop_List:
    if i in Mu:
       del Mu[i]

#소프 딕셔너리
for i in Sof_Pop_List:
    if i in Sof:
       del Sof[i]

#아키 딕셔너리
for i in Arch_Pop_List:
    if i in Arch:
       del Arch[i]