import random
import pandas as pd

# 각 작업실별 딕션너리를 선언


class Club_Select_Algorithm:
    def run(self, i):
        Team_X = {}
        Small_Space = {}
        Space_Place = {}
        Mu = {}
        Sof = {}
        Arch = {}
        Nothing = {}
        # 작업실 최소 인원
        Min_Member = int(i)
        # 각 작업실별에 특정 키값을 선언해 딕셔너리를 선언

        Club = {0: "팀엑스", 1: "작은공간", 2: "공간과장소",
                3: "뮤", 4: "소프", 5: "아키", 6: "비작업실"}

        Club_Value = list(Club.values())

        

        # 신입생들이 지원한 작업실데이터를 불러옴

        New_Students = pd.read_csv('static/csv/result.csv', encoding='CP949')

        # 판다스 데이터 프레임을 리스트로 변환

        New_Students_List = New_Students.values.tolist()

        # 각 작업실 딕셔너리에 추가 하는 함수들

        def Team_X_Add(i, j):
            Team_X[i] = j

        def Small_Space_Add(i, j):
            Small_Space[i] = j

        def Space_Place_Add(i,j):
            Space_Place[i] = j

        def Mu_Add(i, j):
            Mu[i] = j

        def Sof_Add(i, j):
            Sof[i] = j

        def Arch_Add(i, j):
            Arch[i] = j

        def Nothing_Add(i, j):
            Nothing[i] = j

        #2지망으로 보내기
        def Second(Student_Number, Student_Name ,i):
            #2지망이 팀엑스인 신입생
            if 0 == i:      #2지망과 Club딕셔너리에서 일치하는 요소를 찾기.
                Team_X_Add(Student_Number, Student_Name)

            #2지망이 작공인 신입생
            elif 1 == i:
                print("실행")
                Small_Space_Add(Student_Number, Student_Name)

            #2지망이 공장인 신입생
            elif 2 == i:    
                Space_Place_Add(Student_Number, Student_Name)

            #2지망이 뮤인 신입생
            elif 3 == i:
                Mu_Add(Student_Number, Student_Name)

            #2지망이 소프인 신입생
            elif 4 == i:    
                Sof_Add(Student_Number, Student_Name)

            #2지망이 아키인 신입생
            elif 5 == i:
                Arch_Add(Student_Number, Student_Name)


        #가장 많은 작실에서 기준 미달인 작실로 보내기
        def From_Max_To_Min(Max_idx, Min_idx):

            #팀엑스->기준미달    
            if Max_idx == 0:
                #팀엑스 딕셔너리에서 키값인 학번을 리스트로 만들기
                Team_X_Key_List = list(Team_X.keys())
                Bool = True
                while(Bool):
                    #학번 리스트에서 무작위로 한명 고르기
                    Out_Student = random.sample(Team_X_Key_List, 1)
                    for Student_info in New_Students_List:
                        if Out_Student[0] == Student_info[1]:
                            if Student_info[3] == Club[Min_idx]:
                                Second(Student_info[1], Student_info[0] ,Min_idx)
                                del Team_X[Out_Student[0]]
                            break
                    Bool = False
                            
            #작공->기준미달
            elif Max_idx == 1:
                #Small_Space 딕셔너리에서 키값인 학번을 리스트로 만들기
                Small_Space_Key_List = list(Small_Space.keys())
                Bool = True
                while(Bool):
                    #학번 리스트에서 무작위로 한명 고르기
                    Out_Student = random.sample(Small_Space_Key_List, 1)
                    for Student_info in New_Students_List:
                        if Out_Student[0] == Student_info[1]:
                            if Student_info[3] == Club[Min_idx]:
                                Second(Student_info[1], Student_info[0] ,Min_idx)
                                del Small_Space[Out_Student[0]]
                            break
                    Bool = False

            #공장->기준미달
            elif Max_idx == 2:
                #Space_Place 딕셔너리에서 키값인 학번을 리스트로 만들기    
                Space_Place_Key_List = list(Space_Place.keys())
                Bool = True
                while(Bool):
                    #학번 리스트에서 무작위로 한명 고르기
                    Out_Student = random.sample(Space_Place_Key_List, 1)
                    for Student_info in New_Students_List:
                        if Out_Student[0] == Student_info[1]:
                            if Student_info[3] == Club[Min_idx]:
                                Second(Student_info[1], Student_info[0] ,Min_idx)
                                del Space_Place[Out_Student[0]]
                            break
                    Bool = False
                            
            #뮤->기준미달
            elif Max_idx == 3:
                #Mu 딕셔너리에서 키값인 학번을 리스트로 만들기
                Mu_Key_List = list(Mu.keys())
                Bool = True
                while(Bool):
                    #학번 리스트에서 무작위로 한명 고르기
                    Out_Student = random.sample(Mu_Key_List, 1)
                    for Student_info in New_Students_List:
                        if Out_Student[0] == Student_info[1]:
                            if Student_info[3] == Club[Min_idx]:
                                Second(Student_info[1], Student_info[0] ,Min_idx)
                                del Mu[Out_Student[0]]
                            break
                    Bool = False

            #소프->기준미달
            elif Max_idx == 4:
                #Sof 딕셔너리에서 키값인 학번을 리스트로 만들기
                Sof_Key_List = list(Sof.keys())
                Bool = True
                while(Bool):
                    #학번 리스트에서 무작위로 한명 고르기
                    Out_Student = random.sample(Sof_Key_List, 1)
                    for Student_info in New_Students_List:
                        if Out_Student[0] == Student_info[1]:
                            if Student_info[3] == Club[Min_idx]:
                                Second(Student_info[1], Student_info[0] ,Min_idx)
                                del Sof[Out_Student[0]]
                            break
                    Bool = False


            #아키->기준미달
            elif Max_idx == 5:
                #Arch 딕셔너리에서 키값인 학번을 리스트로 만들기
                Arch_Key_List = list(Arch.keys())
                Bool = True
                while(Bool):
                    #학번 리스트에서 무작위로 한명 고르기
                    Out_Student = random.sample(Arch_Key_List, 1)
                    for Student_info in New_Students_List:
                        if Out_Student[0] == Student_info[1]:
                            if Student_info[3] == Club[Min_idx]:
                                Second(Student_info[1], Student_info[0] ,Min_idx)
                                del Arch[Out_Student[0]]
                            break
                    Bool = False


        def Check_Second(Max_idx, Min_idx):
            #팀엑스내에 2지망이 일치 하는가?    
            if Max_idx == 0:
                #팀엑스 딕셔너리에서 키값인 학번을 리스트로 만들기
                Team_X_Key_List = list(Team_X.keys())
                for idx in Team_X_Key_List:
                    for Student_info in New_Students_List:
                        if idx == Student_info[1]:
                            if Student_info[3] == Club[Min_idx]:
                                return True
                return False

                            
            #작공내에 2지망이 일치 하는가?
            elif Max_idx == 1:
                #작공내에 2지망이 일치 하는가? 
                Small_Space_Key_List = list(Small_Space.keys())
                for idx in Small_Space_Key_List:
                    for Student_info in New_Students_List:
                        if idx == Student_info[1]:
                            if Student_info[3] == Club[Min_idx]:
                                return True
                return False

            #Space_Place내에 2지망이 일치 하는가?
            elif Max_idx == 2:
                #Space_Place내에 2지망이 일치 하는가? 
                Space_Place_Key_List = list(Space_Place.keys())
                for idx in Space_Place_Key_List:
                    for Student_info in New_Students_List:
                        if idx == Student_info[1]:
                            if Student_info[3] == Club[Min_idx]:
                                return True
                return False
                            
            #Mu내에 2지망이 일치 하는가? 
            elif Max_idx == 3:
                #Space_Place내에 2지망이 일치 하는가? 
                Mu_Key_List = list(Mu.keys())
                for idx in Mu_Key_List:
                    for Student_info in New_Students_List:
                        if idx == Student_info[1]:
                            if Student_info[3] == Club[Min_idx]:
                                return True
                return False

            #Sof내에 2지망이 일치 하는가?
            elif Max_idx == 4:
                #Space_Place내에 2지망이 일치 하는가? 
                Sof_Key_List = list(Sof.keys())
                for idx in Sof_Key_List:
                    for Student_info in New_Students_List:
                        if idx == Student_info[1]:
                            if Student_info[3] == Club[Min_idx]:
                                return True
                return False


            #Arch내에 2지망이 일치 하는가? 
            elif Max_idx == 5:
                #Space_Place내에 2지망이 일치 하는가? 
                Arch_Key_List = list(Arch.keys())
                for idx in Arch_Key_List:
                    for Student_info in New_Students_List:
                        if idx == Student_info[1]:
                            if Student_info[3] == Club[Min_idx]:
                                return True
                return False




        for i in New_Students_List:
            
            #1지망이 Team_X인 신입생
            if 0 == Club_Value.index(i[2]):      
                Team_X_Add(i[1], i[0])

            if 1 == Club_Value.index(i[2]):
                Small_Space_Add(i[1], i[0])

            #1지망이 공장인 신입생
            if 2 == Club_Value.index(i[2]):    
                Space_Place_Add(i[1], i[0])

            #1지망이 뮤인 신입생
            if 3 == Club_Value.index(i[2]):
                Mu_Add(i[1], i[0])

            #1지망이 소프인 신입생
            if 4 == Club_Value.index(i[2]):    
                Sof_Add(i[1], i[0])

            #1지망이 아키인 신입생
            if 5 == Club_Value.index(i[2]):
                Arch_Add(i[1], i[0])

            #1지망이 비작인 신입생
            if 6 == Club_Value.index(i[2]):
                Nothing_Add(i[1], i[0])





        #모든 작업실에서 최소 인원을 충족하는가? 충족하지 않으면 가장 많은 신입생을 보유한 작업실에서 신입생을 최소로 보유한 작업실로 이동

        #cnt로 브레이크를 검
        cnt = 0
        clock = 0       #임시방편
        Club_Member_Number_List = [len(Team_X),len(Small_Space),len(Space_Place),len(Mu),len(Sof),len(Arch)]
        while(len(Team_X) < Min_Member or len(Small_Space) < Min_Member or len(Space_Place) < Min_Member or len(Mu) < Min_Member or len(Sof) < Min_Member or len(Arch) < Min_Member):
            
            Club_Member_Number_List = [len(Team_X),len(Small_Space),len(Space_Place),len(Mu),len(Sof),len(Arch)]

            #Club_Member_Number_List를 Check로 복사
            Check = Club_Member_Number_List[:]

            #최대 인원 가지고 있는 작업실 추출   
            Max_idx = Club_Member_Number_List.index(max(Club_Member_Number_List))

            #최소 인원 가지고 있는 작업실 추출
            Min_idx = Club_Member_Number_List.index(min(Club_Member_Number_List))
            
            Check1 = Check.pop(Check.index(max(Check)))
            Check2 = Check.pop(Check.index(max(Check)))
            if(Check1 == Check2):
                cnt += 1
                del Check[Max_idx]
                Max_idx = Check.index(max(Check)) + 1

            From_Max_To_Min(Max_idx, Min_idx)
            Check = Club_Member_Number_List
            clock += 1      #임시방편
            if(len(Team_X) >= Min_Member and len(Small_Space) >= Min_Member and len(Space_Place) >= Min_Member and len(Mu) >= Min_Member and len(Sof) >= Min_Member and len(Arch) >= Min_Member):
                break
            if(cnt == 10000 or clock == 10000):
                break




        #최대 많이 지원 받은 작업실에서 2지망으로 최소 인원 작업실이랑 매칭 되지 않을때

        cnt = 0
        while True:

            Club_Member_Number_List = [len(Team_X),len(Small_Space),len(Space_Place),len(Mu),len(Sof),len(Arch)]

            if(min(Club_Member_Number_List) == Min_Member):
                break

            if(cnt == 1000):
                break

            #가장 많은 작업실추출
            Max_Club = Club_Member_Number_List.index(max(Club_Member_Number_List))

            #가장 적은 작업실 추출
            Min_Club = Club_Member_Number_List.index(min(Club_Member_Number_List))

            #Team_X가 가장 많을 경우
            if Max_Club == 0:
                key = random.choice(list(Team_X.keys()))
                
                #Small_Space에 보내기
                if Min_Club == 1:
                    Small_Space_Add(key, Team_X[key])
                
                #Space_Place에 보내기
                elif Min_Club == 2:
                    Space_Place_Add(key, Team_X[key])

                #Mu에 보내기
                elif Min_Club == 3:
                    Mu_Add(key, Team_X[key])

                #소프에 보내기
                elif Min_Club == 4:
                    Sof_Add(key, Team_X[key])

                #아키에 보내기
                elif Min_Club == 5:
                    Arch_Add(key, Team_X[key])
                
                Team_X.pop(key)

            #Small_Space가 가장 많을 경우
            elif Max_Club == 1:
                key = random.choice(list(Small_Space.keys()))
                
                #Team_X에 보내기
                if Min_Club == 0:
                    Team_X_Add(key, Small_Space[key])
                
                #Space_Place에 보내기
                elif Min_Club == 2:
                    Space_Place_Add(key, Small_Space[key])

                #Mu에 보내기
                elif Min_Club == 3:
                    Mu_Add(key, Small_Space[key])

                #소프에 보내기
                elif Min_Club == 4:
                    Sof_Add(key, Small_Space[key])

                #아키에 보내기
                elif Min_Club == 5:
                    Arch_Add(key, Small_Space[key])

                Small_Space.pop(key)


            #Space_Place가 가장 많을 경우
            elif Max_Club == 2:
                key = random.choice(list(Space_Place.keys()))
                
                #Team_X에 보내기
                if Min_Club == 0:
                    Team_X_Add(key, Space_Place[key])
                
                #Small_Space에 보내기
                elif Min_Club == 1:
                    Small_Space_Add(key, Space_Place[key])

                #Mu에 보내기
                elif Min_Club == 3:
                    Mu_Add(key, Space_Place[key])

                #소프에 보내기
                elif Min_Club == 4:
                    Sof_Add(key, Space_Place[key])

                #아키에 보내기
                elif Min_Club == 5:
                    Arch_Add(key, Space_Place[key])

                Space_Place.pop(key)


            #Mu가 가장 많을 경우
            elif Max_Club == 3:
                key = random.choice(list(Mu.keys()))
                
                #Team_X에 보내기
                if Min_Club == 0:
                    Team_X_Add(key, Mu[key])
                
                #Small_Space에 보내기
                elif Min_Club == 1:
                    Small_Space_Add(key, Mu[key])

                #Space_Place에 보내기
                elif Min_Club == 2:
                    Space_Place_Add(key, Mu[key])

                #소프에 보내기
                elif Min_Club == 4:
                    Sof_Add(key, Mu[key])

                #아키에 보내기
                elif Min_Club == 5:
                    Arch_Add(key, Mu[key])

                Mu.pop(key)


        #Sof가 가장 많을 경우
            elif Max_Club == 4:
                key = random.choice(list(Sof.keys()))
                
                #Team_X에 보내기
                if Min_Club == 0:
                    Team_X_Add(key, Sof[key])
                
                #Small_Space에 보내기
                elif Min_Club == 1:
                    Small_Space_Add(key, Sof[key])

                #Space_Place에 보내기
                elif Min_Club == 2:
                    Space_Place_Add(key, Sof[key])

                #Mu에 보내기
                elif Min_Club == 3:
                    Mu_Add(key, Sof[key])

                #Arch에 보내기
                elif Min_Club == 5:
                    Arch_Add(key, Sof[key])

                Sof.pop(key)


            #Arch가 가장 많을 경우
            elif Max_Club == 5:
                key = random.choice(list(Arch.keys()))
                
                #Team_X에 보내기
                if Min_Club == 0:
                    Team_X_Add(key, Arch[key])
                
                #Small_Space에 보내기
                elif Min_Club == 1:
                    Small_Space_Add(key, Arch[key])

                #Space_Place에 보내기
                elif Min_Club == 2:
                    Space_Place_Add(key, Arch[key])

                #Mu에 보내기
                elif Min_Club == 3:
                    Mu_Add(key, Arch[key])

                #Sof에 보내기
                elif Min_Club == 4:
                    Sof_Add(key, Arch[key])

                Arch.pop(key)

            #작업이 한번 끝나면 cnt 1씩증가
            cnt += 1

        return {
            "Team_X": Team_X,
            "Small_Space": Small_Space,
            "Space_Place": Space_Place,
            "Mu": Mu,
            "Sof": Sof,
            "Arch": Arch,
            "Nothing": Nothing
        }
    