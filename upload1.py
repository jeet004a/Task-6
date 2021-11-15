####################################################################################################################
##################Import the libraries##############################################################################
####################################################################################################################
from flask import Flask
from google.cloud import storage
import google.cloud.storage
import json
import os

#####################################################################################################################
######Flask Constructor which takes te name of the current module as argument########################################
#####################################################################################################################
app=Flask(__name__)

######################################################################################################################
#########################It is used to set the endpoint of the application ###########################################
######################################################################################################################
@app.route('/')

######################################################################################################################
###Function of the Application used to upload the file in the GCP bucket and function also contain exception handling#
######################################################################################################################
def vit():
    try: 
        os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'resourcebusy-testing-ee624292f3b5.json'
        storage_client = storage.Client()
        bucket_name = 'resoucebusymanan_99'
        bucket = storage_client.bucket(bucket_name)
        PATH=os.path.join(os.getcwd(),'resourcebusy-testing-ee624292f3b5.json')
        os.environ['GOOGLE_APPLICATION_CREDENTIALS']=PATH
        storage_client=storage.Client(PATH)
        filename='index.html'
        UPLOADFILE=os.path.join(os.getcwd(),filename)
        bucket=storage_client.get_bucket('resoucebusymanan_99')
        blob=bucket.blob(filename)
        blob.upload_from_filename(UPLOADFILE)
        return "Task Compeleted"
    except Exception as e:
        return "Some error occurred Try Again"

#############################################################################################################################
#########################It is used to execute the code when the user run the scripts directly  #############################
#############################################################################################################################
if __name__=='__main__':
    app.run(debug=True)
