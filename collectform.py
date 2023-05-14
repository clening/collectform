from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        first_naem = request.form.get('first_name')
        last_name = request.form.get('last_name')
        age = request.form.get('age')
        address = request.form.get('address')
        gender = request.form.get('gender')
        government_id = request.form.get('government_id')
        sexual_orientation = request.form.get('sexual_orientation')

        # write to a text file
        with open('output.txt', 'a') as f:
            f.write(f'Name: {first.name + last_name}, Age: {age}, Address: {address}, Gender: {gender}, Government ID: {government_id}, Sexual Orientation: {sexual_orientation}\n')

        return 'Form submitted successfully.'

    return render_template('form.html')

if __name__ == "__main__":
    app.run(debug=True)
