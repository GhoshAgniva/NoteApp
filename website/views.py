from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from website import db
from .models import Note
from flask import send_file,make_response
from fpdf import FPDF
from flask import after_this_request
import os

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        # Add new note
        note = request.form.get('note')
        if note:
            if len(note) < 1:
                flash('Notes is too short', category='error')
            else:
                new_note = Note(data=note, user_id=current_user.id)
                db.session.add(new_note)
                db.session.commit()
                flash('Note Added!', category='success')

        # Delete a note
        delete_note_id = request.form.get('delete_note_id')
        if delete_note_id:
            note_to_delete = Note.query.get(delete_note_id)
            if note_to_delete and note_to_delete.user_id == current_user.id:
                db.session.delete(note_to_delete)
                db.session.commit()
                flash('Note deleted successfully', category='success')

        return redirect(url_for('views.home'))

    return render_template("home.html", user=current_user)



# Added New Feature - Edit Note

@views.route('/edit-note/<int:note_id>', methods=['GET', 'POST'])
@login_required
def edit_note(note_id):
    note = Note.query.get(note_id)
    if note and note.user_id == current_user.id:
        if request.method == 'POST':
            note.data = request.form.get('note')
            db.session.commit()
            flash('Note updated successfully!', category='success')
            return redirect(url_for('views.home'))
        return render_template('edit_note.html', note=note, user=current_user)  # Pass 'user'
    
    flash('Note not found or unauthorized access!', category='error')
    return redirect(url_for('views.home'))


#Export your notes as pdf


@views.route('/export-note/pdf/<int:note_id>')
@login_required
def export_note_pdf(note_id):
    note = Note.query.get(note_id)
    if note and note.user_id == current_user.id:
        try:
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=12)
            pdf.cell(200, 10, txt="Your Note", ln=True, align='C')
            pdf.multi_cell(0, 10, note.data)

            # Use absolute path for the PDF file
            pdf_path = os.path.join(os.getcwd(), f"your_note_{note_id}.pdf")
            pdf.output(pdf_path)

            # Confirm file creation
            if not os.path.exists(pdf_path):
                raise FileNotFoundError(f"Failed to create PDF: {pdf_path}")

            @after_this_request
            def remove_file(response):
                try:
                    if os.path.exists(pdf_path):
                        os.remove(pdf_path)
                except Exception as e:
                    print(f"Error deleting file: {e}")
                return response

            return send_file(pdf_path, as_attachment=True)

        except Exception as e:
            flash('An error occurred while generating the PDF.', category='error')
            print(e)
            return redirect(url_for('views.home'))

    flash('Note not found or unauthorized access!', category='error')
    return redirect(url_for('views.home'))
