import dropbox
import os

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        with open(local_path, 'rd') as f:
            dbx.file_upload(f.read(), dropbox_path, mode = WriteMode('overwrite'))

def main():
    access_token = 'sl.Ary0ZKJiy0AJ61sVnbugP-wRVvEkkLASUCPciaeJNkTjuW5OnLchcMksVwFxyT5myqssOGjPbv84TRPDSB-Dk-tau8pRNPWchVvIzGg-hhsYv75Z-PzsCJh3ZlZYcah77Uw7m8g'
    transferData = TransferData(access_token)

    file_from = input("Enter the file: ")
    file_to = input("Enter the path of the upload to dropbox: ")
    
    transferData.upload_file(file_from, file_to)
    print("File has been moved")

main()
