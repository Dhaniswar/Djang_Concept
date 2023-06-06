import gspread
from oauth2client.service_account import ServiceAccountCredentials
import requests

creds = ServiceAccountCredentials.from_json_keyfile_name("./data/secret_key.json")

# gc = pygsheets.authorize()
def read_write(event=None, context=None):

    try:

        file = gspread.authorize(creds)
        workbook = file.open("student_info")
        sheet = workbook.sheet1
        for cell in sheet.range('A1:A5'):
            print(cell.value)
        # print(sheet.range('A2:A5'))

        sheet.update('A6', [["Hari", "paris", "France", 100, 15.5], ["Ram", "paris", "France", 100, 15.5]])
    except:
        raise("Error occurs")
        





