from flask import Flask, request, render_template, send_from_directory

app = Flask(__name__)

power_strength = [[12, 1, 3, 1], [11, 1, 3, 2], [10, 3, 3, 6], [9, 5, 3, 7],
                  [8, 7, 5, 10], [7, 9, 5, 10], [6, 11, 5, 10]]
endurance_isometric = [[3, 64, 3, 13], [5, 54, 3, 19], [7, 45, 3, 22], [9, 36, 3, 23], [11, 24, 3, 20]]


@app.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory('static', filename)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/program_detail')
def program():
    message = request.args.get('message')
    print(message, type(message))
    mode = request.args.get('mode')
    if mode == 'power':
        return_list = power_strength
    else:
        return_list = endurance_isometric
    return render_template('program_detail.html', list=return_list, mode=mode, message=message)


@app.route('/workout')
def workout():
    timex = int(request.args.get('time'))
    rest = int(request.args.get('rest'))
    modex = request.args.get('mode')
    time_invested = request.args.get('time_invested')
    reps = int(request.args.get('reps')) if modex == 'power' else int(request.args.get('reps'))*2
    return render_template('workout.html', hold=timex, rest=rest, count=reps, mode=modex,
                           time_invested=time_invested)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
