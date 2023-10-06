from flask import (
    Flask,
    jsonify,
    render_template,
    request,
    redirect,
    url_for,
    session,
    flash,
)

app = Flask(__name__, static_url_path="/static")
app.secret_key = "your_secret_key"

users = {"jamie@lego.ie": "123"}

my_menu = [
    {
        "name": "Rendang Beef & Sweet Potato Curry",
        "image": "static/images/meals/Rendang_Beef.jpg",
        "time": 30,
        "description": "Packed with ingredients like coconut, coriander,giner and fresh shallot. Rendang is considered a dryer curry which as the suace is simmered down. With a wide cvariety of spices makes it healthy",
        "calories": 850,
        "carbohydrates": 79,
        "protein": 16,
        "fat": 53,
        "allergens": "none",
        "plans": "family",
    },
    {
        "name": "Beef & Vegetable Stir-fry with Hokkien Noodles",
        "image": "static/images/meals/Beef_stirfry.jpg",
        "time": 30,
        "description": "A Classic Asian dish with pre-cut irish beef makes for a tasty and quick stir-fry. This dish is packed with veggies which makes for a colorful and crunchy meal",
        "calories": 409,
        "carbohydrates": 25,
        "protein": 36,
        "fat": 15,
        "allergens": "Sesame Seeds, Wheat, Egg",
        "plans": "family",
    },
    {
        "name": "Chicken Satay with Basmati Rice & Fresh Cucumber",
        "image": "static/images/meals/Chicken_satay.jpg",
        "time": 30,
        "description": "Thai-inspired chicken skewers are marinated in a delicous, spicy peanut sauce, then grilled and served with a satay saice with coconut milk and garlic sauce",
        "calories": 519,
        "carbohydrates": 33,
        "protein": 45,
        "fat": 23,
        "allergens": "Peanuts, Gluten",
        "plans": "classic",
    },
    {
        "name": "Pulled Chicken Burgers with Corn",
        "image": "static/images/meals/Pulled_chickn.jpg",
        "time": 30,
        "description": "These Mexican-inspired chicken burgers are an absolute hit, Fresh and simple. Sizzling honey chicken, tomato puree allows for caramalization creating a fantastic, sticky sauce",
        "calories": 850,
        "carbohydrates": 79,
        "protein": 16,
        "fat": 53,
        "allergens": "none",
        "plans": "family",
    },
    {
        "name": "Halloumi Fajita Traybake",
        "image": "static/images/meals/Halloumi_Traybake.jpg",
        "time": 30,
        "description": "This recipe is as simple as it comes with a punnch of flavours. Packed with vegetables and halloumi this is a serious contender for dinner",
        "calories": 476,
        "carbohydrates": 44,
        "protein": 24,
        "fat": 24,
        "allergens": "Gluten (Tortilla)",
        "plans": "plant-based",
    },
    {
        "name": "Shredded Hoisin Chicken Wraps",
        "image": "static/images/meals/Chicken_Hoisen.jpeg",
        "time": 30,
        "description": "A healthy alternative to chinese takeaway. This makes for a great mid-week meal. Topped with crunchy fresh veg, these wraps are packed with protein and low in fat",
        "calories": 550,
        "carbohydrates": 60,
        "protein": 36,
        "fat": 12,
        "allergens": "Gluten(wraps), Soy, Sesame seeds",
        "plans": "classic",
    },
    {
        "name": "Mushroom & Green Bean Stroganoff with Basmati Rice",
        "image": "static/images/meals/mushroom_stroganoff.jpg",
        "time": 30,
        "description": "Famous dish of Russian origin with a twist to make it both meat and gluten free. The stroganoff saice is made with natural yogurt, smoked paprika, rosemary and fresh taragon, served with basmati rice",
        "calories": 227,
        "carbohydrates": 42,
        "protein": 12,
        "fat": 2,
        "allergens": "Milk",
        "plans": "plant-based",
    },
    {
        "name": "Vegetable Korma & Rice",
        "image": "static/images/meals/Veg_Korma.jpg",
        "time": 30,
        "description": "Packed with ingredients like coconut, coriander,giner and fresh shallot. Rendang is considered a dryer curry which as the suace is simmered down. With a wide cvariety of spices makes it healthy",
        "calories": 850,
        "carbohydrates": 79,
        "protein": 16,
        "fat": 53,
        "allergens": "none",
        "plans": "plant-based",
    },
    {
        "name": "Rendang Beef & Sweet Potato Curry",
        "image": "static/images/meals/Rendang_Beef.jpg",
        "time": 30,
        "description": "A super easy one pot meal which requires minimal wahsing up. This mild and healthy dish will be a winner for the whole family",
        "calories": 524,
        "carbohydrates": 96,
        "protein": 18,
        "fat": 6,
        "allergens": "GLuten, Dairy ",
        "plans": "family",
    },
    {
        "name": "Honey & Lime Hallumi Tacos with Beans & Mango Salsa ",
        "image": "static/images/meals/Tacos.jpg",
        "time": 30,
        "description": "The minty mango salsk makes this dish feel so light and refreshing as well as packing a seriosu hit of vitamin C. Black beans adding antioxidants and fibre",
        "calories": 539,
        "carbohydrates": 58,
        "protein": 33,
        "fat": 13,
        "allergens": "Wheat, Dairy",
        "plans": "plant-based",
    },
    {
        "name": "Cherry Tomato Linguine with Cajun Grilled Chicken",
        "image": "static/images/meals/Linguine_chicken.jpg",
        "time": 30,
        "description": "Healthy, yet tastes like a treat. The pasta cooks in its own sauce giving it a luscious, flavoursome base complimented by the cikc from the cajun chicken",
        "calories": 500,
        "carbohydrates": 40,
        "protein": 17,
        "fat": 6,
        "allergens": "Dairy, Gluten",
        "plans": "family",
    },
    {
        "name": "One Pot Chicken Quinoa Balti",
        "image": "static/images/meals/Quinoa_Balti.jpg",
        "time": 30,
        "description": "High protein meal to get you through a workout. Great source of protein and fibre, making it nutritous",
        "calories": 524,
        "carbohydrates": 64,
        "protein": 40,
        "fat": 7,
        "allergens": "Nuts, Egg",
        "plans": "classic",
    },
]


