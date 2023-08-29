class Answer:
    def __init__(self, question):
        self.question = question
        self.answer = None
        self.similarity = None

    # Setter method for 'answer'
    def set_answer(self, answer):
        self.answer = answer

    # Getter method for 'answer'
    def get_answer(self):
        return self.answer

    # Setter method for 'similarity'
    def set_similarity(self, similarity):
        self.similarity = similarity

    # Getter method for 'similarity'
    def get_similarity(self):
        return self.similarity

    # Setter method for 'question'
    def set_question(self, question):
        self.question = question

    # Getter method for 'question'
    def get_question(self):
        return self.question