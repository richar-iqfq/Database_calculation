from utils.CalculatorAsyncV6 import MainCalculator

'''
Script that unifies the recovering of the data, the calculation of each b and
the corroboration of the convergence for the molecules 
'''

alpha = (-0.27)
calc_types = (0, 0, 0, 4, 0)

if __name__=='__main__':
    cores = 10
    tolerance = {
        'Ne_calc' : 1E-7,
        'Energy_S' : 1E-9,
        'Energy_Savrg' : 1E-9,
        'Recover' : 1E-9
    }

    database = 'log_files/extracted_data/data.csv'
    energies = 'log_files/extracted_data/energies.feather'

    output_path = f'a{alpha}_final-results'

    calculator = MainCalculator(output_path, calc_types=calc_types, cores=cores, tolerance=tolerance)
    calculator.run_optimization(database, energies, alpha)