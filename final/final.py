import urllib.request

url = "https://firebasestorage.googleapis.com/v0/b/skill-matrix-2a884.appspot.com/o/Arindam%20Lahiri%20Resume%20Aug%20'21.pdf?alt=media&token=07238b80-f27f-46b1-9091-7b771355612c"
file_name = "arindam.pdf"

urllib.request.urlretrieve(url, file_name)