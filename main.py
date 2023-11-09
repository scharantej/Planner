 
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

schedules = []

@app.route('/')
def index():
  return render_template('index.html', schedules=schedules)

@app.route('/create_schedule', methods=['GET', 'POST'])
def create_schedule():
  if request.method == 'POST':
    schedule = request.form.get('schedule')
    schedules.append(schedule)
    return redirect(url_for('index'))
  return render_template('create_schedule.html')

@app.route('/view_schedule/<int:schedule_id>')
def view_schedule(schedule_id):
  schedule = schedules[schedule_id]
  return render_template('view_schedule.html', schedule=schedule)

@app.route('/edit_schedule/<int:schedule_id>', methods=['GET', 'POST'])
def edit_schedule(schedule_id):
  schedule = schedules[schedule_id]
  if request.method == 'POST':
    schedule = request.form.get('schedule')
    schedules[schedule_id] = schedule
    return redirect(url_for('index'))
  return render_template('edit_schedule.html', schedule=schedule)

@app.route('/delete_schedule/<int:schedule_id>')
def delete_schedule(schedule_id):
  schedules.pop(schedule_id)
  return redirect(url_for('index'))

if __name__ == '__main__':
  app.run(debug=True)
