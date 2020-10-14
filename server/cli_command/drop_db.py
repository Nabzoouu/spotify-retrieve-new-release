import datetime

def build_drop_db_cli_command(db, app):
  @app.cli.command("drop_db")
  def drop_db():
    db.drop_all()
    db.create_all()