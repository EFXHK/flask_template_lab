from flask import render_template, request, redirect
from app import app
from models.event_list import events, save_event
from models.event import Event


@app.route("/events")
def index():
    return render_template("index.html", title="Home", events=events)

@app.route("/events", methods=["POST"])
def add_event():
    test = request.form["event"]
    event_description = request.form["description"]
    new_event = Event(event_name, event_description)
    save_event(new_event)
    return redirect("/events")


# @app.route("/events", methods=["POST"])
# def add_event():
#     task_title = request.form["title"]
#     task_description = request.form["description"]
#     new_event = Event(task_title, task_description, False)
#     save_event(new_event)
#     return redirect("/events")

