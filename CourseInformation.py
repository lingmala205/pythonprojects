def main():

    roomNumber = {'CS101':'3004','CS102':'4501',
                  'CS103':'6755','NT110':'1244',
                  'CM241':'1411'}

    print("Course Number(key)\tRoom Number(value)")
    print("__________________________________________")
    for key, value in roomNumber.items():
        print(key,"\t","\t","\t", value)

    print()
    print()
    
    instructor = {'CS101':'Haynes','CS102':'Alvarado',
                  'CS103':'Rich','NT110':'Burke',
                  'CM241':'Lee'}

    print("Course Number(key)\tInstructor(value)")
    print("__________________________________________")
    for key, value in instructor.items():
        print(key,"\t","\t","\t", value)


    print()
    print()
    
    meetingTime = {'CS101':'8:00 a.m.','CS102':'9:00 a.m.',
                   'CS103':'10:00 a.m.','NT110':'11:00 a.m.',
                   'CM241':'1:00 p.m.'}

    print("Course Number(key)\tMeeting Time(value)")
    print("__________________________________________")
    for key, value in meetingTime.items():
        print(key,"\t","\t","\t", value)


    

main()
