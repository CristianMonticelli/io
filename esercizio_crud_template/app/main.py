from flask import Blueprint, g, redirect, render_template, request, url_for, flash
from werkzeug.exceptions import abort
from app.repositories import item_repository

bp = Blueprint('main', __name__)

# ============= READ - Visualizza tutti gli item =============
@bp.route('/')
def index():
    """Mostra la lista di tutti gli item"""
    items = item_repository.get_all_items()
    return render_template('index.html', items=items)

# ============= READ - Visualizza un singolo item =============
@bp.route('/item/<int:item_id>')
def view_item(item_id):
    """Mostra i dettagli di un singolo item"""
    item = item_repository.get_item_by_id(item_id)
    if item is None:
        abort(404)
    return render_template('view.html', item=item)

# ============= CREATE - Crea un nuovo item =============
@bp.route('/create', methods=('GET', 'POST'))
def create():
    """Crea un nuovo item"""
    if request.method == 'POST':
        # TODO: Leggi i dati dal form
        # Esempio:
        # name = request.form['name']
        # description = request.form['description']
        # error = None
        
        # if not name:
        #     error = 'Il nome è obbligatorio'
        
        # if error is not None:
        #     flash(error)
        # else:
        #     item_repository.create_item(name, description)
        #     return redirect(url_for('main.index'))
        pass
    
    return render_template('create.html')

# ============= UPDATE - Modifica un item =============
@bp.route('/update/<int:item_id>', methods=('GET', 'POST'))
def update(item_id):
    """Modifica un item esistente"""
    item = item_repository.get_item_by_id(item_id)
    if item is None:
        abort(404)
    
    if request.method == 'POST':
        # TODO: Leggi i dati dal form e aggiorna
        # Esempio:
        # name = request.form['name']
        # description = request.form['description']
        # error = None
        
        # if not name:
        #     error = 'Il nome è obbligatorio'
        
        # if error is not None:
        #     flash(error)
        # else:
        #     item_repository.update_item(item_id, name, description)
        #     return redirect(url_for('main.view_item', item_id=item_id))
        pass
    
    return render_template('update.html', item=item)

# ============= DELETE - Elimina un item =============
@bp.route('/delete/<int:item_id>', methods=('POST',))
def delete(item_id):
    """Elimina un item"""
    item = item_repository.get_item_by_id(item_id)
    if item is None:
        abort(404)
    
    item_repository.delete_item(item_id)
    flash('Item eliminato con successo!')
    return redirect(url_for('main.index'))
