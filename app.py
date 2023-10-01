import genetic_tsp
import aux
import flask

app = flask.Flask(__name__, static_folder="assets")

@app.route("/")
def index():
    return flask.render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    print("Generating...")

    if not flask.request.is_json:
        #do something here
        pass

    # absorb data
    data = flask.request.get_json()
    iterations = int(data["iter"])
    city_count = int(data["citycount"])
    mutation_rate = float(data["mutationrate"])
    population_size = int(data["populationsize"])
    k = int(data["kvalue"])
    seed = data["seed"]

    return flask.jsonify({
        "graph": genetic_tsp.initialize_and_plot(iterations, population_size, k, mutation_rate, city_count),
        "error": ""
    })



# Application entry point.
if __name__ == "__main__":
    is_debug_mode = "DEBUG_MODE" in os.environ
    logger = logging.getLogger("werkzeug")

    # Only log errors in the console.
    logger.setLevel(logging.ERROR)

    aux.log("Backend ready; awaiting requests")
    app.run(debug=is_debug_mode)
