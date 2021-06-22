from pathlib import Path
from wolf_sheep import model


# Initialise model
wsmodel = model.WolfSheep(initial_sheep = 100, initial_wolves = 50, verbose = False)


# Run model
wsmodel.run_model()


# Output .csv
wsmodel_df = wsmodel.datacollector.get_model_vars_dataframe()

output_folder = Path('/data/outputs/') # This starts at root so annoying if not in a container
output_folder.mkdir(parents=True, exist_ok=True)
output_file = output_folder.joinpath('wolf_sheep_out.csv')

wsmodel_df.to_csv(output_file)