# from app import create_app

# app = create_app()

# if __name__ == "__main__":
#     app.run(host='0.0.0.0', port=5000, debug=True)

# import os
# from app import create_app

# app = create_app()

# if __name__ == "__main__":
#     app = create_app()
#     app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
#     # app.run(host="0.0.0.0", port=8080) 
#     app.run()


# import os
# from app import create_app

# app = create_app()

# if __name__ == "__main__":
#     # This is only for local testing
#     app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))


from app import create_app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True,port=8080)

# import os
# from flask import Flask

# app = Flask(__name__)

# @app.route("/")
# def home():
#     return "Hello from Flask on Fly!"

# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
