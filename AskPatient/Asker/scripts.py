def upload_answer(request, 
                  answers_db, 
                  comments_db,
                  doctor_db,
                  questions_db,
                  av_answerd_db):
    """Внесение в базы данных ответов
    Args:
        request (QueryDict): request (Запрос)
        answers_db (object): Модель ответов
        comments_db (object): Модель комментариев
    """
    patient = request.POST['snils']
    questions = {}
    req_questions = request.POST.getlist('questions')
    for quest in req_questions:
        answers = quest.split('_')
        questions[answers[0]] = answers[1]
    doctor = request.POST['doctor_choose']
    comment = request.POST['commentary']
    try:
        for quest in questions:
            answers_db.objects.create(
                patient = patient,
                question = questions_db.objects.get(id=quest),
                doctor = doctor_db.objects.get(id=doctor),
                answer = av_answerd_db.objects.get(id=questions[quest])
            )
        
        comments_db.objects.create(
            comment = comment,
            doctor = doctor_db.objects.get(id=doctor)
        )
        return [True, 'Success']
    except Exception as error_add:
        return [False, error_add]