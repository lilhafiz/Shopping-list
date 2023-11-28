from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)

# Sample data for the shopping list
shopping_list = ["Jersey", "Watch", "Shoes"]

@app.route('/')
def index():
    return render_template('index.html', shopping_list=shopping_list)

@app.route('/add', methods=['POST'])
def add_item():
    item = request.form.get('item')
    if item:
        shopping_list.append(item)
    return redirect(url_for('index'))

@app.route('/clear-list', methods=['POST'])
def clear_list():
    shopping_list.clear()
    return jsonify(success=True)

@app.route('/remove-item', methods=['POST'])
def remove_item():
    item_to_remove = request.json.get('item')
    if item_to_remove in shopping_list:
        shopping_list.remove(item_to_remove)
        return jsonify(success=True)
    else:
        return jsonify(success=False, error='Item not found in the list')

if __name__ == '__main__':
    app.run(debug=True)
