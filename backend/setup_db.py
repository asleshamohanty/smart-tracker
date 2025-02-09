from app import db, app
from models import User  # Import your User model

with app.app_context():
    db.create_all()  # Create all tables
    print("✅ Database created successfully!")

    # Add a test user
    new_user = User(fullname="Aslesha Mohanty", username="aslesha", email="aslesha@example.com", password="securepassword")
    db.session.add(new_user)
    db.session.commit()
    print("✅ Test user added successfully!")


    users = User.query.all()
    for user in users:
        print(user.id, user.fullname, user.username, user.email)

