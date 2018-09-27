"""
Python 3.6
@author: wrgsRay
"""


def main():
    from appJar import gui

    def songChanged(rb):
        print(app.getRadioButton(rb))

    def reset(btn):
        # set back to the default, but don't call the change function
        app.setRadioButton("song", "Killer Queen", callFunction=False)

    app = gui()
    app.addRadioButton("song", "Killer Queen")
    app.addRadioButton("song", "Paradise City")
    app.setRadioButtonChangeFunction("song", songChanged)
    app.addButton("Reset", reset)
    app.go()


if __name__ == '__main__':
    main()
