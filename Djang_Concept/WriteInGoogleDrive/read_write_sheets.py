from flask import Flask, jsonify, request
from oauth2client.service_account import ServiceAccountCredentials
import gspread

app = Flask(__name__)
creds = ServiceAccountCredentials.from_json_keyfile_name('/path/to/secret_key.json')

@app.route('/add_post', methods=['POST'])
def add_post():
    # Extract the data from the request body
    data = request.get_json()
    post_data = data.get('post_data')
    
    # Parse the data and update the sheet
    sheet_data = [[post_data.get('name'), post_data.get('city'), post_data.get('country'), post_data.get('score'), post_data.get('rating')]]
    try:
        file = gspread.authorize(creds)
        workbook = file.open("student_info")
        sheet = workbook.sheet1
        sheet.update('A6', sheet_data)
        return jsonify({'success': True, 'message': 'Post added successfully'})
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
