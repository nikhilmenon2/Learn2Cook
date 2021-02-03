from werkzeug.security import generate_password_hash
from app.models import db, User

# Adds a demo user, you can add other users here if you want


def seed_users():

    demo = User(username='Demo', email='demo@aa.io',
                password='password', firstName='Demo', lastName='User', profileImg='https://images-na.ssl-images-amazon.com/images/I/81EX5e24qBL._AC_SL1500_.jpg')
    demo2 = User(username='Demo1', email='demo1@aa.io',
                 password='password', firstName='Ryan', lastName='Reynolds', profileImg='https://www.randomlists.com/img/people/ryan_reynolds.webp')
    demo3 = User(username='Demo2', email='demo2@aa.io',
                 password='password', firstName='Jackie', lastName='Chan', profileImg='https://www.randomlists.com/img/people/jackie_chan.webp')
    demo4 = User(username='Demo3', email='demo3@aa.io',
                 password='password', firstName='Dwayne', lastName='Wade', profileImg='https://www.randomlists.com/img/people/dwayne_wade.webp')
    demo5 = User(username='Demo4', email='demo4@aa.io',
                 password='password', firstName='Russell', lastName='Crowe', profileImg='https://www.randomlists.com/img/people/russell_crowe.webp')
    demo6 = User(username='Demo5', email='demo5@aa.io',
                 password='password', firstName='Tiger', lastName='Woods', profileImg='https://www.randomlists.com/img/people/tiger_woods.webp')
    demo7 = User(username='Demo6', email='demo6@aa.io',
                 password='password', firstName='Daniel', lastName='Radcliffe', profileImg='https://www.randomlists.com/img/people/daniel_radcliffe.webp')
    demo8 = User(username='Demo7', email='demo7@aa.io',
                 password='password', firstName='Ray', lastName='Ramano', profileImg='https://www.randomlists.com/img/people/ray_romano.webp')
    demo9 = User(username='Demo8', email='demo8@aa.io',
                 password='password', firstName='Jim', lastName='Carey', profileImg='https://www.randomlists.com/img/people/jim_carrey.webp')
    demo10 = User(username='Demo9', email='demo9@aa.io',
                  password='password', firstName='Robert', lastName='Downey Jr', profileImg='https://www.randomlists.com/img/people/robert_downey_jr_.webp')

    db.session.add(demo)
    db.session.add(demo2)
    db.session.add(demo3)
    db.session.add(demo4)
    db.session.add(demo5)
    db.session.add(demo6)
    db.session.add(demo7)
    db.session.add(demo8)
    db.session.add(demo9)
    db.session.add(demo10)

    db.session.commit()

# Uses a raw SQL query to TRUNCATE the users table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and resets
# the auto incrementing primary key


def undo_users():
    db.session.execute('TRUNCATE users;')
    db.session.commit()
