from script import prediction

welcomeString1 = "Input text in one of these languages:\nEnglish\nFrench\nSpanish\nPortugese\nItalian\n"
welcomeString2 = "Russian\nSwedish\nMalayalam\nDutch\nArabic\nTurkish\nGerman\nTamil\nDanish\nKannada\n"
welcomeString3 = "Greek\nHindi\n"
welcomeString = "{}{}{}".format(welcomeString1, welcomeString2, welcomeString3)

language = str(input(welcomeString))

prediction(language)