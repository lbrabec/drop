class Config():
    UPLOAD_FOLDER = '~/Drop'
    ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'heic', 'heif', 'mov'}
    PORT = 6969

    def set_drop_dir(self, drop_dir):
        self.UPLOAD_FOLDER = drop_dir

config = None

def get_config():
    global config
    if not config:
        config = Config()

    return config
