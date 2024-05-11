from flask import Flask, render_template, request
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB connection
client = MongoClient('mongodb://localhost:27017/')
db = client['comment_database']
comments_collection = db['comments']

@app.route('/')
def index():
    # Fetch comments from MongoDB
    comments = comments_collection.find()
    return render_template('index.html', comments=comments)

@app.route('/post_comment', methods=['POST'])
def post_comment():
    if request.method == 'POST':
        comment_text = request.form['comment']
        
        # Store the comment in MongoDB
        comments_collection.insert_one({'text': comment_text})
        
        # Redirect to home page after posting comment
        return index()

if __name__ == '__main__':
    app.run(debug=True)
