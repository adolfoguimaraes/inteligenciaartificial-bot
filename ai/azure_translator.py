import requests, uuid, json


class AzureTranslator():

    def __init__(self):

        # Add your subscription key and endpoint
        subscription_key = "710de65c377943c39e3e28be216174f9"
        endpoint = "https://api.cognitive.microsofttranslator.com"

        # Add your location, also known as region. The default is global.
        # This is required if using a Cognitive Services resource.
        location = "eastus"

        path = '/translate'
        self.constructed_url = endpoint + path

        self.params = {
            'api-version': '3.0',
            'from': 'en',
            'to': ['pt']
        }
        

        self.headers = {
            'Ocp-Apim-Subscription-Key': subscription_key,
            'Ocp-Apim-Subscription-Region': location,
            'Content-type': 'application/json',
            'X-ClientTraceId': str(uuid.uuid4())
        }



    def translate(self, text):
        # You can pass more than one object in body.
        body = [{
            'text': text
        }]

        request = requests.post(self.constructed_url, params=self.params, headers=self.headers, json=body)
        response = request.json()

        return response[0]['translations'][0]['text']


if __name__ == "__main__":

    azure_ = AzureTranslator()
    azure_.translate("Hello World")