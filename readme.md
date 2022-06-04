conda create -n streamlite_app python=3.7 -y


conda activate streamlit_app2
pip install -r requirements.txt

streamlit run connection.py
streamlit run connect_mongo.py
streamlit run connect_mysql.py
