from flask import Flask, render_template, request

import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
'''model = pickle.load(open('liver.pkl', 'rb'))'''

app = Flask(__name__)



@app.route('/')
def man():
    return render_template('home.html')


@app.route('/predict', methods=['POST'])
def home():
    d1 = request.form['age']
    d2 = request.form['no']
    d3 = request.form['tb']
    d4 = request.form['db']
    d5 = request.form['ap']
    d6 = request.form['aa']
    d7 = request.form['aam']
    d8 = request.form['tp']
    d9 = request.form['alb']
    d10= request.form['ag']

        
    
    
    arr = np.array([[float(d1), float(d2), float(d3), float(d4),float(d5),float(d6),float(d7),float(d8),float(d9),float(d10)]])
  
  
    df=pd.read_csv('D:\\Downloads\\indian_liver_patient.csv')
    df["Albumin_and_Globulin_Ratio"].fillna(df['Albumin_and_Globulin_Ratio'].mean(), inplace = True)
    X = df.iloc[:,:-1].values
    Y = df.iloc[:,-1].values
    for u in range(len(Y)):
        if Y[u] == 2:
            Y[u] = 0

    from sklearn.preprocessing import LabelEncoder
    lbl = LabelEncoder()
    X[:,1] = lbl.fit_transform(X[:,1])
    from sklearn.model_selection import train_test_split
    X_train, X_test, Y_train, Y_test = train_test_split(X,Y,random_state=18,test_size=0.25)

    from sklearn.preprocessing import StandardScaler
    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    X_test = sc.transform(X_test)
    
    from sklearn.linear_model import LogisticRegression

    logreg = LogisticRegression()

    logreg.fit(X_train, Y_train)
    p=sc.transform(arr);
    pred= logreg.predict(p)
    
  
    return render_template('after.html', data=pred)


if __name__ == "__main__":
    app.run(debug=True)















