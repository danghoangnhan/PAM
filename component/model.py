class Answer:
    def __init__(self,id, question,similarity=-1,answer=-1):
        self.id = id
        self.question = question
        self.answer = answer
        self.similarity = similarity
    

    # Setter method for 'answer'
    def set_id(self, id):
        self.id = id

    # Getter method for 'answer'
    def get_id(self):
        return self.id

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
    
    def to_dict(self):
        """
        Convert the Answer object to a dictionary.
        """
        return {
            'question': self.id,
            'participants_ans': self.answer,
            'participants_evaluation': self.similarity
        }