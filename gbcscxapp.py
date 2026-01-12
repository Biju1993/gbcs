from jinja2 import Environment, PackageLoader, select_autoescape, FileSystemLoader
import os
import streamlit as st
from streamlit.components.v1 import iframe

#st.image("data:image/jpeg;base64,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")
st.title("DB COMMISSIONING REPORT GENERATOR")

env = Environment(loader=FileSystemLoader("."), autoescape=select_autoescape())
template = env.get_template("temp.html")

form = st.form("template_form")

v1= form.date_input("DATE OF INSPECTION")
v2 = form.text_input("ENTER PROJECT NAME")
v3 = form.text_input("ENTER DISTRIBUTION BOARD NAME")
form.subheader("PHYSICAL CHECKS")
v4= form.radio("PHYSICAL CONDITION OF PANEL GOOD NO DAMAGE EVIDENT",["YES", "NO","NA"],index=1,horizontal=True)
v5= form.radio("DIMENSION ARE AS PER DRAWING",["YES", "NO","NA"],index=1,horizontal=True)
v6= form.radio("PANELS CLEARLY LABELED",["YES", "NO","NA"],index=1,horizontal=True)
form.subheader("DESIGN VERIFICATION")
v7= form.radio("POWER & CIRCUIT WIRING / CABLING AS PER DESIGN ",["YES", "NO","NA"],index=1,horizontal=True)
v8= form.radio("All BREAKER RATINGS AS PER DRAWINGS",["YES", "NO","NA"],index=1,horizontal=True)
v9= form.radio("ALL CABLE SIZES AS PER DRAWINGS",["YES", "NO","NA"],index=1,horizontal=True)
v10= form.radio("SIZE OF THE EARTHING CABLES / BUS BARS IS AS PER DESIGN",["YES", "NO","NA"],index=1,horizontal=True)
v11= form.radio("ALL THE PANEL INDICATIONS & METERING  IS AS PER THE DESIGN",["YES", "NO","NA"],index=1,horizontal=True)
v12= form.radio("CONTROL CIRCUIT AS PER DESIGN INTENT",["YES", "NO","NA"],index=1,horizontal=True)
form.subheader("INSTALLATION CHECKS")
v13= form.radio("PROPER CONNECTION & TERMINATION OF CABLES DONE",["YES", "NO","NA"],index=1,horizontal=True)
v14= form.radio("MECHANICAL OPERATION OF BREAKERS VERIFIED",["YES", "NO","NA"],index=1,horizontal=True)
v15= form.radio("EARTHING CONNECTIONS IN/FOR PANEL DONE PROPERLY",["YES", "NO","NA"],index=1,horizontal=True)
v16= form.radio("ALL CONNECTIONS TIGHTENED",["YES", "NO","NA"],index=1,horizontal=True)
v17= form.radio("ALL THE LABELS / TAGS IN PLACE",["YES", "NO","NA"],index=1,horizontal=True)
v18= form.radio("CONNECTION TIGHTNESS VERIFIED WITH A TORQUE WRENCH",["YES", "NO","NA"],index=1,horizontal=True)
v19= form.radio("ELECTRICAL /  MECHANICAL INTERLOCK VERIFIED FOR OPERATION",["YES", "NO","NA"],index=1,horizontal=True)
form.subheader("FUNCTIONAL CHECKS ")
v20= form.radio("MILLIVOLT DROP TEST CONDUCTED",["YES", "NO","NA"],index=1,horizontal=True)
v21= form.radio("PERMANENT POWER SOURCE AVAILABLE",["YES", "NO","NA"],index=1,horizontal=True)
v22= form.radio("INDICATION LAMPS OPERATION",["YES", "NO","NA"],index=1,horizontal=True)
v23= form.radio("ON / OFF OPERATION OF BREAKER",["YES", "NO","NA"],index=1,horizontal=True)
v24= form.radio("INTERLOCK VERIFIED",["YES", "NO","NA"],index=1,horizontal=True)
v25= form.radio("I/C & O/G CONTINUITY TEST",["YES", "NO","NA"],index=1,horizontal=True)
v26= form.radio("PHASE SEQUENCE VERIFIED",["YES", "NO","NA"],index=1,horizontal=True)
v27= form.radio("METERING ARRANGEMENT VERIFIED FOR ITS OPERATION",["YES", "NO","NA"],index=1,horizontal=True)

submit = form.form_submit_button("GENERATE REPORT")

if submit:
    html = template.render(V1=v1,
V2=v2,
V3=v3,
V4=v4,
V5=v5,
V6=v6,
V7=v7,
V8=v8,
V9=v9,
V10=v10,
V11=v11,
V12=v12,
V13=v13,
V14=v14,
V15=v15,
V16=v16,
V17=v17,
V18=v18,
V19=v19,
V20=v20,
V21=v21,
V22=v22,
V23=v23,
V24=v24,
V25=v25,
V26=v26,
V27=v26
)
    with open("report.html", "w") as f:
        f.write(html)
    f.close()

    st.download_button("⬇️ Download Report",data=html,file_name=v3+".html") 
