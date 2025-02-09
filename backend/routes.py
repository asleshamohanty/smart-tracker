from flask import Blueprint, request, jsonify
from models import db, User, Task  # ✅ Import db from models.py
from werkzeug.security import generate_password_hash, check_password_hash

api = Blueprint('api', __name__)

# ✅ Example: Register user
@api.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    hashed_password = generate_password_hash(data['password'])
    new_user = User(fullname=data['fullname'], username=data['username'], email=data['email'], password=hashed_password)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User registered successfully!"})

@api.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    # Find user in the database
    user = User.query.filter_by(username=username).first()

    if user and check_password_hash(user.password, password):
        return jsonify({"message": "Login successful!"}), 200
    else:
        return jsonify({"message": "Invalid username or password"}), 401
    
@api.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    title = data.get('title')
    description = data.get('description')
    user_id = data.get('user_id')  # Assume user is already logged in and passed their user_id

    # Create new task and add to the database
    new_task = Task(
        title=title,
        description=description,
        user_id=user_id
    )
    db.session.add(new_task)
    db.session.commit()

    return jsonify({"message": "Task created successfully!"}), 201

@api.route('/tasks/<int:user_id>', methods=['GET'])
def list_tasks(user_id):
    tasks = Task.query.filter_by(user_id=user_id).all()
    return jsonify([task.title for task in tasks]), 200

@api.route('/tasks', methods=['POST'])
def add_task():
    data = request.get_json()
    title = data.get('title')
    user_id = data.get('user_id')
    
    if not title or not user_id:
        return jsonify({"error": "Title and user_id are required"}), 400
    
    new_task = Task(title=title, user_id=user_id)
    db.session.add(new_task)
    db.session.commit()
    
    return jsonify({"message": "Task created successfully", "task": new_task.title}), 201

@api.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = Task.query.get(task_id)
    
    if not task:
        return jsonify({"error": "Task not found"}), 404
    
    db.session.delete(task)
    db.session.commit()
    
    return jsonify({"message": "Task deleted successfully"}), 200

@api.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    data = request.get_json()
    new_title = data.get('title')
    new_completed_status = data.get('completed')
    
    task = Task.query.get(task_id)
    
    if not task:
        return jsonify({"error": "Task not found"}), 404
    
    # Update the title if it's provided
    if new_title is not None:
        task.title = new_title
    
    # Update the completed status if it's provided
    if new_completed_status is not None:
        task.completed = new_completed_status
    
    db.session.commit()
    
    return jsonify({"message": "Task updated successfully", "task": {"title": task.title, "completed": task.completed}}), 200
