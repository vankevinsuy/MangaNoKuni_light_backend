from Fillers import FillMongoDB

FillMongoDB.UpdateAnime()

FillMongoDB.UpdateManga()

FillMongoDB.UpdateEpisodes()

FillMongoDB.UpdateChapters()

# lancement programmé
# import schedule

# def job(m):
#     FillMongoDB.UpdateAnime()

#     FillMongoDB.UpdateManga()

#     FillMongoDB.UpdateEpisodes()

#     FillMongoDB.UpdateChapters()


# schedule.every().days.at("14:00").do(job,'Time to update data')

# while True:
#     schedule.run_pending()