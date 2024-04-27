from flask import Blueprint, request, render_template, redirect, url_for
from app.database import db
from app.models.models import Player, PerformanceAttribute, PhysicalAttribute
# from app.dash_app import dash_app

player_bp = Blueprint('player_bp', __name__)

# Display all players
@player_bp.route('/')
def players():
    all_players = Player.query.all()
    return render_template('players.html', players=all_players)

# Display form to add a new player
@player_bp.route('/add', methods=['GET'])
def add_player_form():
    return render_template('add_player.html')

# Process adding a new player
@player_bp.route('/add', methods=['POST'])
def add_player():
    name = request.form['name']
    api_id = request.form['api_id']
    new_player = Player(player_name=name, player_api_id_x=api_id)
    db.session.add(new_player)
    db.session.commit()
    return redirect(url_for('player_bp.players'))

# Display form to update a player
@player_bp.route('/update/<int:id>', methods=['GET'])
def update_player_form(id):
    player = Player.query.get(id)
    return render_template('update_player.html', player=player)

@player_bp.route('/view_performance/<int:id>', methods=['GET'])
def view_performance(id):
    player = Player.query.get_or_404(id)
    performance_attributes = PerformanceAttribute.query.filter_by(player_api_id=id).first()
    return render_template('performance_attributes.html', player=player, performance_attributes=performance_attributes)

@player_bp.route('/view_physical/<int:id>', methods=['GET'])
def view_physical(id):
    player = Player.query.get_or_404(id)
    physical_attributes = PhysicalAttribute.query.filter_by(player_api_id=id).first()
    return render_template('physical_attributes.html', player=player, physical_attributes=physical_attributes)

# Process updating a player
@player_bp.route('/update/<int:id>', methods=['POST'])
def update_player(id):
    player = Player.query.get(id)
    player.player_name = request.form['name']
    db.session.commit()
    return redirect(url_for('player_bp.players'))

# Delete a player
@player_bp.route('/delete/<int:id>', methods=['POST'])
def delete_player(id):
    player = Player.query.get(id)
    db.session.delete(player)
    db.session.commit()
    return redirect(url_for('player_bp.players'))

# player_routes.py

@player_bp.route('/visualizations')
def render_visualizations():
    return dash_app.index()
