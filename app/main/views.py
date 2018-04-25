from . import main
from flask import render_template



@main.route('/')
def index():

  title ="housing"
  return render_template('index.html',title = title)

@main.route('/kenya')
def kenya():

  title ="housing"
  return render_template('kenya.html',title = title)

@main.route('/tanzania')
def tanzania():

  title ="housing"
  return render_template('tanzania.html',title = title)

  @main.route('/uganda')
  def uganda():

    title ="housing"
    return render_template('uganda.html',title = title)
