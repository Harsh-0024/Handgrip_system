from flask import Flask, request, render_template, send_from_directory

app = Flask(__name__)

power_strength = [[12, 1, 3], [11, 1, 3], [10, 3, 3], [9, 5, 3], [8, 7, 5], [7, 9, 5], [6, 11, 5]]
endurance_isometric = [[3, 64, 3], [5, 54, 3], [7, 45, 3], [9, 36, 3], [11, 24, 3]]


@app.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory('static', filename)


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
    rest = request.args.get('rest')
    modex = request.args.get('mode')
    reps = request.args.get('reps') if modex == 'power' else int(request.args.get('reps'))*2
    return render_template('workout.html', hold=timex, rest=rest, count=reps, mode=modex)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
