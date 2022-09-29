
while True:
    grade=input('请输入你的成绩:')
    try:
        grade=int(grade)
    except Exception as e:
        print('invaild input type!',e)
        continue
    print(f'你的成绩是{grade}分')
    break
    
