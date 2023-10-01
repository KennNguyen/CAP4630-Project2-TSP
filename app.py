from flask import Flask
import genetic_tsp
import aux

from flask import Flask

app = Flask(__name__)

@app.route("/")
def test():
    iterations = int(aux.query_user("How many iterations?", "1000"))
    city_count = int(aux.query_user("How many cities?", "20"))
    mutation_rate = float(aux.query_user("What mutation rate (float)?", "0.1"))
    population_size = int(aux.query_user("What population size?", "50"))
    k = int(aux.query_user("What k value?", "3"))
    seed = aux.query_user("What random seed?", "123456")

    #random.seed(seed)
    return genetic_tsp.initialize_and_plot(iterations, population_size, k, mutation_rate, city_count)

# Application entry point.
if __name__ == "__main__":
    is_debug_mode = "DEBUG_MODE" in os.environ
    logger = logging.getLogger("werkzeug")

    # Only log errors in the console.
    logger.setLevel(logging.ERROR)

    aux.log("Backend ready; awaiting requests")
    app.run(debug=is_debug_mode)
