import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import *

# list of documents used in this programme
def files_list():
    files_list = ["What happens in the brain when habits form?.txt","What are the best foods to fight aging?.txt","What are the best diets for 2018?.txt",
    "This supplement may promote healthy arterial aging.txt","The top 10 mental health apps.txt","The state of cancer: Are we close to a cure?.txt","The end of toxic chemo? Blocking vitamin B-2 may stop cancer.txt","The 10 best period tracking apps.txt","The 10 best fitness blogs.txt","Osteoarthritis: Could researchers have found the key to prevention?.txt",
    "Marijuana: Good or bad?.txt","Low-fat vs low-carb: Which diet is best for weight loss?.txt","Intermittent fasting may have 'profound health benefits'.txt","Existing drug may prevent Alzheimer's.txt","Eight cancers could be diagnosed with a single blood test.txt","E-cigarettes may cause cancer and heart disease, says study.txt",
    "Dual attack with two existing drugs destroys lung cancer.txt","Death risk increased with two blood pressure drugs.txt","Belly fat linked to vitamin D deficiency.txt","Baking soda: A safe, easy treatment for arthritis?.txt","Anxiety may be an early sign of Alzheimer's.txt","Alzheimer's risk 10 times lower with herpes medication.txt","Alcohol 'more damaging to brain health than marijuana'.txt","16:8 fasting diet actually works, study finds.txt",
    "Fish oil may not be as healthful as you think, study finds.txt","Full-fat dairy may actually benefit heart health.txt","How does alcohol cause cancer?.txt","How fruit juice affects the gut.txt","Is this how abdominal fat leads to diabetes?.txt","Keto diet: Scientists find link to diabetes risk.txt","Vitamin D-3 could 'reverse' damage to heart.txt","Trouble losing weight? This might be why.txt","What are the best teas for health?.txt","What are the best foods for heart health?.txt","'Too much' brain calcium may cause Parkinson's.txt","Magic mushrooms: Treating depression without dulling emotions.txt","HIV could be treated with a once-a-week pill.txt","One injection could kill cancer.txt","Type 2 diabetes: New guidelines lower blood sugar control levels.txt","Vitamin D: Recent research uncovers new benefits.txt","New multiple sclerosis culprit identified.txt","Could Viagra and a flu shot kill cancer?.txt","'Normal' blood sugar levels may not be so normal after all.txt",
    "Can we learn to avoid being bitten by dogs?.txt","Weight loss breakthrough: Sunlight is key.txt","What too much salt can do to your brain.txt","Eating less not the best way to lose weight, study shows.txt","Could targeting gut bacteria prevent autoimmunity?.txt","Low-calorie sweeteners may promote metabolic syndrome.txt","This 'metastasis-blocking' compound may stop the spread of cancer.txt","Night shifts raise women's cancer risk.txt","What causes multiple sclerosis? Landmark study finds clue.txt","New cancer vaccine is 100 percent successful in mouse model.txt","Ibuprofen could stop Alzheimer's, say researchers.txt","Dogs: Our best friends in sickness and in health.txt","These supplements may actually harm your health.txt","How blueberries help to kill cancer cells.txt","How to boost your brain.txt","Coconut oil: Healthful or unhealthful?.txt","Breakthrough: Researchers fix Alzheimer's gene.txt","A waking nightmare: The enigma of sleep paralysis.txt",
    "Could 'dog flu' be the next pandemic?.txt","Alzheimer's: 'Triple-action' diabetes drug shows promise as treatment.txt","Understanding anhedonia: What happens in the brain?.txt","Could an existing drug halt Parkinson's disease?.txt","Stomach acid drugs may cause depression.txt","Colorectal cancer: The importance of diet.txt","Is Parkinson's an autoimmune disease? More evidence emerges.txt","Why a low-carb diet may not be so good for you.txt","Fasting-induced anti-aging molecule keeps blood vessels young.txt","Drinking hot tea can contribute to cancer risk.txt","How fasting boosts exercise's effects on endurance.txt","Cancer cells' survival strategy defeated with new approach.txt","The brain link between coffee and cannabis.txt","'Natural insecticide' kills advanced prostate cancer cells.txt","Could gut bacteria cause joint pain?.txt","Type 2 diabetes: Intermittent fasting may raise risk.txt","Viruses reprogrammed to attack cancer.txt","Fats or carbs: What causes obesity?.txt",
    "Can a 16-week lifestyle intervention impact blood pressure?.txt","Hormone-fueled breast cancer cells halted with new approach.txt","Turmeric compound could boost memory and mood.txt","E-cigarette flavors found to be toxic.txt","What are the health benefits of being creative?.txt","Skip the guilt: Red wine could protect your oral health.txt","How long-term depression alters the brain.txt","Vitamin D may protect against cancer.txt","How vitamin D protects against heart failure.txt","Multiple sclerosis: Have researchers found a key to prevention?.txt","Why all men 'should be concerned about declining testosterone'.txt","Which foods might stop your brain from shrinking?.txt","How much salt does it really take to harm your heart?.txt"]

    return files_list

#list of stemmed documents
def stem_documents_list():
    stem_documents_list = ["1.txt","2.txt","3.txt","4.txt","5.txt","6.txt","7.txt","8.txt","9.txt","10.txt","11.txt","12.txt","13.txt","14.txt","15.txt","16.txt","17.txt","18.txt","19.txt","20.txt","21.txt","22.txt","23.txt","24.txt",
    "25.txt","26.txt","27.txt","28.txt","29.txt","30.txt","31.txt","32.txt","33.txt","34.txt","35.txt","36.txt","37.txt","38.txt","39.txt","40.txt","41.txt","42.txt","43.txt","44.txt","45.txt","46.txt","47.txt","48.txt","49.txt",
    "50.txt","51.txt","52.txt","53.txt","54.txt","55.txt","56.txt","57.txt","58.txt","59.txt","60.txt","61.txt","62.txt","63.txt","64.txt","65.txt","66.txt","67.txt","68.txt","69.txt","70.txt","71.txt","72.txt","73.txt",
    "74.txt","75.txt","76.txt","77.txt","78.txt","79.txt","80.txt","81.txt","82.txt","83.txt","84.txt","85.txt","86.txt","87.txt","88.txt","89.txt","90.txt","91.txt","92.txt"]

    return stem_documents_list

#FUNCTION FOR TOKENIZATION AND NORMALIZATION
def T_N(file_content):
    file_content  = file_content.lower()
    puncts = "!?-—()&/;:,[]``''"
    for punk in puncts:
        file_content = file_content.replace(punk,'')
        tokens = nltk.word_tokenize(file_content)
    T_N = " ".join(str(tok) for tok in tokens) #converts the list to a string
    return T_N # return a tokenized and normalized string

#FUNCTION FOR REMOVING stop_words
def remove_stopwords(file):
    stoplist = stopwords.words('english')
    clean_words = [word for word in file.split() if word not in stoplist]
    clean_words = " ".join(str(word) for word in clean_words)
    return clean_words #returns words without stop words

#FUNCTION TO IMPLEMENT STEMMING
def stem_words(files):
    stemmer = PorterStemmer()
    stem_words = [stemmer.stem(word) for word in files.split()]
    stem_words = " ".join(str(word) for word in stem_words)
    return stem_words #returns stemmed words

#Functions that collects all the unique words and stores it in "ulist"
def unique_words(text):
    ulist = []
    [ulist.append(x) for x in text.split() if x not in ulist]
    unique_words = " ".join(str(word) for word in ulist)
    return unique_words
