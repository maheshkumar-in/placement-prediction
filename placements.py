import pandas as pd
import streamlit as st
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split


#Step 1
#Loading the dataset:

df= pd.read_csv("C:\dataset1.csv")


#Step 2
#Data preproccessing

le=LabelEncoder()
stream=le.fit_transform(df['Stream'])
df["Stream"]=stream
x=df.pop("Stream")
df.insert(2,"Stream",x)


x=le.fit_transform(df["Gender"])
df.drop("Gender",axis=1,inplace=True)
df.insert(1,"Gender",x)

#Step 3
#Building our model

x_train,x_test,y_train,y_test=train_test_split(df[['Age','Gender','Stream','Internships','CGPA','HistoryOfBacklogs']],df.PlacedOrNot,test_size=0.2)
model=LogisticRegression()
model.fit(x_train,y_train)

y_pred=model.predict(x_test)


#Step 4
#Building Streamlit app
def fun():

	st.header("Placement prediction project")
	st.info("Enter all the details properly")

	age=st.number_input("Enter your age")
	gen=st.radio("Enter your gender",["male","female"])
	stream=st.radio("Enter your stream",["CSE","IT","ECE"])
	interns=st.number_input("Enter how many Internships did you do")
	cgpa=st.number_input("ENter your cgpa")
	back=st.number_input("Enter HistoryOfBacklogs")
	if gen == "male":
		gen=1
	else:
		gen=0

	if stream =="CSE":
		stream=1
	elif stream =="IT":
		stream=4
	elif stream=="ECE":
		stream=5
	else:
		stream=2


	li=[age,gen,stream,interns,cgpa,back]
	x=st.button("submit")
	if x:
		output=model.predict([li])
		if output==1:
			st.success("Youre in")
		else:
			st.error("Youre out")
fun()

