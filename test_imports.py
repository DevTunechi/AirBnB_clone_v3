#!/usr/bin/env python3

try:
    import sqlalchemy
    print("sqlalchemy imported successfully")
except ImportError as e:
    print("Error importing sqlalchemy:", e)

try:
    import models
    print("models imported successfully")
except ImportError as e:
    print("Error importing models:", e)

try:
    from models.engine.file_storage import FileStorage
    print("FileStorage imported successfully")
except ImportError as e:
    print("Error importing FileStorage:", e)

