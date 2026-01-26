#!/usr/bin/env python
"""Script per avviare l'applicazione Flask"""

from app import create_app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
