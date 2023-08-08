#!/usr/bin/python3
"""
This module initiates a FileStorage instance and reloads it from a file
(if it exists).
"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
