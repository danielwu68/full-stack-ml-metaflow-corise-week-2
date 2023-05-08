
from metaflow import FlowSpec, step, card, current
from metaflow.cards import Markdown, Table

class Branch_Flow(FlowSpec):
    """
    train multiple tree based methods
    """
    @card 
    @step
    def start(self):
        """
        Load the data
        """
        #Import scikit-learn dataset library
        from sklearn import datasets

        #Load dataset
        self.iris = datasets.load_iris()
        self.X = self.iris['data']
        self.y = self.iris['target']
        self.next(self.rf_model, self.xt_model, self.dt_model)
    
                
    @step
    def rf_model(self):
        """
        build random forest model
        """
        from sklearn.ensemble import RandomForestClassifier
        from sklearn.model_selection import cross_val_score
        
        self.clf = RandomForestClassifier(n_estimators=10, max_depth=None,
            min_samples_split=2, random_state=0)
        self.scores = cross_val_score(self.clf, self.X, self.y, cv=5)
        self.next(self.choose_model)

    @step
    def xt_model(self):
        """
        build extra trees classifier
        """
        from sklearn.ensemble import ExtraTreesClassifier
        from sklearn.model_selection import cross_val_score
        

        self.clf = ExtraTreesClassifier(n_estimators=10, max_depth=None,
            min_samples_split=2, random_state=0)

        self.scores = cross_val_score(self.clf, self.X, self.y, cv=5)
        self.next(self.choose_model)

    @step
    def dt_model(self):
        """
        build decision tree classifier
        """
        from sklearn.tree import DecisionTreeClassifier
        from sklearn.model_selection import cross_val_score
        
        self.clf = DecisionTreeClassifier(max_depth=None, min_samples_split=2,
            random_state=0)

        self.scores = cross_val_score(self.clf, self.X, self.y, cv=5)

        self.next(self.choose_model)

    @card                 
    @step
    def choose_model(self, inputs):
        """
        find 'best' model
        """
        import numpy as np

        def score(inp):
            return inp.clf,\
                   np.mean(inp.scores)

            
        current.card.append(Markdown('# Choose Model'))
        self.results = sorted(map(score, inputs), key=lambda x: -x[1]) 
        self.model = self.results[0][0]
        current.card.append(Markdown(f'## Best Model: {self.results[0][0]}'))
        current.card.append(Markdown('## Results:'))
        rows = [ f"- {model} - {score}" for model, score in self.results]
        print(rows)
        for r in rows:
            current.card.append(Markdown(r))

        self.next(self.end)

        
    @step
    def end(self):
        """
        End of flow!
        """
        print('Scores:')
        print('\n'.join('%s %f' % res for res in self.results))
        print('Best model:')
        print(self.model)


if __name__ == "__main__":
    Branch_Flow()
