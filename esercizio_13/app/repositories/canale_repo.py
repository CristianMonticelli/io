from app.db import get_db

def get_canale():
    """Recupera tutti i coinquilini di un immobile."""
    db = get_db()
    query = '''
            SELECT id, nome, numero_iscritti, categoria
            FROM canali 
            ORDER BY numero_iscritti DESC'''
       
        
    channels = db.execute(query).fetchall()
    return [dict(channel) for channel in channels]


def get_canale_id(id):
    """Recupera tutti i coinquilini di un immobile."""
    db = get_db()
    query = '''
            SELECT canale_id, titolo
            FROM video 
            GROUP BY canale_id
            WHERE canale_id=?''',(id)
       
        
    videos = db.execute(query).fetchall()
    return [dict(channel) for channel in videos]

       