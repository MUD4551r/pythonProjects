def ask(ques, ans):
    u_ans = input(ques+ " ")
    if u_ans.lower() == ans.lower():
        print("Correct !")
        return 1
    else:
        print("Wrong!")
        return 0 
score = 0
score += ask("Capital of Pakistan?", "Islamabad")
score += ask("2 + 2 ? ", "4")

print("your score : ", score)