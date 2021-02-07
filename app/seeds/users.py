from werkzeug.security import generate_password_hash
from app.models import db, User

# Adds a demo user, you can add other users here if you want
## AI Generated Faces https://generated.photos/faces


def seed_users():

    demo = User(username='Demo', email='demo@aa.io',
                password='password', firstName='Demo', lastName='User', profileImg='https://images.generated.photos/qNwRFWNSN3FVMRBTzI4s_q5cpxkkhkix9Q-EipSRoPc/rs:fit:256:256/Z3M6Ly9nZW5lcmF0/ZWQtcGhvdG9zL3Yz/XzA4NzM5NDYuanBn.jpg')
    demo2 = User(username='Demo1', email='demo1@aa.io',
                 password='password', firstName='Ryan', lastName='Wellington', profileImg='https://images.generated.photos/wJ17Fkghd7To0OWuqoIczIiguTaMa1M634kr9E4veiI/rs:fit:256:256/Z3M6Ly9nZW5lcmF0/ZWQtcGhvdG9zL3Yz/XzAzMjAxNzcuanBn.jpg')
    demo3 = User(username='Demo2', email='demo2@aa.io',
                 password='password', firstName='Jackie', lastName='Wade', profileImg='https://images.generated.photos/jO38FEIfMHn0Akh2CT6SXcna-uRNOtQAFa9PRiUToG4/rs:fit:256:256/Z3M6Ly9nZW5lcmF0/ZWQtcGhvdG9zL3Yz/XzA5MjU1MTIuanBn.jpg')
    demo4 = User(username='Demo3', email='demo3@aa.io',
                 password='password', firstName='Raj', lastName='Kumar', profileImg='https://images.generated.photos/jrKRLtnvZZUZskO0qqX8bABCRMPD7Cp5rWJuxfSOo7Y/rs:fit:256:256/Z3M6Ly9nZW5lcmF0/ZWQtcGhvdG9zL3Yz/XzA5OTc4NDUuanBn.jpg')
    demo5 = User(username='Demo4', email='demo4@aa.io',
                 password='password', firstName='Rishia', lastName='Crowe', profileImg='https://images.generated.photos/5CLeaeMFH5ebkXgGWi-lVNbnVNlHVxynsirxT4GljME/rs:fit:256:256/Z3M6Ly9nZW5lcmF0/ZWQtcGhvdG9zL3Yz/XzA0MzM3MTkuanBn.jpg')
    demo6 = User(username='Demo5', email='demo5@aa.io',
                 password='password', firstName='Bethany', lastName='Woods', profileImg='https://images.generated.photos/0IMOH9ou8FFhZO13vthSDLRVOktCdeys0opP3fJo4Hs/rs:fit:256:256/Z3M6Ly9nZW5lcmF0/ZWQtcGhvdG9zL3Yz/XzA0Mzc4NDAuanBn.jpg')
    demo7 = User(username='Demo6', email='demo6@aa.io',
                 password='password', firstName='Daniel', lastName='Cliffe', profileImg='https://images.generated.photos/rN2ygnRNFLFo06uHfz5IXzqONJlXYKVD8gT1eCy6L78/rs:fit:256:256/Z3M6Ly9nZW5lcmF0/ZWQtcGhvdG9zL3Yz/XzAxNDE0MzIuanBn.jpg')
    demo8 = User(username='Demo7', email='demo7@aa.io',
                 password='password', firstName='Karishma', lastName='Ramano', profileImg='https://images.generated.photos/6QmDMgrbxH_oalMczk1RsTttd3CoWcTONlsfdey56aU/rs:fit:256:256/Z3M6Ly9nZW5lcmF0/ZWQtcGhvdG9zL3Yz/XzAxNjQzNjEuanBn.jpg')
    demo9 = User(username='Demo8', email='demo8@aa.io',
                 password='password', firstName='Jim', lastName='Caringo', profileImg='https://images.generated.photos/tto6p603fPilklNh-rhUjlc3YW4OJXhE6IDD8nH2048/rs:fit:256:256/Z3M6Ly9nZW5lcmF0/ZWQtcGhvdG9zL3Yz/XzA1MjIwMDMuanBn.jpg')
    demo10 = User(username='Demo9', email='demo9@aa.io',
                  password='password', firstName='Robert', lastName='Dawson', profileImg='https://images.generated.photos/3tQ6Nv-_MuhLX0hAt7jNe63_4KFBCqcaHkXstcQwu6c/rs:fit:256:256/Z3M6Ly9nZW5lcmF0/ZWQtcGhvdG9zL3Yz/XzAyMjM2MzMuanBn.jpg')

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
