"""
Python 3.6
@author: wrgsRay
"""
from appJar import gui

def main():
    def submit(button):
        if button == 'Submit':
            filepath = app.openBox()
            app.setLabel('result', filepath)

    app = gui('Testing Goodness', '400x300')

    app.setFont(20)
    app.addLabel('title', 'Hello World')
    app.addLabelEntry('Check this ASIN')
    app.addButton('Submit', submit)
    app.addLabel('result', 'Please input an ASIN')
    app.go()


if __name__ == '__main__':
    main()
