from flask import Flask, request, render_template
app = Flask(__name__)

power_strength = [[12, 1, 3], [11, 1, 3], [10, 3, 3], [9, 5, 3], [8, 7, 5], [7, 9, 5], [6, 11, 5]]
endurance_isometric = [[3, 64, 5], [5, 54, 5], [7, 45, 5], [9, 36, 5], [11, 24, 5]]


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/program_detail')
def program():
    mode = request.args.get('mode')
    if mode == 'power':
        return_list = power_strength
    else:
        return_list = endurance_isometric
    return render_template('program_detail.html', list=return_list, mode=mode)


@app.route('/workout')
def workout():
    timex = request.args.get('time')
    reps = request.args.get('reps')
    rest = request.args.get('rest')
    modex = request.args.get('mode')
    return render_template('workout.html', hold=timex, rest=rest, count=reps, mode=modex)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
