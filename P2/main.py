import timeit

from src import run_experiment
from models import custom_models_base
from load_dataset import SurrData

if __name__ == '__main__':
    general_results_dir = '/Volumes/SamDick/Grad Project/temp/results'

    tot0 = timeit.default_timer()
    run_experiment.DoExperiment(descriptor='SurrData-test',
                                general_results_dir=general_results_dir,
                                custom_net=custom_models_base.TestSurr,
                                custom_net_args={},
                                learning_rate=1e-2,  # default 1e-3
                                weight_decay=1e-7,  # default 1e-7
                                num_epochs=30, patience=10,
                                batch_size=1, debug=True,
                                use_test_set=False, task='train_eval',
                                old_params_dir='',
                                chosen_dataset=SurrData.SurrData,
                                chosen_dataset_args={})
    tot1 = timeit.default_timer()
    print('Total Time', round((tot1 - tot0) / 60.0, 2), 'minutes')
