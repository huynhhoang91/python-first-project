from Question import Question

question_prompts = [
    "1. What year was the first Iron Man movie released, kicking off the Marvel Cinematic Universe?\n"
    "(a) 2005\n(b) 2008\n(c) 2010\n(d) 2012",
    "2. What is the name of Thor's hammer?\n"
    "(a) Vanir\n(b) Mjolnir\n(c) Aesir\n(d) Norn",
    "3. In the Incredible Hulk, what does Tony tell Thaddeus Ross at the end of the film?\n"
    "(a) That he wants to study The Hulk\n(b) That he knows about S.H.I.E.L.D.\n(c) That they are putting a team together\n(d) That Thaddeus owes him money",
    "4. What is Captain America's shield made of?\n"
    "(a) Adamantium\n(b) Vibranium\n(c) Promethium\n(d) Carbonadium",
    "5. The Flerkens are a race of extremely dangerous aliens that resembles what?\n"
    "(a) Cats\n(b) Ducks\n(c) Reptiles\n(d) Raccoons",
    "6. Before becoming Vision, what is the name of Iron Man’s A.I. butler?\n"
    "(a) H.O.M.E.R.\n(b) J.A.R.V.I.S\n(c) A.L.F.R.E.D.\n(d) M.A.R.V.I.N.",
    "7. What is the real name of the Black Panther?\n"
    "(a) T'Challa\n(b) M'Baku\n(c) N'Jadaka\n(d) N'Jobu",
    "8. What is the alien race Loki sends to invade Earth in The Avengers?\n"
    "(a) The Chitauri\n(b) The Skrulls\n(c) The Kree\n(d) The Flerkens",
    "9. Who was the last holder of the Space Stone before Thanos claims it for his Infinity Gauntlet?\n"
    "(a) Thor\n(b) Loki\n(c) The Collector\n(d) Tony Stark",
    "10. What fake name does Natasha use when she first meets Tony?\n"
    "(a) Natalie Rushman\n(b) Natalia Romanoff\n(c) Nocole Rohan\n(d) Naya Rabe"
]

#creates object questions
questions = [
    Question(question_prompts[0], "b"),
    Question(question_prompts[1], "b"),
    Question(question_prompts[2], "c"),
    Question(question_prompts[3], "b"),
    Question(question_prompts[4], "a"),
    Question(question_prompts[5], "b"),
    Question(question_prompts[6], "a"),
    Question(question_prompts[7], "a"),
    Question(question_prompts[8], "b"),
    Question(question_prompts[9], "a")
]

def run_test(questions):
    #keep track user's score
    score = 0
    for question in questions:
        answer = input(question.prompt + "\nYour answer: ")
        if answer == question.answer:
            score += 1

    print("You got " + str(score) + "/" + str(len(questions)) + " Correct")


run_test(questions)