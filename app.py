from flask import Flask, render_template, redirect, session, flash
from flask_debugtoolbar import DebugToolbarExtension
from models import connect_db, db, User, Feedback
from forms import LoginForm, UserForm, FeedbackForm



app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///feedback"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True
app.config["SECRET_KEY"] = "abc123"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

connect_db(app)

app.app_context().push()

db.create_all()

toolbar = DebugToolbarExtension(app)

@app.route('/')
def show_home():
    """ Redirect to register """
    return redirect('/register')

@app.route('/register', methods=["GET", "POST"])
def register_user():
    """ Display register form """
    
    form = UserForm()
    
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        first_name = form.first_name.data
        last_name = form.last_name.data
        email = form.email.data
        
        user = User.register(username, password, first_name, last_name, email)
        db.session.add(user)
        db.session.commit()

        session['username'] = user.username

        
        return redirect('/')
    
    else:
        return render_template('form-register.html', form=form)

@app.route('/login', methods=["GET", "POST"])
def form_login():
    """login form to authenticate user"""
    
    form = LoginForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
    
        user = User.authenticate(username, password)
        if user:
            session['user_username'] = user.username
            return redirect(f'/users/{username}')
        else:
            form.username.errors = ['Invalid username/password.']

    return render_template('form-login.html', form=form)

@app.route('/users/<username>')
def show_user(username):
    """ Render user details page """
    if 'user_username' not in session or session['user_username'] != username:
        flash('Please login first before trying to access that page.', 'danger')
        return redirect('/login')
    else:
        user = User.query.filter_by(username=username).first()
        return render_template('user-details.html', user=user)
    
@app.route('/logout')
def logout_user():
    """ Log out user """
    session.pop('user_username')
    flash('You have been successfully logged out.', 'success')
    return redirect('/login')

@app.route('/users/<username>/delete', methods=['POST'])
def delete_user(username):
    """ Delete user """
    if 'user_username' not in session or session['user_username'] != username:
        flash('Please login to your own account.', 'danger')
        return redirect('/login')
    else:
        session.pop('user_username')
        Feedback.query.filter_by(username=username).delete()
        db.session.commit()
        User.query.filter_by(username=username).delete()
        db.session.commit()
        return redirect('/login')

#### Feedback routes

@app.route('/users/<username>/feedback/add', methods=['GET', 'POST'])
def feedback_form(username):
    """ Show feedback form """
    form = FeedbackForm()
    user = User.query.get_or_404(username)
    
    if form.validate_on_submit():
        title = form.title.data
        content = form.content.data
        
        if 'user_username' not in session or session['user_username'] != username:
            flash('Please login to your own account.', 'danger')
            return redirect('/login')
        else:
            feedback = Feedback(title=title, content=content, username=username)
            db.session.add(feedback)
            db.session.commit()
            return redirect(f'/users/{username}')
    
    return render_template('form-feedback.html', user=user, form=form)

@app.route('/feedback/<int:feedbackID>/update', methods=['GET', 'POST'])
def update_feedback(feedbackID):
    """ Update feedback """
    feedback = Feedback.query.filter_by(id=feedbackID).first()
    username = feedback.username
    form = FeedbackForm(obj=feedback)

    if form.validate_on_submit():
        title = form.title.data
        content = form.content.data
        
        if 'user_username' not in session or session['user_username'] != username:
            flash('Please login to your own account.', 'danger')
            return redirect('/login')
        else:
            feedback.title = title
            feedback.content = content
            db.session.add(feedback)
            db.session.commit()
            return redirect(f'/users/{username}')
    
    return render_template('edit-feedback.html', username=username, form=form)
    
@app.route('/feedback/<int:feedbackID>/delete', methods=['POST'])
def delete_feedback(feedbackID):
    """ Delete feedback """
    feedback = Feedback.query.filter_by(id=feedbackID).first()
    username = feedback.username
    
    if 'user_username' not in session or session['user_username'] != username:
        flash('Please login to your own account.', 'danger')
        return redirect('/login')
    else:
        Feedback.query.filter_by(id=feedbackID).delete()
        db.session.commit()
        return redirect(f'/users/{username}')