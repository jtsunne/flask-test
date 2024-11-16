from src.frontend import frontend
from src.config import DI
from flask import render_template
from dependency_injector.wiring import inject, Provide
from datetime import datetime


@frontend.context_processor
def inject_now():
    return {"now": datetime.now()}


@frontend.route("/", methods=["GET"])
def home_():
    return render_template("home.html")


@frontend.route("/config", methods=["GET"])
@inject
def config(cfg=Provide[DI.config]):
    print(cfg)
    return render_template(
        "home.html",
        cfg=cfg,
    )
