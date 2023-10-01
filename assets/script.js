
async function generate()
{
    const iter = document.getElementById("iterations").value;
    const citycount = document.getElementById("city-count").value;
    const mutationrate = document.getElementById("mutation-rate").value;
    const populationsize = document.getElementById("population-size").value;
    const kvalue = document.getElementById("k-value").value;
    const seed = document.getElementById("seed").value;

    document.getElementById("graph-img").alt = "Generating..."

    const response = await fetch("/generate", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({
            iter,
            citycount,
            mutationrate,
            populationsize,
            kvalue,
            seed
        })
    })

    if (!response.ok)
        throw new Error("Failed to fetch generation", response.status, response.statusText)

    const json = await response.json()

    if (!json.graph)
        throw new Error("Failed to fetch generation", "Response did not contain a graph")

    document.getElementById("graph-img").src = json.graph
}


const genbutton = document.getElementById("generate-button")
genbutton.addEventListener("click", generate);
