#!/usr/bin/env python

from time import time
from mealpy.swarm_based.WOA import BaseWOA as WOA
from dotenv import dotenv_values

from fun import drop_wave

if __name__ == "__main__":
	config = dotenv_values(".env")

	a = float(config["A"])
	b = float(config["B"])
	epoch = int(config["GENERATIONS"])
	pop_size = int(config["POP_SIZE"])

	problem = {
		"obj_func": drop_wave,
		"lb": [a, a],
		"ub": [b, b],
		"minmax": "max",
		"verbose": True,
	}

	model = WOA(problem=problem, epoch=epoch, pop_size=pop_size)

	start_time = time()

	model.solve()

	end_time = time()

	print(f"Czas wykonania: {end_time-start_time}")
