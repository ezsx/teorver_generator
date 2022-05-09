import docx

import arr_generate
import main_logic
import random
def F(tasks, v , path): # массив заданий # количество вариантов # путь
    doc = docx.Document()
    answers = []
    variants = [x for x in range(1, v+1)] # 1-10
    for j in variants: # сколько вариантов генерим
        doc.add_paragraph("                                                                            Вариант: "+str(j))
        ans=[]
        for i in tasks: # какие задания будут в варианте
            (task, answer) = main_logic.F('t'+str(i), 'v5')
            doc.add_paragraph(task)
            ans.append(answer)
        answers.append(ans)
        doc.paragraphs[-1].runs[0].add_break(docx.enum.text.WD_BREAK.PAGE)    # разрыв страницы
    doc.save(path+'/variants.docx')

    doc_answer = docx.Document()
    doc_answer.add_paragraph("Ответы: ")
    for j in variants:
        doc_answer.add_paragraph("                                                                            Вариант: " + str(j))
        for i in tasks:
            doc_answer.add_paragraph(str(str(i) + ") " + answers[j-1][i-1]))
        doc_answer.paragraphs[-1].runs[0].add_break(docx.enum.text.WD_BREAK.PAGE)  # разрыв страницы
    doc_answer.save(path+'/variants_answers.docx')
F(arr_generate.F('1-10'), 10, "C:/Users/scdco/Documents/My Cheat Tables")