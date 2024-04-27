from app.database import db

class Player(db.Model):
    __tablename__ = 'players'
    player_api_id_x = db.Column(db.Integer, primary_key=True)
    player_name = db.Column(db.String(255), nullable=False)

class PhysicalAttribute(db.Model):
    __tablename__ = 'physical_attributes'
    id = db.Column(db.Integer, primary_key=True)
    player_api_id = db.Column(db.Integer, db.ForeignKey('players.player_api_id'))
    height = db.Column(db.Numeric(5, 2))
    weight = db.Column(db.Numeric(5, 2))

class PerformanceAttribute(db.Model):
    __tablename__ = 'performance_attributes'
    player_fifa_api_id = db.Column(db.Integer, primary_key=True)
    player_api_id = db.Column(db.Integer, db.ForeignKey('players.player_api_id'))
    overall_rating = db.Column(db.Numeric(3, 1))
    potential = db.Column(db.Numeric(3, 1))
    preferred_foot = db.Column(db.String(50))
    attacking_work_rate = db.Column(db.String(50))
    defensive_work_rate = db.Column(db.String(50))
    agility = db.Column(db.Numeric(3, 1))
    balance = db.Column(db.Numeric(3, 1))
    shot_power = db.Column(db.Numeric(3, 1))
    stamina = db.Column(db.Numeric(3, 1))
    strength = db.Column(db.Numeric(3, 1))
    long_shots = db.Column(db.Numeric(3, 1))
    aggression = db.Column(db.Numeric(3, 1))
    penalties = db.Column(db.Numeric(3, 1))
