from bundle import myapp 

if __name__ == "__main__":
    server = myapp()
    server.run(port=5000, host='0.0.0.0', debug=True)