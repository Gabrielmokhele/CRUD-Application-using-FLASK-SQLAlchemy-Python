from app import app, db, Employee

# Create the application context
app_ctx = app.app_context()
app_ctx.push()

# Now you can work with the database
db.create_all()


# Pop the application context
app_ctx.pop()

