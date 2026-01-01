with open("text.txt","w") as f:
    list=["I\n","Like\n","Manya\n"]
    f.writelines(list)
    f.write("Happy New Year\n")
    f.write("2026")