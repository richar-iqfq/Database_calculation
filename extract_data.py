from utils.Extractor import Extractor
from utils.TerminationChecker import TerminationChecker

if __name__=='__main__':
    '''
    Extract and unify data in one csv file
    '''

    # input_path = 'full_dissociation_log_files'
    # input_path = 'new_full_from_gen_dissociation_files'
    input_path = 'dissociation_log_H2'
    output_path = 'extracted_data'

    t_checker = TerminationChecker(input_path)
    t_checker.check(move=True)

    mb = Extractor(input_path, output_path)
    mb.extract(force=True)
