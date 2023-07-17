"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file contains the routes for your application.
"""
import os
from app import app,db
from flask import render_template, request, redirect, url_for, flash, session, abort,send_from_directory,jsonify
from app.models import Illustrations
#from app.forms import IllustrationForm
from werkzeug.utils import secure_filename


#to run flask, run flask --app Flask/app --debug run

###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')

@app.route('/jmf')
def jmfhome():
    #ppic = db.session.execute(db.select(Photography)).scalars() 
    return render_template('jmf.html')#,ppic=ppic)

@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Bob")

@app.route('/test',methods=['POST'])
def test():
    if (request.method=='POST'):
        """ 
        data = request.get_json()
        value1 = data['user']
        value2 = data['test']
        
        """
    value1 = request.form.get('name')
    value2 = request.form.get('cost')
    """Render the website's about page."""
    print(value1)
    print(value2)
    response_data = {'message': 'Success'}
    #return render_template('about.html', name="Bob")
    return jsonify(response_data)

@app.route("/photo/add", methods=['POST', 'GET'])
def addPhoto():
     
    test='Love'
    #pseriesList.append((test,test))
    form=IllustrationForm()
    if request.method == 'POST':
        if form.validate_on_submit:
            genre = form.genre.data
            series = form.series.data
            photodata = form.photo.data
            photo = secure_filename(photodata.filename) #Name of photo
            photopath=os.path.join(app.config['P_FOLDER'],photo)
            photodata.save(photopath)

            """ 
            # opening the file in read mode
            my_file = open("test.txt", "w")

            my_file.write(genre)
            
            my_file.close()

            """
            #add a button to the side to add a section


           
            
            # new_photo = Photography(photo,x,cmodel,genre,series)
            # db.session.add(new_photo)
            # db.session.commit()
            #photodata.save(os.path.join(app.config['UPLOAD_FOLDER'],photo))
            
            flash('Property successfully added!', 'success')
            #return redirect(url_for('showProperties'))


    return render_template('addPhoto.html')

@app.route('/puploads/<filename>')
def get_image(filename):
    return send_from_directory(os.path.join(os.getcwd(), app.config['P_FOLDER']), filename)

@app.route("/ppic")
def showProperties():
    #ppic = db.session.execute(db.select(Photography)).scalars()
    return render_template('show_properties.html')#,ppic=ppic) 

###
# The functions below should be applicable to all Flask apps.
###

# Display Flask WTF errors as Flash messages
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404
