from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Reflection
from . import db
import json

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        reflection = request.form.get('reflection')

        if len(reflection) < 1:
            flash('Please input a Reflection!', category='error')
        else:
            new_reflection = Reflection(data=reflection, user_id=current_user.id)
            db.session.add(new_reflection)
            db.session.commit()
            flash('Reflection added!', category='success')

    return render_template("home.html", user=current_user)


@views.route('/delete-reflection', methods=['POST'])
def delete_reflection():
    reflection = json.loads(request.data)
    reflectionId = reflection['reflectionId']
    reflection = Reflection.query.get(reflectionId)
    if reflection:
        if reflection.user_id == current_user.id:
            db.session.delete(reflection)
            db.session.commit()

    return jsonify({})