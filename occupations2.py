#Bayle Smith-Salzberg
#SoftDev1 pd8
#HW03 -- ..and Now Enjoy Its Contents
#2016-09-23

from flask import Flask, render_template
import util.testmod
    

mHello=Flask(__name__)
@mHello.route("/")
def hello_world():
    return "goodbye world"

@mHello.route("/occupations")
def plugIn():
    return render_template("html.html",var="occupations table", fool=util.testmod.prof_dict, rand = util.testmod.randMan())

if __name__=="__main__":
    mHello.debug = True
    mHello.run()
