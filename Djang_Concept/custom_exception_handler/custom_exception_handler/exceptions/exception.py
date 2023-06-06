from rest_framework.exceptions import APIException


class UnreadableCSVFile(APIException):
    status_code = 400
    default_detail = "Unable to read file."
    default_code = "unreadable_csv_file"