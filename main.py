from Procedures import FillDynamoDB, FillMongoDB

FillMongoDB.UpdateManga()
FillMongoDB.UpdateAnime()

FillMongoDB.UpdateChapters()
FillMongoDB.UpdateEpisodes()

#FillDynamoDB.insertManga()
#FillDynamoDB.insertChapitre()