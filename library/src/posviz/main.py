import altair as alt
import pandas as pd
import numpy as np
import typer
from rich import print
import math

app = typer.Typer()

def generate_rope_embedding(seq_len, dim, base=10000):
    embedding = []
    for pos in range(seq_len):
        pos_embedding = []
        for i in range(0, dim):
            theta = pos / (base ** (i / dim))
            pos_embedding.append(math.sin(theta))
        embedding.append(pos_embedding)
    return np.array(embedding)

def generate_sinusoid_data(velocities):
    t = np.linspace(0, 2*np.pi, 100)
    data = []
    for v in velocities:
        y = np.sin(v * t)
        for ti, yi in zip(t, y):
            data.append({"time": ti, "amplitude": yi, "velocity": v})
    return pd.DataFrame(data)

def create_chart(data, title):
    chart = alt.Chart(data).mark_line().encode(
        x='position:Q',
        y='value:Q',
        color='dimension:N',
        tooltip=['dimension', 'position', 'value']
    ).properties(
        width=600,
        height=400,
        title=title
    ).interactive()
    return chart

@app.command()
def visualize_sinusoid():
    """Visualize sinusoids with different velocities."""
    velocities = [0.5, 1.0, 1.5, 2.0]
    data = generate_sinusoid_data(velocities)
    chart = create_chart(data, "Sinusoid with Varying Velocities")
    chart.save("sinusoid_visualization.html")
    print("Visualization saved as 'sinusoid_visualization.html'")

@app.command()
def visualize_rope_embedding():
    """Visualize a few dimensions from rope embeddings."""
    seq_len = 128
    dim = 8 
    embedding = generate_rope_embedding(seq_len, dim)
    
    data = []
    for pos in range(seq_len):
        for d in range(dim):
            data.append({"position": pos, "value": embedding[pos][d], "dimension": f"dim_{d}"})
    
    df = pd.DataFrame(data)
    chart = create_chart(df, "Rope Embedding Visualization")
    chart.save("rope_embedding_visualization.html")
    print("Visualization saved as 'rope_embedding_visualization.html'")

if __name__ == "__main__":
    app()
