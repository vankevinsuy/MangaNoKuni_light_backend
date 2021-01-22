class faildChapterWriter :
    def __init__(self):
        self.file_name = "failed_chapter.txt"
        self.file = open(self.file_name, 'w')


    def add_link(self, link):
        self.file.write(link + '\n')