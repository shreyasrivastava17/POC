from flask import Flask, request, redirect, render_template
import sys
import simplejson
import time
from flask_cors import CORS, cross_origin
from functions.sqlquery import sql_query2, sql_edit_insert, sql_query

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
customer_cache=[]
start_time=time.time()
 

@app.route('/GetCustomerNames')
@cross_origin()
def GetCustNames():
    cust_list=[]
    customers = sql_query(''' SELECT * FROM Customers''')
    for result in customers:
        result_dict={
            'ID': result['id'],
            'Name':result['Name'],
            'firebaseid':result['firebase_id'],
            'IsSignificant':result['IsSignificant'],
            'mobile number': result['mobile']
        }
        cust_list.append(result_dict)

    return simplejson.dumps(cust_list)

@app.route('/')
def sql_database():

    global customer_cache
    global start_time
    count=0
    while(True):
        # print(count)
        result_list=[]
        extra_cust=[]
        flag=False
            # if((time.time() - start_time)/(1000*60*60) >3 ):
        print((time.time() - start_time))
        if((time.time() - start_time) >5555):
            # print("*********************customer cache")
            customer_cache = []
            start_time = time.time()

        # print("ok")
        fname=["akshata","shreya"]

        #for testing purposes
        
        if(time.time() - start_time>5):
            fname.append("POPO")


        # print(customer_cache)
        for name in fname:
            if(name not in customer_cache):
                flag=True
                # print("name*****************",name)
                extra_cust.append(name)

        # print("extra cust******",extra_cust)

        if(flag==True):
            # print("***************DB CALL********************")
            results = sql_query2(''' SELECT person_id, first_name,last_name,firebase_id,IsSignificant,mobile FROM Customers_master where first_name in (%s)'''% ','.join('?'*len(extra_cust)),extra_cust)
            count+=1
           
            # print("Result*****",results)
            if(len(results)==0):
                for name in extra_cust:
                    customer_cache.append(name)

            for result in results:

                result_dict={
                    'ID': result['person_id'],
                    'firstname':result['first_name'],
                    'lastname':result['last_name'],
                    'firebaseid':result['firebase_id'],
                    'IsSignificant':result['IsSignificant'],
                    'mobile number': result['mobile']
                }
                if(len(customer_cache)==0):
                    start_time = time.time()
                customer_cache.append(result['first_name'])
                result_list.append(result_dict)
                name = result_dict['firstname'] + result_dict['lastname']
                sql_edit_insert(''' INSERT INTO Customers (id,Name,IsSignificant,firebase_id, mobile) VALUES (?,?,?,?,?)''', (result_dict['ID'],name, result_dict['IsSignificant'], result_dict['firebaseid'], result_dict['mobile number']))
                extra_cust = []
            #firebase
        # return "str"
            # return simplejson.dumps(result_list)



if __name__ == "__main__":
    app.run(debug=True)











