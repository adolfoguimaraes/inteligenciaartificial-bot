from joblib import load


class CustomSentiment():

    def __init__(self):

        file_model = load("data/models/sentiment.joblib")
        self.model = file_model['model']
        self.vector = file_model['vector']



    def sentiment(self, text):
        ptext = self.vector.transform([text])
        value = self.model.predict(ptext)

        if value[0] == 0:
            return "negative"
        else: 
            return 'positive'



if __name__ == '__main__':

    custom_ = CustomSentiment()

    print(custom_.sentiment("I hate music."))
