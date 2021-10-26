import dropbox

class TransferData:
    def __init__(self,access_token):
        self.access_token = access_token
    def upload_file(self,file_from,file_to):
        dbx = dropbox.Dropbox(self.access_token)
        f = open(file_from,'rb')
        dbx.files_upload(f.read(),file_to)
def main():
    access_token = 'orxxkFAHg3YAAAAAAAAAAXB1j8l1LMhRViIOpzSGwkuJ6NZkAdIrxw5cFmumke-J'
    transferData = TransferData(access_token)
    file_from = input('Enter The File Path You Want To Transfer : ')
    file_to = input('Enter The Full Path TO Upload To Dropbox : ')
    transferData.upload_file(file_from,file_to)
    print('File Has Been Moved')
main()