# Defining routes for the different HTML pages
@app.route("/")
def home():
    return render_template("index.html", menu=my_menu)


@app.route("/about")
def about():
    return render_template("about.html", menu=my_menu)


@app.route("/menu")
def menu():
    return render_template("menu.html", menu=my_menu)


@app.route("/works")
def works():
    return render_template("works.html")


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/register")
def register():
    return render_template("register.html")


@app.route("/cart")
def cart():
    return render_template("cart.html")


@app.route("/checkout")
def checkout():
    return render_template("checkout.html")


def process_form_data(
    full_name,
    email,
    address,
    city,
    state,
    zip_code,
    card_number,
    exp_month,
    exp_year,
    cvv,
):
    # Process and store the form data as needed
    print(
        f"Processing Form Data: {full_name}, {email}, {address}, {city}, {state}, {zip_code}, {card_number}, {exp_month}, {exp_year}, {cvv}"
    )


@app.route("/checkout", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Access form data
        full_name = request.form.get("full_name")
        email = request.form.get("email")
        address = request.form.get("address")
        city = request.form.get("city")
        state = request.form.get("state")
        zip_code = request.form.get("zip_code")
        card_number = request.form.get("card_number")
        exp_month = request.form.get("exp_month")
        exp_year = request.form.get("exp_year")
        cvv = request.form.get("cvv")

        # Process form data using the function
        process_form_data(
            full_name,
            email,
            address,
            city,
            state,
            zip_code,
            card_number,
            exp_month,
            exp_year,
            cvv,
        )

    return render_template("checkout.html")


@app.route("/login_validation", methods=["POST"])
def login_validation():
    email = request.form.get("email")
    password = request.form.get("password")

    # to check if the email provided matches
    if email in users and users[email] == password:
        session["user_email"] = email
        return render_template("menu.html")
    else:
        flash("Username or Password is incorrect")
        return render_template("login.html")


@app.route("/add_user", methods=["POST"])
def add_user():
    name = request.form.get("uname")
    email = request.form.get("uemail")
    password = request.form.get("upassword")
    repassword = request.form.get("urepassowrd")
    # if email in users:
    #     return "Email already exists. Please use a different email"
    # # Adding a new user to the database
    # users[email] = password
    # return redirect("/login")
    if email in users:
        flash("Email already exists. Please use a different email.", "error")
        return redirect("/register")

    if password != repassword:
        flash("Passwords do not match. Please try again.", "error")
        return redirect("/register")
    users[email] = password

    flash("Registration successful!", "success")
    return redirect("/login")


@app.route("/logout")
def logout():
    session.pop("email", None)
    return redirect("/login")


if __name__ == "__main__":
    app.run(debug=True, port=8080)
