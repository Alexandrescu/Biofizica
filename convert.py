import json
import random

counter = 1
questions = []


def convertToArray():
    global counter
    global questions
    f = open("Modul2.txt", "r")

    question = ""
    lines = f.read().splitlines()
    accumulated_lines = 0
    for line in lines:
        # print line
        # print len(line.strip()) == 0
        if len(line.strip()) == 0 and accumulated_lines > 1 and question is not "":
            counter += 1
            questions.append(question)
            question = ""
            accumulated_lines = 0
        else:
            # print question
            accumulated_lines += 1
            if question == "":
                question = line
            elif len(line.strip()) != 0:
                question = "{question}\n{line}".format(question=question, line=line)
    print counter


def print_partial():
    global questions
    with open('partial.txt', 'w') as the_file:
        for idx, question in enumerate(questions):
            # print "Printing", question
            the_file.write("Intrebarea {idx}\n".format(idx=idx))
            the_file.write("{question}".format(question=question))
            the_file.write("\n\n")


correct_objects = []


def isgood(s):
    if not (isinstance(s, str) or isinstance(s, unicode)):
        print 'YESYESYES'
    return isinstance(s, str) or isinstance(s, unicode)


def convert(question, idx):
    if not isgood(question):
        return
    print idx
    [q, a] = question.split("The correct answer is:", 1)
    global correct_objects
    correct_objects.append({
        "question": r"{}".format(q.replace("Correct", "").replace("Incorrect", "")),
        "answer": a,
        "full": question,
        "idx": idx
    })
    print "\n\n\nQuestion", q
    print "Answer", a, "\n\n\n"


def count_correct():
    correct_counter = 0
    feedback_counter = 0
    ras_corr_counter = 0
    for idx, question in enumerate(questions):
        good = False
        if "The correct answer is:" in question:
            correct_counter += 1
            good = True
            convert(question, idx)
        if "Feedback" in question:
            feedback_counter += 1
            good = True
        if "RaspundeCorrect" in question:
            ras_corr_counter += 1
            good = True
        if not good:
            print idx

    print "Correct", correct_counter, len(questions)
    print "Feedback", feedback_counter, len(questions)
    print "Ras Correct", ras_corr_counter, len(questions)


def output():
    write_file = open("data.json", 'w')
    global correct_objects
    # write_file.write(
    random.shuffle(correct_objects)
    write_file.write(json.dumps(correct_objects, ensure_ascii=False))


def main():
    convertToArray()
    print_partial()
    count_correct()
    output()

main()
