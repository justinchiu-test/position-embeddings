import altair as alt
import pandas as pd
import numpy as np
import typer
from rich import print

app = typer.Typer()

def generate_sinusoid_data(velocities):
    t = np.linspace(0, 2*np.pi, 100)
    data = []
    for v in velocities:
        y = np.sin(v * t)
        for ti, yi in zip(t, y):
            data.append({"time": ti, "amplitude": yi, "velocity": v})
    return pd.DataFrame(data)

def create_sinusoid_chart(data):
    chart = alt.Chart(data).mark_line().encode(
        x='time',
        y='amplitude',
        color='velocity:N',
        tooltip=['velocity', 'time', 'amplitude']
    ).properties(
        width=600,
        height=400,
        title="Sinusoid with Varying Velocities"
    ).interactive()
    return chart

@app.command()
def visualize_sinusoid():
    """Visualize sinusoids with different velocities."""
    velocities = [0.5, 1.0, 1.5, 2.0]
    data = generate_sinusoid_data(velocities)
    chart = create_sinusoid_chart(data)
    chart.save("sinusoid_visualization.html")
    print("Visualization saved as 'sinusoid_visualization.html'")

if __name__ == "__main__":
    app()
import pandas as pd
import numpy as np
import typer
from rich import print
