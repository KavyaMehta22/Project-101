import dropbox
class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token
    def upload_folder(self, folder_from, folder_to):
        dbx = dropbox.Dropbox(self.access_token)
        f = open(folder_from, 'rb')
        dbx.folders_upload(f.read(), folder_to)

def main():
    access_token = "WL4ml0YRTHIAAAAAAAAAAWtA3xnKeGdaBBPHgdm-pJiLj9lUvS0pAl4XZvb36LWL"
    transferData = TransferData(access_token)
    folder_from = input("Enter the folder path to transfer :-")
    folder_to = input("Enter the full path to upload to dropbox:- ") # This is the full path to upload the folder to, including name that you wish the folder to be called once uploaded.
# API v2
    transferData.upload_folder(folder_from, folder_to)
    print("folder has been moved !!!")

main()
