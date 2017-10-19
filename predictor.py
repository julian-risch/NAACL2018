import warnings
warnings.filterwarnings(action="ignore", module="scipy", message="^internal gelsd")
import numpy as np
import pandas as pd
from sklearn.metrics import precision_recall_fscore_support
from scipy.sparse import hstack as sparse_hstack, csr_matrix, issparse
from numpy import hstack
from sklearn.preprocessing import normalize, MaxAbsScaler
from sklearn.metrics import mean_squared_error
from sklearn.metrics import accuracy_score
from classifier.svr import SVR
from classifier.linear_regression import LinearRegression
# from classifier.naive_bayes import NaiveBayes
from classifier.logistic_regression import LogisticRegression
import feature as Features

class Predictor:
    def fit(self, df):
        '''
        Generate the features from the dataframe and fit the classifiers.
        '''
        feature_matrix = self.calculate_feature_matrix(df)
        print("...using", feature_matrix.shape[1], "features from", ", ".join([feature[0] for feature in self.features]))
        learners = self.regressors if self._useRegression else self.classifier
        for learner in learners:
            learner[1].fit(feature_matrix, self.ground_truth(df))

    def predict(self, df):
        # Generate the features and predict the results.
        feature_matrix = self.calculate_feature_matrix(df)
        predictions = pd.DataFrame()
        learners = self.regressors if self._useRegression else self.classifier
        for learner in learners:
            predictions[learner[0]] = learner[1].predict(feature_matrix)

        self.regression_metrics(df, predictions) if self._useRegression else self.classification_metrics(df, predictions)
        # self.thresholded_regression_metrics(df, predictions, 0.8) if self._useRegression else self.classification_metrics(df, predictions)

        return predictions

    def thresholded_regression_metrics(self, df, predictions, threshold, metric='precision'):
        metrics = {}
        def normalize(x):
            return x / np.linalg.norm(x)
        for classifier in self.regressors:
            for i in range (1, 100):
                cutoff = i/100
                scores = precision_recall_fscore_support(
                    self.ground_truth(df),
                    normalize(predictions[classifier[0]]) > cutoff,
                    average='binary'
                )
                metrics[classifier[0]] = dict(zip(['precision', 'recall', 'f-score', 'support'], scores))
                metrics[classifier[0]]['accuracy'] = accuracy_score(self.ground_truth(df), normalize(predictions[classifier[0]]) > cutoff)
                if metrics[classifier[0]][metric] > threshold:
                    break
        self._metrics = metrics
        return metrics


    def classification_metrics(self, df, predictions):
        metrics = {}
        for classifier in self.classifier:
            scores = precision_recall_fscore_support(
                self.ground_truth(df),
                predictions[classifier[0]],
                average='binary'
            )
            metrics[classifier[0]] = dict(zip(['precision', 'recall', 'f-score', 'support'], scores))
            metrics[classifier[0]]['accuracy'] = accuracy_score(self.ground_truth(df), predictions[classifier[0]])

        self._metrics = metrics
        return metrics

    def regression_metrics(self, df, predictions):
        ground_truth = self.ground_truth(df)
        mean = np.mean(ground_truth)
        size = ground_truth.size
        metrics = {
            'dataset': {
                'mean': float("%.2f" % mean),
                'size': size,
                'rmse (avg)': float("%.2f" % mean_squared_error(ground_truth, np.ones((size, 1)) * mean) ** 0.5)
            }
        }
        for learner in self.regressors:
            metrics[learner[0]] = {
                # 'coef': learner[1].model.coef_ if learner[0] == 'linear_regression' else None,
                'rmse': float("%.2f" % mean_squared_error(ground_truth, predictions[learner[0]]) ** 0.5)
            }

        self._metrics = metrics
        return metrics

    def metrics(self):
        return self._metrics

    def set_target(self, column, useRegression):
        self._ground_truth = column
        self._useRegression = useRegression

    def ground_truth(self, df):
        return df[self._ground_truth]

    def calculate_feature_matrix(self, df):
        features = [feature[1].extract_features(df) for feature in self.features]
        has_sparse = False
        for feature in features:
            if issparse(feature):
                has_sparse = True
        # [print(f.shape) for f in features]
        if len(features) == 1:
            feature_matrix = features[0]
        else:
            if has_sparse:
                feature_matrix = sparse_hstack(features)
            else:
                feature_matrix = hstack(features)
        scaler = MaxAbsScaler()
        scaled_feature_matrix = scaler.fit_transform(feature_matrix)
        scaled_feature_matrix = normalize(scaled_feature_matrix, norm='l2', axis=0)
        return scaled_feature_matrix

    def __init__(self):
        self.features = [
            # ======== napoles ========
            # ('bow_features', Features.napoles.BowFeatures()),
            # ('embeddings_features', Features.napoles.EmbeddingsFeatures()),
            # ('entity_features', Features.napoles.EntityFeatures()),
            # ('length_features', Features.napoles.LengthFeatures()),
            # ('lexicon_features', Features.napoles.LexiconFeatures()),
            # ('popularity_features', Features.napoles.PopularityFeatures()),
            # ('pos_features', Features.napoles.POSFeatures()),
            # ('similarity_features', Features.napoles.SimilarityFeatures()),
            # ('user_features', Features.napoles.UserFeatures()),

            # ======== tsagkias ========
            ('surface_features', Features.tsagkias.SurfaceFeatures()),
            ('cumulative_features', Features.tsagkias.CumulativeFeatures()),
            ('real_world_features', Features.tsagkias.RealWorldFeatures()),
            ('semantic_features', Features.tsagkias.SemanticFeatures()),
            ('text_features', Features.tsagkias.TextFeatures()),

            # ========== own ===========
            ('t_density_features', Features.TDensityFeatures()),
            ('subjectivity_features', Features.SubjectivityFeatures()),
            ('word2vec', Features.Word2Vec()),
            ('ngram_features', Features.NGramFeatures()),
            ('doc2vec_features', Features.Doc2VecFeatures()),
            ('meta_features', Features.MetaFeatures()),
            ('topic_features', Features.TopicFeatures()),
            ('semantic_features', Features.SemanticFeatures()),
        ]

        self.classifier = [
            ('logistic regression', LogisticRegression()),
        ]

        self.regressors = [
            ('svr', SVR()),
            ('linear_regression', LinearRegression()),
        ]