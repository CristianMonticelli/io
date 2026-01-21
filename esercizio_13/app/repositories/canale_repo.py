from app.db import get_db

def get_canale():
    db = get_db()
    query = '''
            SELECT id, nome, numero_iscritti, categoria_id
            FROM canali 
            ORDER BY numero_iscritti DESC'''
       
        
    channels = db.execute(query).fetchall()
    return [dict(channel) for channel in channels]

def get_categoria():
    db = get_db()
    query = '''
            SELECT id, nome  
            FROM categoria 
            '''
       
        
    categorie = db.execute(query).fetchall()
    return [dict(categoria) for categoria in categorie]

def get_canale_id(id):
    db = get_db()
    query = '''
            SELECT id, nome, numero_iscritti, categoria_id
            FROM canali 
            WHERE id=?'''
    print("--------------------------------------------------------")
    print(query)
        
    channel = db.execute(query,(id,)).fetchone()
    if channel:
        return dict(channel)
    return None

def get_video_id(id):
    db = get_db()
    query = '''
            SELECT id, canale_id, titolo
            FROM video 
            WHERE canale_id=?'''
    
        
    channels = db.execute(query,(id,)).fetchall()
    return [dict(channel) for channel in channels]

def create_channel(nome: str, numero_iscritti: int, categoria: str) -> None:
    db = get_db()
    query = '''
            INSERT INTO canali (nome, numero_iscritti, categoria)
            VALUES (?, ?, ?)'''
    cursor = db.execute(query, (nome, numero_iscritti, categoria))
    db.commit()
    return cursor.lastrowid

def create_video(canale_id: str, titolo: str, durata: int, immagine: str) -> None:
    db = get_db()
    query = '''
            INSERT INTO video (canale_id, titolo, durata, immagine)
            VALUES (?, ? ,?,?)'''
    cursor = db.execute(query, (canale_id, titolo, durata, immagine))
    db.commit()
    return cursor.lastrowid
