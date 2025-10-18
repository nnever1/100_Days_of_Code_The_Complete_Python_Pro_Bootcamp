def calculate_love_score(person1,person2):
    true_tally=0
    love_tally=0
    love_score=""
    true= ["t","r","u","e"]
    love = ["l","o","v","e"]
    for t_letter in true:
        for letter in person1.lower():
            if letter == t_letter:
                true_tally += 1
    love_score= f"T occurs {true_tally} times"
    print(love_score)
    #     for letter in person2.lower():
    #         if letter == t_letter:
    #             true_tally += 1
    # print(f"T occurs {true_tally}\n R occurs {true_tally}")
    # for l_letter in love:
    #     for letter in person1:
    #         if letter == l_letter:
    #             love_tally += 1
    #     for letter in person2:
    #         if letter == l_letter:
    #             love_tally += 1
calculate_love_score("Tim","love")