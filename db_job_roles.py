# process all jobs
import os
import psycopg2


def get_connection():
    
    connection = psycopg2.connect(host=os.getenv("PDBHOST"),
                                    user=os.getenv("PDBUSER"),
                                    password=os.getenv("PDBPASS"),
                                    dbname=os.getenv("PDBNAME"),
                                    port=os.getenv("PDBPORT"))

    return connection


def get_jobs_data():
    
    db = get_connection()
    cur = db.cursor()

    data = []
    
    #jobrole2jobtable
    #role_id, job_id
    #create table for job roles
    query = "select job_title, html_job_description, industry from jobs.job where industry != '' and html_job_description != '' and industry = 'Healthcare' limit 20"
    cur.execute(query)
    job_list = cur.fetchall()

    for row in job_list:
        data.append(row)

    cur.close()
    db.close()

    return data

def store_job_roles(predicted_job_roles):
    
    #predicted_job_roles
    print('predicted_job_roles')
    
    db = get_connection()
    cur = db.cursor()

    query = "update query"
    cur.execute(query)

    cur.close()
    db.close()
    
    
    return