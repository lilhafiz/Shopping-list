from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

login_manager = LoginManager(app)
login_manager.login_view = 'login'

# Sample data for the shopping list
shopping_list = ["Jersey", "Watch", "Shoes"]

# Sample user data (for demonstration purposes)
class User(UserMixin):
    def __init__(self, user_id):
        self.id = user_id

# Replace this with your actual user database or authentication logic
users = {'user1': User('user1')}

@login_manager.user_loader
def load_user(user_id):
    return users.get(user_id)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        # Replace this with your actual authentication logic
        if username in users and password == 'password':
            user = users[username]
            login_user(user)
            return redirect(url_for('index'))

    return render_template('login.html')


@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/')
@login_required
def index():
    return render_template('index.html', shopping_list=shopping_list, username=current_user.id)

@app.route('/clear-list', methods=['POST'])
def clear_list():
    shopping_list.clear()
    return jsonify(success=True)

@app.route('/add_item', methods=['POST'])
@login_required
def add_item():
    item = request.form.get('item')
    if item:
        shopping_list.append(item)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
