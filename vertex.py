from core.algoritmo import Algoritmo
from core.loader import Loader
from core.utils import Logger


def clustering(dataset_folder, dataset, window_size=10, hash_module=1024, threshold=26, input_limit=None):
	loader = Loader()
	pages = loader.load_pages(dataset_folder, dataset)
	pages = pages[:input_limit]

	logger = Logger.get_instance()
	logger.print('############### INITIALIZE PASS 1 ####################', 1)
	hash_table = {}
	algoritmo = Algoritmo()
	hash_table = algoritmo.pass1(pages, window_size, hash_module)

	logger.print('############### FINE PASS 1 ####################', 1)
	logger.print(hash_table, 3)

	logger.print('############### INITIALIZE PASS 2 ####################', 1)
	hash_table = algoritmo.pass2(hash_table, threshold)


	## TODO: testing pass1
	## TODO: testing pass2
	## TODO: testing pass3
  ## TODO: testing pass4
	## TODO: testing pass5
  ## TODO: da rivedere bene come fare gli hash che per ora sono fortemente dipendenti dal modulo che scegliamo, anche alla luce dei risultati che raggiungiamo

	logger.print('############### FINE PASS 2 ####################', 1)  
	logger.print(hash_table, 3)

	logger.print('############### INITIALIZE PASS 3 ####################', 1)
	cluster ={}
	cluster = algoritmo.pass3(hash_table, pages, hash_module, window_size)

	logger.print('################ FINE PASS 3 ####################', 1)
	
	logger.print('############### INITIALIZE PASS 4 ####################', 1)
	cluster ={}
	cluster = algoritmo.pass4(hash_table, pages, hash_module, window_size)

	logger.print('################ FINE PASS 4 ####################', 1)
	
	logger.print('############### INITIALIZE PASS 5 ####################', 1)
	cluster ={}
	cluster = algoritmo.pass5(hash_table, pages, hash_module, window_size)

	logger.print('################ FINE PASS 5 ####################', 1)
	
	logger.print('Numero cluster ' + str(len(cluster)), 2)
	logger.print('\nClusters: \n', 2)
	logger.print(cluster, 2)

	file = open("prediction.csv", "w")
	index_cluster = 0
	for key in cluster:
	    logger.print("\ncluster\n", 3)
	    for page in cluster[key]:
	        file.write(page.name + ", " + str(index_cluster) + "\n")
	    index_cluster += 1

	file.close()
