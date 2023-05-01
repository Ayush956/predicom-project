from django.shortcuts import render
import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
import numpy as np
from login.views import f

def home(request):
    name = f(request)
    status = False
    if name!=None:
        status = True
    data = {
        'name':name,
        'status':status
    }
    print(name)
    return render(request,"home.html",data)

def services(request):
    return render(request ,"services.html")

def car(request):
    data = pd.read_csv("C:\\Users\\ayush\\OneDrive\\Desktop\\data structure\\car.csv")
    data.replace({"fuel":{"Petrol":0,"Diesel":1,"CNG":2,"LPG":3,"Electric":4}},inplace = True)
    data.replace({"transmission":{"Manual":0,"Automatic":1}},inplace = True)
    data.replace({"owner":{"First Owner":0,"Second Owner":1,"Third Owner":2,"Fourth & Above Owner":3,"Test Drive Car":4}},inplace = True)
    X = data.drop(["selling_price","name","seller_type"],axis=1)
    Y = data["selling_price"]
    X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.30)
    model =LinearRegression()
    model.fit(X_train,Y_train)

    d = {}
    isActive = False
    var1 = (request.GET.get("n1"))
    var2 = (request.GET.get("n2"))
    var3 = (request.GET.get("n3"))
    var4 = (request.GET.get("n4"))
    var5 = (request.GET.get("n5"))
    if var1!=None:
        var1=float(var1)
        var2=float(var2)
        var3=float(var3)
        var4=float(var4)
        var5=float(var5)
        pred = model.predict(np.array([var1,var2,var3,var4,var5]).reshape(1,-1))
        pred = round(pred[0])
        isActive = True
    

        d = {
            "pred":pred,
            "isActive":isActive
        }
    
    return render(request,"products/car.html",d)

def mobile(request):
    data = pd.read_csv("C:\\Users\\ayush\\OneDrive\\Desktop\\data structure\\mobile.csv")
    data.replace({"Brand":{"Samsung":0,"Xiaomi":1,"Oppo":2,"Realme":3,"Vivo":4,"Apple":5,"Nokia":6,"Motorola":7,"OnePlus":8,"Huawei":9,"Google":10,"Asus":11,"LG":12,"Blackberry":13,"Sony":14,"CAT":15}},inplace = True)
    X = data.drop(("Price"),axis=1)
    Y = data["Price"]
    X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.30)
    model =LinearRegression()
    model.fit(X_train,Y_train)
    d = {}
    isActive = False
    var1 = (request.GET.get("n1"))
    var2 = (request.GET.get("n2"))
    var3 = (request.GET.get("n3"))
    var4 = (request.GET.get("n4"))
    var5 = (request.GET.get("n5"))
    if var1!=None:
        var1=float(var1)
        var2=float(var2)
        var3=float(var3)
        var4=float(var4)
        var5=float(var5)
        pred = model.predict(np.array([var1,var2,var3,var4,var5]).reshape(1,-1))
        pred = round(pred[0])
        if pred>300:
            pred=pred-200
        pred=pred*72
        isActive = True
    

        d = {
            "pred":pred,
            "isActive":isActive
        }
    return render(request,"products/mobile.html",d)

def house(request):

    data = pd.read_csv("C:\\Users\\ayush\\OneDrive\\Desktop\\data structure\\USA_Housing.csv")
    # data.head()
    data = data.drop(["Address"],axis=1)
    X = data.drop(["Price"],axis=1)
    Y = data["Price"]
    X_train,X_test,Y_train,Y_test  = train_test_split(X,Y,test_size =.30)
    model = LinearRegression()
    model.fit(X_train,Y_train)
    # np.isnan(X.values.any())
    d = {}
    isActive = False
    var1 = (request.GET.get("n1"))
    var2 = (request.GET.get("n2"))
    var3 = (request.GET.get("n3"))
    var4 = (request.GET.get("n4"))
    var5 = (request.GET.get("n5"))
    if var1!=None:
        var1=float(var1)
        var2=float(var2)
        var3=float(var3)
        var4=float(var4)
        var5=float(var5)
        pred = model.predict(np.array([var1,var2,var3,var4,var5]).reshape(1,-1))
        pred = round(pred[0])
        pred=pred*72
        isActive = True
    

        d = {
            "pred":pred,
            "isActive":isActive
        }
    return render(request,"products/house.html",d)

def laptop(request):
    data = pd.read_csv("C:\\Users\\ayush\\OneDrive\\Desktop\\data structure\\laptop.csv")
    data.replace({"Company":{"Dell":0,"Lenovo":1,"HP":2,"Asus":3,"Acer":4,"MSI":5,"Toshiba":6,"Apple":7,"Samsung":8,"Razer":9,"Mediacom":10,"Microsoft":11,"Xiaomi":12,"Vero":13,"Chuwi":14,"Google":15,"Fujitsu":16,"LG":17,"Huawei":18}},inplace = True)
    data.replace({"TypeName":{"Notebook":0,"Gaming":1,"Ultrabook":2,"2 in 1 Convertible":3,"Workstation":4,"Netbook":5}},inplace = True)
    data.replace({"OpSys":{"Windows":0,"No OS":1,"Linux":2,"Chrome OS":3,"macOS":4,"Mac OS X":5,"Android":6}},inplace = True)
    X = data.drop(["Price"],axis=1)
    Y = data["Price"]
    X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.30)
    model =LinearRegression()
    model.fit(X_train,Y_train)
    d = {}
    isActive = False
    var1 = (request.GET.get("n1"))
    var2 = (request.GET.get("n2"))
    var3 = (request.GET.get("n3"))
    var4 = (request.GET.get("n4"))
    var5 = (request.GET.get("n5"))
    var6 = (request.GET.get("n6"))
    var7 = (request.GET.get("n7"))
    if var1!=None:
        var1=float(var1)
        var2=float(var2)
        var3=float(var3)
        var4=float(var4)
        var5=float(var5)
        var6=float(var6)
        var7=float(var7)
        pred = model.predict(np.array([var1,var2,var3,var4,var5,var6,var7]).reshape(1,-1))
        pred = round(pred[0])
        isActive = True
    

        d = {
            "pred":pred,
            "isActive":isActive
        }
    return render(request,"products/laptop.html",d)

def service(request):
    return render(request,"service.html")

def about(request):
    return render(request,"about.html")
