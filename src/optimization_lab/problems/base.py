
class Problem:

    def __init__(self, n_var, n_obj, xl, xu):

        self.n_var = n_var
        self.n_obj = n_obj

        self.xl = xl
        self.xu = xu

    def evaluate(self, x):

        raise NotImplementedError(
            "Subclasses must implement evaluate()."
        )
