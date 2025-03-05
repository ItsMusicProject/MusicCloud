import os
from werkzeug.utils import secure_filename

def get_file_type(filename):
    """Determine file type category based on extension"""
    ext = filename.rsplit('.', 1)[1].lower()
    if ext in {'jpg', 'jpeg', 'png', 'gif'}:
        return 'image'
    elif ext in {'mp3', 'wav'}:
        return 'audio'
    elif ext in {'mp4', 'avi', 'mov'}:
        return 'video'
    else:
        return 'document'

def create_user_directory(upload_folder, username):
    """Create directory for user files"""
    user_dir = os.path.join(upload_folder, secure_filename(username))
    os.makedirs(user_dir, exist_ok=True)
    return user_dir
