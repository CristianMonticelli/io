"""Repository per le operazioni CRUD su items"""
from app import get_db

def get_all_items():
    """Ritorna tutti gli item dal database"""
    # TODO: Implementa la query
    # SELECT * FROM items
    db = get_db()
    return []  # Ritorna lista vuota per ora

def get_item_by_id(item_id):
    """Ritorna un item specifico per ID"""
    # TODO: Implementa la query
    # SELECT * FROM items WHERE id = ?
    db = get_db()
    return None  # Ritorna None per ora

def create_item(name, description):
    """Crea un nuovo item nel database"""
    # TODO: Implementa l'INSERT
    # INSERT INTO items (name, description) VALUES (?, ?)
    db = get_db()
    db.commit()

def update_item(item_id, name, description):
    """Aggiorna un item esistente"""
    # TODO: Implementa l'UPDATE
    # UPDATE items SET name = ?, description = ? WHERE id = ?
    db = get_db()
    db.commit()

def delete_item(item_id):
    """Elimina un item dal database"""
    # TODO: Implementa la DELETE
    # DELETE FROM items WHERE id = ?
    db = get_db()
    db.commit()
