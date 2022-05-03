import docx
import main_logic
import random
def F(tasks, v , path): # массив заданий # количество вариантов #путь
    doc = docx.Document()
    answers = []
    variants = [x for x in range(1, v+1)]
    for _ in variants: #сколько вариантов генерим
        doc.add_paragraph("                                                                            Вариант: "+str(_))
        for i in tasks: #какие задания будут в варианте
            (task, answer) = main_logic.F('t'+str(i), 'v5', False)
            print(task)
            doc.add_paragraph(task)
            answers.append(answer)
        doc.paragraphs[len(doc.paragraphs)-1].runs[0].add_break(docx.enum.text.WD_BREAK.PAGE)    # разрыв страницы
    doc.save(path+'/variants.docx')

    doc_answer = docx.Document()
    doc_answer.add_paragraph("Ответы: ")
    for _ in variants:
        doc_answer.add_paragraph("                                                                            Вариант: " + str(_))
        for i in tasks:
            doc_answer.add_paragraph(str(str(i) + ")" + answers[i]))
        doc_answer.paragraphs[len(doc_answer.paragraphs) - 1].runs[0].add_break(docx.enum.text.WD_BREAK.PAGE)  # разрыв страницы
    doc_answer.save(path+'/variants_answers.docx')