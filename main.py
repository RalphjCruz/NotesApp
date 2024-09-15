from website import create_app

app = create_app()
                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
# This is auto rerun server when changes are made
if __name__ == '__main__':
    app.run(debug=True)