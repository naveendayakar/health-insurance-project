
from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_USER'] = 'sql9365288'
app.config['MYSQL_PASSWORD'] = 'RLtjMbHeDA'
app.config['MYSQL_HOST'] = 'sql9.freemysqlhosting.net'
app.config['MYSQL_DB'] = 'sql9365288'


mysql= MySQL(app)

    
@app.route("/")
def home():
    cur = mysql.connection.cursor()
    # cur.execute('''
    # CREATE TABLE individuals (id INTEGER AUTO_INCREMENT PRIMARY KEY,
    # gender VARCHAR(8), date_of_birth DATE ,social_security VARCHAR(9) UNIQUE,smoking_status VARCHAR(5),
    # allergies VARCHAR(100),medical_conditions VARCHAR(100))''')
    # cur.execute('''
    # CREATE TABLE events (event_id INTEGER AUTO_INCREMENT PRIMARY KEY,
    # user_id INTEGER,
    # date_of_incidence DATE, type_of_issue VARCHAR(50) ,billed_amount DECIMAL(8,2),covered_amount DECIMAL(8,2),
    # FOREIGN KEY (user_id) REFERENCES individuals(id))''')
    # cur.execute('''DROP TABLE events''')
    # cur.execute('''DROP TABLE individuals''')
    return render_template("home.html")


@app.route("/AddIndividuals", methods=['GET','POST'])
def AddIndividuals():
    if request.method== "POST":
        result=request.form
        gender=result['gender']
        date_of_birth=result['date_of_birth']
        social_security=result['social_security']
        smoking_status=result['smoking_status']
        allergies=result['allergies']
        medical_conditions=result['medical_conditions']
        cur = mysql.connection.cursor()       
        try:
            cur.execute("INSERT INTO individuals (gender,date_of_birth,social_security,smoking_status,allergies,medical_conditions) VALUES(%s,%s,%s,%s,%s,%s)",(gender,date_of_birth,social_security,smoking_status,allergies,medical_conditions))
        except:
            return "Cannot Add Individual"
        mysql.connection.commit()
        cur.close()
        cur = mysql.connection.cursor()
        try:
            addedIndividual= cur.execute("SELECT id FROM individuals ORDER BY id DESC LIMIT 1")
        except (mysql.connection.Error, mysql.connection.Warning) as e:
            print(e) 
        if addedIndividual > 0:
            addedIndividual= cur.fetchone() 
        cur.close()
        return render_template('Individual.html', addedIndividual=addedIndividual)
    return render_template("AddIndividuals.html")

@app.route("/Individual")
def Individual():
    return render_template("Individual.html")

@app.route("/AddEvents", methods=['GET','POST'])
def AddEvents():
    if request.method== "POST":
        result=request.form
        user_id=result['user_id']
        date_of_incidence=result['date_of_incidence']
        type_of_issue=result['type_of_issue']
        billed_amount=result['billed_amount']
        covered_amount=result['covered_amount']
        cur = mysql.connection.cursor()
        try:
            cur.execute("INSERT INTO events (user_id,date_of_incidence,type_of_issue,billed_amount,covered_amount) VALUES(%s,%s,%s,%s,%s)",(user_id,date_of_incidence,type_of_issue,billed_amount,covered_amount))
        except:
            return "Cannot Add Event: Check if user id is present"
        
        mysql.connection.commit()
        cur.close()
        cur = mysql.connection.cursor()
        try:
            addedEvent= cur.execute("SELECT event_id FROM events ORDER BY event_id DESC LIMIT 1")
        except (mysql.connection.Error, mysql.connection.Warning) as e:
            print(e)
        if addedEvent > 0:
            addedEvent= cur.fetchone() 
        cur.close() 
        return render_template('Event.html', addedEvent=addedEvent)
    return render_template("AddEvents.html")

@app.route("/Event")
def Event():
    return render_template("Event.html")

@app.route("/AllIndividuals")
def AllIndividuals():
    cur= mysql.connection.cursor()
    try:
        resultIndividuals= cur.execute("SELECT * FROM individuals")
    except (mysql.connection.Error, mysql.connection.Warning) as e:
        print(e)  
    if resultIndividuals > 0:
        resultIndividuals= cur.fetchall()
        return render_template("AllIndividuals.html",resultIndividuals=resultIndividuals)
    return "Individuals Table is Empty"

@app.route("/AllEvents")
def AllEvents():
    cur= mysql.connection.cursor()
    try:
        resultEvents= cur.execute("SELECT * FROM events")
    except (mysql.connection.Error, mysql.connection.Warning) as e:
        print(e)   
    if resultEvents > 0:
        resultEvents= cur.fetchall()
        return render_template("AllEvents.html",resultEvents=resultEvents)
    return "Events Table is Empty"

@app.route("/AverageAge")
def AverageAge():
    cur= mysql.connection.cursor()
    try:
        resultAverageAge= cur.execute("SELECT CAST( AVG((YEAR(NOW()) - YEAR(date_of_birth) - (DATE_FORMAT(date_of_birth, '%m%d') < DATE_FORMAT(NOW(), '%m%d')))) AS DECIMAL(8,0)) as avg FROM individuals")
    except (mysql.connection.Error, mysql.connection.Warning) as e:
        print(e)  
    if resultAverageAge > 0:
        resultAverageAge= cur.fetchall()
        print(resultAverageAge)
        return render_template("AverageAge.html",resultAverageAge=resultAverageAge)
    return "Individuals Table is Empty: No Age Information"

@app.route("/TotalCoveredAmount")
def TotalCoveredAmount():
    cur= mysql.connection.cursor()
    try:
        resultTotalCoveredAmount= cur.execute("SELECT SUM(covered_amount) as TotalCoveredAmount FROM events")
    except (mysql.connection.Error, mysql.connection.Warning) as e:
        print(e)  
    if resultTotalCoveredAmount > 0:
        resultTotalCoveredAmount= cur.fetchall()
        print(resultTotalCoveredAmount)
        return render_template("TotalCoveredAmount.html",resultTotalCoveredAmount=resultTotalCoveredAmount)
    return "Event Table is Empty: No Covered Amount Information"

@app.route("/ClaimsPerYear")
def ClaimsPerYear():
    cur= mysql.connection.cursor()
    try:
        resultClaimsPerYear= cur.execute("SELECT COUNT(*),YEAR(date_of_incidence)  FROM events GROUP BY YEAR(date_of_incidence) ")
    except (mysql.connection.Error, mysql.connection.Warning) as e:
        print(e)  
    if resultClaimsPerYear > 0:
        resultClaimsPerYear= cur.fetchall()
        print(resultClaimsPerYear)
        return render_template("ClaimsPerYear.html",resultClaimsPerYear=resultClaimsPerYear)
    return "Event Table is Empty: No Claims Information"
    


@app.route("/EventPerUser", methods=['GET','POST'])
def EventPerUser():
    if request.method== "POST":
        result=request.form
        user_id=result['user_id']
        cur = mysql.connection.cursor()
        try:
            try:
                EventPerUser= cur.execute("SELECT * FROM events where user_id = %s",[user_id])
            except:
                return None
            
            if EventPerUser > 0:
                EventPerUser= cur.fetchall()
                return render_template("EventPerUserDetails.html",EventPerUser=EventPerUser)
            return "User id does not esist"

        finally:
            cur.close()

    return render_template("EventPerUser.html")   


    
if __name__ == "__main__":
    app.run(debug=True)
