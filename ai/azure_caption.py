from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from msrest.authentication import CognitiveServicesCredentials
import os


# pip install azure-cognitiveservices-vision-computervision

class AzureCaption():

    def __init__(self):
        self.region = "eastus"
        self.key = "7a600cf67daa4e4eae3b796213a9cff2"
        self.endpoint = "https://d2l-captionimage.cognitiveservices.azure.com/"
        

        self.credentials = CognitiveServicesCredentials(self.key)
        self.client = ComputerVisionClient(endpoint=self.endpoint,credentials=self.credentials)

    def caption_image(self, image):
        result = result = self.client.describe_image_in_stream(image)
        return result.captions[0].text


#
    

if __name__ == "__main__":

    azure_ = AzureCaption()

    with open("smile-g2f31ce42f_1920.jpg",'rb') as img:
        text_ = azure_.caption_image(img)
        print(text_)





