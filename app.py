from flask import Flask

AI=Flask(__name__)

# create one view function and decorate it with route method of AI

@AI.route('/wish')
def wish():
    return 'This is my first flask View Function'

@AI.route('/second')
def second():
    return 'Second View Function'

if __name__=='__main__':
    AI.run(debug=True)