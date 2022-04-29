import docx

import main_logic

doc = docx.Document()
answers = []
answers2 = []
for i in range(1, 17):
    (v1, v2) = main_logic.F('t'+str(1), 'v4', False)
    doc.add_paragraph(v1)
    answers.append(v2)
doc.paragraphs[len(doc.paragraphs)-1].runs[0].add_break(docx.enum.text.WD_BREAK.PAGE) # разрыв страницы
for i in range(1, 17):
    (v1, v2) = main_logic.F('t'+str(1), 'v5', False)
    doc.add_paragraph(v1)
    answers2.append(v2)
doc.paragraphs[len(doc.paragraphs)-1].runs[0].add_break(docx.enum.text.WD_BREAK.PAGE) # разрыв страницы
doc.add_paragraph("Ответы: ")
for i in range(1,len(answers)):
    doc.add_paragraph(str(str(i)+")"+answers[i]))
doc.paragraphs[len(doc.paragraphs)-1].runs[0].add_break(docx.enum.text.WD_BREAK.PAGE) # разрыв страницы
for i in range(1,len(answers2)):
    doc.add_paragraph(str(str(i)+")"+answers2[i]))
doc.save('smth.docx')