#!/usr/bin/env python3
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager, Shell

from app import create_app, db
from app.models.user import UserModel

app = create_app('default')
manager = Manager(app)
Migrate(app, db)

def make_shell_context():
    """
    Cria um contexto de execução personalizado para a aplicação
    """

    return dict(
        app=app,
        db=db,
        UserModel=UserModel
    )

manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
