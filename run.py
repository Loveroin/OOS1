#程序总入口

from App import app

app = app()

if __name__ == '__main__':
    # with app.app_context():
    #     db.create_all()
    app.run(host='0.0.0.0', port=8080, debug=True) 