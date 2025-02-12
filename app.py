from flask import Flask, request, render_template
import time

app = Flask(__name__)

power_strength = [[12, 1,], [11, 1], [10, 3], [9, 5], [8, 7], [7, 9], [6, 11]]
endurance_isometric = [[3, 64], [5, 54], [7, 45], [9, 36], [11, 24]]


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/program_detail')
def program():
    mode = request.args.get('mode')
    if mode == 'power':
        return_list = power_strength
        rest = 3
    else:
        return_list = endurance_isometric
        rest = 5
    return render_template('program_detail.html', list=return_list, rest=rest)


@app.route('/workout')
def workout():
    timex = request.args.get('time')
    reps = request.args.get('reps')
    rest = request.args.get('rest')
    return render_template('workout.html', hold=timex, rest=rest, count=reps)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)

