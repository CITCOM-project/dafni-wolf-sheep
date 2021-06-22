import os
from pathlib import Path
from wolf_sheep import model


# Initialise model
# Read values from environment variables but use default values if they don't exist
default_initial_sheep = 100
default_initial_wolves = 50

initial_sheep = int(os.getenv("initial_sheep", default_initial_sheep))
initial_wolves = int(os.getenv("initial_wolves", default_initial_wolves))

wsmodel = model.WolfSheep(initial_sheep = initial_sheep, 
                          initial_wolves = initial_wolves, 
                          verbose = False)


# Run model
wsmodel.run_model()


# Output .csv
wsmodel_df = wsmodel.datacollector.get_model_vars_dataframe()

output_folder = Path('/data/outputs/') # This starts at root so annoying if not in a container
output_folder.mkdir(parents=True, exist_ok=True)
output_file = output_folder.joinpath('wolf_sheep_out.csv')

wsmodel_df.to_csv(output_file)