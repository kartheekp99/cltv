from flask import Flask, render_template, session, redirect, url_for, request, send_file, send_from_directory
from flask_wtf import FlaskForm
from wtforms import FileField
from wtforms.validators import DataRequired
import pickle
import os
import pandas as pd

from handle_csv import Datasheet
from generate_report import Report

app = Flask(__name__)

app.config['SECRET_KEY'] = 'key'


class InfoForm(FlaskForm):
    file = FileField('file')


data = None


@app.route('/',methods = ['GET', 'POST'])
def index():
    form = InfoForm()
    if request.method=='POST':
        try:
            global data
            check = False
            input_data = pd.read_csv(form.file.data, encoding="cp1252")
            data = input_data.copy()
            Datasheet(input_data).compute()
            return redirect(url_for('download'))
        except:
            return render_template('file_error.html')
        
    return render_template('index.html', form = form)



@app.errorhandler(404)
def not_found(error):
    return render_template('404.html')


@app.route('/return-file/')
def return_file():
    directory = os.getcwd()
    return send_from_directory(directory,'customer_lifetime_value.csv', as_attachment=True)



@app.route('/download/', methods = ['GET', 'POST'])
def download():
    return render_template('download.html')



@app.route('/report/')
def report():
    try:
        report_data = Report(data).generate()
        return render_template(
                            'chart.html',
                            clv_data=report_data['clv'],
                            countries_data=report_data['countries'],
                            monthly_revenue = report_data['monthly_revenue'],
                            monthly_active = report_data['monthly_active'],
                            new_exist=report_data['New_Exist']
                        )
    except:
        return render_template('file_error.html')

    report_data = Report(data).generate()
    return render_template(
                            'chart.html',
                            clv_data=report_data['clv'],
                            countries_data=report_data['countries'],
                            monthly_revenue = report_data['monthly_revenue'],
                            monthly_active = report_data['monthly_active'],
                            new_exist=report_data['New_Exist']
                        )




if __name__ == '__main__':
    app.run(debug=True)