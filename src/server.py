import json
from flask import Flask,render_template,request,redirect,flash,url_for

from src.data_fetching import get_data
from src.helper.helper import is_not_a_past_competition, is_valid_purchase


app = Flask(__name__)
app.secret_key = 'something_special'

get_data.load()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/show-summary',methods=['POST'])
def show_summary():
    if club := get_data.get_club_by_email(request.form['email']):
        return render_template('welcome.html',club=club,competitions=get_data.competitions)
    flash("Sorry, that email wasn't found.")
    return redirect(url_for('index'))


@app.route('/book/<competition>/<club>')
def book(competition,club):
    found_club = get_data.get_club_by_name(club)
    found_competition = get_data.get_competition_by_name(competition)
    if found_club and found_competition:
        return render_template('booking.html',club=found_club,competition=found_competition)
    flash("Something went wrong-please try again")
    return render_template('welcome.html', club=club, competitions=get_data.competitions)


@app.route('/purchase-places',methods=['POST'])
def purchase_places():
    competition = get_data.get_competition_by_name(request.form["competition"])
    club = get_data.get_club_by_name(request.form["club"])
    places_required = int(request.form['places'])
    if competition and club and is_not_a_past_competition(competition):
        if is_valid_purchase(competition,club,places_required):
            competition['numberOfPlaces'] = int(competition['numberOfPlaces']) - int(places_required)
            club["points"] = int(club["points"]) - (int(places_required) * 3)
            flash('Great-booking complete!')
        else: 
            flash("Sorry, that wasn't a valid purchase, maybe you don't have enough points or competition is full, you're also not allowed to book negative or zero places")
    else:
        flash("Past competitions can't be booked")
    return render_template('welcome.html', club=club, competitions=get_data.competitions)


@app.route('/clubs')
def clubs():
    if clubs := get_data.clubs:
        return render_template('clubs.html',clubs=clubs)
    flash("Sorry, there are no clubs to show")
    return redirect(url_for('index'))


@app.route('/logout')
def logout():
    return redirect(url_for('index'))