import numpy as np
from feature.features import Features

class ZeitFeatures(Features):
  def __init__(self):
    super().__init__('carl/zeit_features')

  def _extract_features(self, df):
    features = [
        df['shared_on_facebook'],



        # df['urgent'] == 'yes',
        # df['product-id'] == 'ZEDE',
        # df['product-id'] == 'ZEI',
        # df['product-id'] == 'ZECW',
        # df['product-id'] == 'TGS',
        # df['edited'] == 'yes',
        # df['copyrights'].str.contains('dpa'),
        # df['copyrights'].str.contains('Reuters'),
        # df['copyrights'].str.contains('afp'),
        # df['copyrights'].str.contains('AFP'),
        # df['copyrights'].str.contains('ZEIT ONLINE'),
        # df['copyrights'].str.contains('sk'),
        # df['copyrights'].str.contains('sah'),
        # df['copyrights'].str.contains('tst'),
        # df['copyrights'].str.contains('fst'),
        # df['copyrights'].str.contains('fa'),
        # df['copyrights'].str.contains('aba'),
        # df['copyrights'].str.contains('nsc'),
        # df['copyrights'].str.contains('kp'),
        # df['copyrights'].str.contains('stü'),
        # df['copyrights'].str.contains('cz'),
        # df['copyrights'].str.contains('sre'),
        # df['copyrights'].str.contains('spo'),
        # df['copyrights'].str.contains('mm'),
        # df['lead_candidate'] == 'yes',
        # df['lead_candidate'] == 'no',
        # df['is_instant_article'] == 'yes',
        # df['is_instant_article'] == 'no',
        # df['is_amp'] == 'yes',
        # df['is_amp'] == 'no',
        # df['has_recensions'] == 'yes',
        # df['export_cds'] == 'yes',
        # df['comments_premoderate'] == 'no',
        # df['corrected'] == 'yes',
        # df['breaking_news'] == 'yes',
        # df['banner_content'] == 'yes',
        # df['DailyNL'] == 'yes',


        # channels features
        # df['channels'].str.contains('Ausland'),
        # df['channels'].str.contains('Beruf'),
        # df['channels'].str.contains('Campus'),
        # df['channels'].str.contains('Chancen'),
        # df['channels'].str.contains('Community'),
        # df['channels'].str.contains('Datenschutz'),
        # df['channels'].str.contains('Deutschland'),
        # df['channels'].str.contains('Digital'),
        # df['channels'].str.contains('English'),
        # df['channels'].str.contains('Entdecken'),
        # df['channels'].str.contains('essen-trinken'),
        # df['channels'].str.contains('Familie'),
        # df['channels'].str.contains('Film'),
        # df['channels'].str.contains('fussball'),
        # df['channels'].str.contains('Games'),
        # df['channels'].str.contains('Geld'),
        # df['channels'].str.contains('Geldanlage'),
        # df['channels'].str.contains('Geschichte'),
        # df['channels'].str.contains('Gesellschaft'),
        # df['channels'].str.contains('Gesundheit'),
        # df['channels'].str.contains('Hamburg'),
        # df['channels'].str.contains('HH-Newsletter'),
        # df['channels'].str.contains('Hochschule'),
        # df['channels'].str.contains('Internet'),
        # df['channels'].str.contains('Karriere'),
        # df['channels'].str.contains('Kultur'),
        # df['channels'].str.contains('kultur'),
        # df['channels'].str.contains('KulturUndGesellschaft'),
        # df['channels'].str.contains('Kunst'),
        # df['channels'].str.contains('leben'),
        # df['channels'].str.contains('Literatur'),
        # df['channels'].str.contains('Mobil'),
        # df['channels'].str.contains('Mobilitaet'),
        # df['channels'].str.contains('mode-design'),
        # df['channels'].str.contains('Musik'),
        # df['channels'].str.contains('Politik'),
        # df['channels'].str.contains('politik-wirtschaft'),
        # df['channels'].str.contains('Reisen'),
        # df['channels'].str.contains('Schule'),
        # df['channels'].str.contains('Sport'),
        # df['channels'].str.contains('stadtleben'),
        # df['channels'].str.contains('Studium'),
        # df['channels'].str.contains('Umwelt'),
        # df['channels'].str.contains('Unternehmen'),
        # df['channels'].str.contains('Wirtschaft'),
        # df['channels'].str.contains('Wissen'),
        # df['channels'].str.contains('zeit-magazin'),
        # df['channels'].str.contains('Zeitgeschehen'),

        # subressort features
        # df['sub_ressort'] == 'Ausland',
        # df['sub_ressort'] == 'Beruf',
        # df['sub_ressort'] == 'Bewerbung',
        # df['sub_ressort'] == 'Boerse',
        # df['sub_ressort'] == 'Datenschutz',
        # df['sub_ressort'] == 'Deutschland',
        # df['sub_ressort'] == 'Familie',
        # df['sub_ressort'] == 'Film',
        # df['sub_ressort'] == 'Games',
        # df['sub_ressort'] == 'Geldanlage',
        # df['sub_ressort'] == 'Geschichte',
        # df['sub_ressort'] == 'Gesundheit',
        # df['sub_ressort'] == 'Hochschule',
        # df['sub_ressort'] == 'Internet',
        # df['sub_ressort'] == 'Kunst',
        # df['sub_ressort'] == 'Literatur',
        # df['sub_ressort'] == 'Mobil',
        # df['sub_ressort'] == 'Mode',
        # df['sub_ressort'] == 'Musik',
        # df['sub_ressort'] == 'Partnerschaft',
        # df['sub_ressort'] == 'Rankings',
        # df['sub_ressort'] == 'Reisen',
        # df['sub_ressort'] == 'Schule',
        # df['sub_ressort'] == 'Studiengaenge',
        # df['sub_ressort'] == 'Umwelt',
        # df['sub_ressort'] == 'Uni-Leben',
        # df['sub_ressort'] == 'Unternehmen',
        # df['sub_ressort'] == 'Zeitgeschehen',
        # df['sub_ressort'] == 'essen-trinken',
        # df['sub_ressort'] == 'fussball',
        # df['sub_ressort'] == 'kultur',
        # df['sub_ressort'] == 'leben',
        # df['sub_ressort'] == 'mode-design',
        # df['sub_ressort'] == 'politik-wirtschaft',
        # df['sub_ressort'] == 'stadtleben',
        # df['sub_ressort'] == 'unknown',

        # ressort features
        # df['ressort'] == 'Campus',
        # df['ressort'] == 'Chancen',
        # df['ressort'] == 'Community',
        # df['ressort'] == 'Digital',
        # df['ressort'] == 'Dossier',
        # df['ressort'] == 'Entdecken',
        # df['ressort'] == 'Feuilleton',
        # df['ressort'] == 'Fussball',
        # df['ressort'] == 'Geschichte',
        # df['ressort'] == 'Gesellschaft',
        # df['ressort'] == 'Glauben und Zweifeln',
        # df['ressort'] == 'Hamburg',
        # df['ressort'] == 'Karriere',
        # df['ressort'] == 'KinderZEIT',
        # df['ressort'] == 'Kultur',
        # df['ressort'] == 'Literatur Spezial',
        # df['ressort'] == 'Mobilitaet',
        # df['ressort'] == 'Politik',
        # df['ressort'] == 'Politik\n      ÖSTERREICH',
        # df['ressort'] == 'Politik OSTEN',
        # df['ressort'] == 'Politik SCHWEIZ',
        # df['ressort'] == 'Recht und Unrecht',
        # df['ressort'] == 'Reisen',
        # df['ressort'] == 'Sport',
        # df['ressort'] == 'Studium',
        # df['ressort'] == 'Wirtschaft',
        # df['ressort'] == 'Wissen',
        # df['ressort'] == 'ZEIT Geld',
        # df['ressort'] == 'ZEIT Literatur',
        # df['ressort'] == 'zeit-magazin',

        # genre features
        # df['genre'] == 'analyse',
        # df['genre'] == 'bericht',
        # df['genre'] == 'gastbeitrag',
        # df['genre'] == 'glosse',
        # df['genre'] == 'interview',
        # df['genre'] == 'kommentar',
        # df['genre'] == 'leserartikel',
        # df['genre'] == 'nachricht',
        # df['genre'] == 'portrait',
        # df['genre'] == 'reportage',
        # df['genre'] == 'unknown',

        # author features
        # df['author'] == 'Patrick Beuth',
        # df['author'] == 'Eike Kühl',
        # df['author'] == 'Mark Spörrle',
        # df['author'] == 'Oliver Fritsch',
        # df['author'] == 'Lisa Caspari',
        # df['author'] == 'Christian Spiller',
        # df['author'] == 'Martin Gehlen',
        # df['author'] == 'Katharina Schuler',
        # df['author'] == 'Lenz Jacobsen',
        # df['author'] == 'Sabine Hockling',
        # df['author'] == 'Marcus Rohwetter',
        # df['author'] == 'Tina Groll',
        # df['author'] == 'Josef Joffe',
        # df['author'] == 'Peter Dausend',
        # df['author'] == 'Christoph Drösser',
        # df['author'] == 'Daniel Haas',
        # df['author'] == 'Ludwig Greven',
        # df['author'] == 'Thomas Fischermann',
        # df['author'] == 'Zacharias Zacharakis',
        # df['author'] == 'Marlies Uken',
        # df['author'] == 'Alexandra Endres',
        # df['author'] == 'Jan Freitag',
        # df['author'] == 'Matthias Naß',
        # df['author'] == 'Michael Thumann',
        # df['author'] == 'Mark Schieritz',
        # df['author'] == 'Jens Jessen',
        # df['author'] == 'Ulf Weigelt',
        # df['author'] == 'Heike Buchter',
        # df['author'] == 'Peter Kümmel',
        # df['author'] == 'Susanne Mayer',
        # df['author'] == 'Alina Schadwinkel',
        # df['author'] == 'Felix Stephan',
        # df['author'] == 'Jochen Bittner',
        # df['author'] == 'Michael Allmaier',
        # df['author'] == 'Kai Biermann',
        # df['author'] == 'Matthias Daum',
        # df['author'] == 'Georg Blume',
        # df['author'] == 'Kilian Trotier',
        # df['author'] == 'Martin Klingst',
        # df['author'] == 'Ulrich Stock',
        # df['author'] == 'Tilman Steffen',
        # df['author'] == 'Matthias Breitinger',
        # df['author'] == 'Theo Sommer',
        # df['author'] == 'Stefan Schmitt',
        # df['author'] == 'Alexander Cammann',
        # df['author'] == 'Alfred Dorfer',
        # df['author'] == 'Gero von Randow',
        # df['author'] == 'Evelyn Finger',
        # df['author'] == 'Finis',
        # df['author'] == 'David Hugendick',
        # df['author'] == 'Carsten Luther',
        # df['author'] == 'Thomas Fischer',
        # df['author'] == 'Andrea Böhm',
        # df['author'] == 'Nadine Oberhuber',
        # df['author'] == 'Thorsten Schröder',
        # df['author'] == 'Özlem Topçu',
        # df['author'] == 'Wenke Husmann',
    ]

    # sub_ressort_features = pd.get_dummies(df.sub_ressort).as_matrix()
    # counts = pd.value_counts(df['ressort'])
    # mask = df['ressort'].isin(counts[counts > 50].index)
    # ressort_features = pd.get_dummies(df[mask]['ressort'])
    # genre_features = pd.get_dummies(df.genre).as_matrix()

    return np.vstack(features).T
