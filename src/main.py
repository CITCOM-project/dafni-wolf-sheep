from wolf_sheep import model

wsmodel = model.WolfSheep(initial_sheep = 100, initial_wolves = 50, verbose = False)

wsmodel.run_model()

wsmodel_df = wsmodel.datacollector.get_model_vars_dataframe()

wsmodel_df.to_csv('wolf_sheep_out.csv')