"""Repository per le operazioni CRUD su items"""
from app import get_db

def get_all_items():
    """Ritorna tutti gli item dal database"""
    db = get_db()
    query = """
        SELECT 
            id,
            name,
            description,
            created
        FROM items
        ORDER BY created DESC
    """
    items = db.execute(query).fetchall()
    return items if items else []

def get_item_by_id(item_id):
    """Ritorna un item specifico per ID"""
    db = get_db()
    query = """
        SELECT 
            id,
            name,
            description,
            created
        FROM items
        WHERE id = ?
    """
    item = db.execute(query, (item_id,)).fetchone()
    return item

def search_items_by_name(search_term):
    """Ricerca item per nome (case-insensitive con LIKE)"""
    db = get_db()
    search_pattern = f"%{search_term}%"
    query = """
        SELECT 
            id,
            name,
            description,
            created
        FROM items
        WHERE LOWER(name) LIKE LOWER(?)
        ORDER BY created DESC
    """
    items = db.execute(query, (search_pattern,)).fetchall()
    return items if items else []

def create_item(name, description):
    """Crea un nuovo item nel database"""
    db = get_db()
    query = """
        INSERT INTO items (name, description)
        VALUES (?, ?)
    """
    db.execute(query, (name, description))
    db.commit()

def update_item(item_id, name, description):
    """Aggiorna un item esistente"""
    db = get_db()
    query = """
        UPDATE items
        SET name = ?, description = ?
        WHERE id = ?
    """
    db.execute(query, (name, description, item_id))
    db.commit()

def delete_item(item_id):
    """Elimina un item dal database"""
    db = get_db()
    query = """
        DELETE FROM items
        WHERE id = ?
    """
    db.execute(query, (item_id,))
    db.commit()
