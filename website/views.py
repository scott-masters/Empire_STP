# This page has received basic logging.

import os
import flask as fl
import flask_login as fo
import pickle as pk

views = fl.Blueprint("views", __name__)

# TAB: VAGAS DE TRABALHO

@views.route("/jobs/AQ", methods = ["GET"])
def AQ():
    return fl.render_template(f"jobs/AQ.html")

@views.route("/jobs/AQ/form", methods = ["GET", "POST"])
def AQ_form():
    if fl.request.method == "POST":
        data = fl.request.form
        name = data.get("name")
        phone = data.get("phone")
        mode = data.get("mode")
        filename = name + " " + phone
        filename = filename.replace(" ", "_")
        try:
            if mode == "cv":
                cv_file = fl.request.files.get("cv")
                cv_file.save(f"applications/AQ/{filename}.pdf")
            with open(f"applications/AQ/{filename}.pkl", "wb") as file:
                pk.dump(data, file)
        except:
            if mode == "cv":
                cv_file = fl.request.files.get("cv")
                cv_file.save(f"/home/PortalSTP/Empire_STP/applications/AQ/{filename}.pdf")
            with open(f"/home/PortalSTP/Empire_STP/applications/AQ/{filename}.pkl", "wb") as file:
                pk.dump(data, file)
        return fl.render_template(f"jobs/submitted.html")
    return fl.render_template(f"jobs/AQ_form.html")

@views.route("/jobs/CE", methods = ["GET"])
def CE():
    return fl.render_template(f"jobs/CE.html")

@views.route("/jobs/CE/form", methods = ["GET", "POST"])
def CE_form():
    if fl.request.method == "POST":
        data = fl.request.form
        name = data.get("name")
        phone = data.get("phone")
        filename = name + " " + phone
        filename = filename.replace(" ", "_")
        try:
            with open(f"applications/CE/{filename}.pkl", "wb") as file:
                pk.dump(data, file)
        except:
            with open(f"/home/PortalSTP/Empire_STP/applications/CE/{filename}.pkl", "wb") as file:
                pk.dump(data, file)
        return fl.render_template(f"jobs/submitted.html")
    return fl.render_template(f"jobs/CE_form.html")

@views.route("/jobs/IN", methods = ["GET"])
def IN():
    return fl.render_template(f"jobs/IN.html")

@views.route("/jobs/IN/form", methods = ["GET", "POST"])
def IN_form():
    if fl.request.method == "POST":
        data = fl.request.form
        name = data.get("name")
        phone = data.get("phone")
        filename = name + " " + phone
        filename = filename.replace(" ", "_")
        try:
            with open(f"applications/IN/{filename}.pkl", "wb") as file:
                pk.dump(data, file)
        except:
            with open(f"/home/PortalSTP/Empire_STP/applications/IN/{filename}.pkl", "wb") as file:
                pk.dump(data, file)
        return fl.render_template(f"jobs/submitted.html")
    return fl.render_template(f"jobs/IN_form.html")

@views.route("/jobs/CT", methods = ["GET"])
def CT():
    return fl.render_template(f"jobs/CT.html")

@views.route("/jobs/LB", methods = ["GET"])
def LB():
    return fl.render_template(f"jobs/LB.html")

# TAB: SOBRE NÓS

@views.route("/about_us")
def about_us():
    return fl.render_template("about_us.html")

@views.route("/offline")
def offline():
    return fl.render_template("offline.html", user = fo.current_user)

@views.route("/ping")
def ping():
    return fl.Response("ping", status = 200, mimetype = "text/plain")

# 1470