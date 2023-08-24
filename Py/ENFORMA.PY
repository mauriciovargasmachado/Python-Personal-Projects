class Person:
    def __init__(self, name, surname, start_date, size, weight, age, arms, chest, abdomen, waist, legs):
        self.name = name
        self.surname = surname
        self.start_date = start_date
        self.size = size
        self.weight = weight
        self.age = age
        self.arms = arms
        self.chest = chest
        self.abdomen = abdomen
        self.waist = waist
        self.legs = legs
        self.trainings = []

    def edit_info(self, name=None, surname=None, start_date=None, size=None, weight=None, age=None, arms=None,
                  chest=None, abdomen=None, waist=None, legs=None):
        if name:
            self.name = name
        if surname:
            self.surname = surname
        if start_date:
            self.start_date = start_date
        if size:
            self.size = size
        if weight:
            self.weight = weight
        if age:
            self.age = age
        if arms:
            self.arms = arms
        if chest:
            self.chest = chest
        if abdomen:
            self.abdomen = abdomen
        if waist:
            self.waist = waist
        if legs:
            self.legs = legs

    def add_training(self, training):
        self.trainings.append(training)

    def remove_training(self, training):
        self.trainings.remove(training)

    def get_trainings(self):
        return self.trainings

    def stop_training(self, date, reason):
        self.end_date = date
        self.reason = reason


class Exercise:
    def __init__(self, name, description, calories_per_rep, youtube_link):
        self.name = name
        self.description = description
        self.calories_per_rep = calories_per_rep
        self.youtube_link = youtube_link

    def edit_exercise(self, name=None, description=None, calories_per_rep=None, youtube_link=None):
        if name:
            self.name = name
        if description:
            self.description = description
        if calories_per_rep:
            self.calories_per_rep = calories_per_rep
        if youtube_link:
            self.youtube_link = youtube_link


class Training:
    def __init__(self, exercise, date, reps, time):
        self.exercise = exercise
        self.date = date
        self.reps = reps
        # time in (hours, minutes, seconds)
        self.time = time

    def edit_training(self, exercise=None, date=None, reps=None, time=None):
        if exercise:
            self.exercise = exercise
        if date:
            self.date = date
        if reps:
            self.reps = reps
        if time:
            # time in (hours, minutes, seconds)
            self.time = time


class EnForma:
    def __init__(self):
        #HACER EL ARRAY FICTICIO DE PERSONAS YA VINCULADAS EN LA APP Y CONSEGUIR ALGUN VIDEO FICTICIO PARA PROBARLA
