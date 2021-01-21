from selenium import webdriver
from time import sleep
from random import randint

class Instagram:
    def __init__(self, username, password, taglist, numAccounts):
        print('\033[1;31mLogando no Instagram...\033[0;0m')
        self.driver = webdriver.Chrome()
        self.username = username
        self.hashtaglist = taglist
        self.accounts = numAccounts
        self.driver.get('https://instagram.com')
        sleep(1)

        self.driver.find_element_by_xpath("//input[@name=\"username\"]").send_keys(username)
        self.driver.find_element_by_xpath("//input[@name=\"password\"]").send_keys(password)
        self.driver.find_element_by_xpath("//button[@type='submit']").click()

        print('\033[1;31mLogado no Instagram!\033[0;0m')
        sleep(1)

        print('\033[1;31mRemovendo janela de entrada...\033[0;0m')
        sleep(15)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button').click()
        print('\033[1;31mJanela de entrada removida!\033[0;0m')

    def execute(self):
        for hashtag in self.hashtaglist:
            print('\033[1;31mProcurando pela hashtag ' + hashtag + '...\033[0;0m')
            sleep(1)
            self.driver.get('https://instagram.com/explore/tags/' + hashtag + '/')
            print('\033[1;31mEstamos na página da Hashtag ' + hashtag + '!\033[0;0m')

            sleep(1)
            print('\033[1;31mProcurando por posts...\033[0;0m')
            sleep(5)

            first_thumbnail = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div/div/div/div[1]/div[1]/a/div')
            first_thumbnail.click()
            print('\033[1;31mProcurando pelo primeiro post...\033[0;0m')
            sleep(5)
            print('\033[1;31mComeçando o processo...\033[0;0m')
            self.getFollowers()

    def getFollowers(self):
        newFollowers = 0
        visited = 0
        while newFollowers < self.accounts:
            visited += 1 
            username = self.driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/article/header/div[2]/div[1]/div[1]').text

            if self.follow(username) == True:
                newFollowers += 1 
                buttonlike = self.driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/article/div[3]/section[1]/span[1]/button')
                buttonlike.click()

                print('\033[1;31mPost curtido!\033[0;0m')
                sleep(randint(10, 25))
                print('\033[1;31mEscrevendo um comentário...\033[0;0m')
                self.comment()
            self.nextPhoto(visited)

    def follow(self, username):
        print('\033[1;31mVerificando se a pessoa já está sendo seguida por você...\033[0;0m')
        if self.driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/article/header/div[2]/div[1]/div[2]/button').text == 'Seguir':
            self.driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/article/header/div[2]/div[1]/div[2]/button').click()
            print('\033[1;31mVocê agora está seguindo o/a usuário(a) : ' + username + '!\033[0;0m')
            return True
        print('\033[1;31mVocê já segue esta conta!\033[0;0m')
        return False

    def like(self):
        buttonLike = self.driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/article/div[3]/section[1]/span[1]/button/div/span/svg')
        buttonLike.click() # like the photo 
        sleep(randint(10,30))

    def comment(self):
        try:
            comment = randint(2, 9)
            print('\033[1;31mProvavelmente devemos comentar... ' + str(comment) + '!\033[0;0m')
            if comment > 5:
                self.driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/article/div[3]/section[1]/span[2]/button').click()
                commentBox = self.driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/article/div[3]/section[3]/div/form/textarea')
                if comment == 6:
                    commentBox.send_keys('Nice!!')
                    sleep(randint(2,5))
                elif comment == 7:
                    commentBox.send_keys('Cool!')
                    sleep(randint(2,5))
                elif comment == 8:
                    commentBox.send_keys('Nice!')
                    sleep(randint(2,5))
                elif comment == 9:
                    commentBox.send_keys('Cool!')
                    sleep(randint(2,5))
                self.driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/article/div[3]/section[3]/div/form/button').click()
                print('\033[1;31mComentário postado!\033[0;0m')
                sleep(randint(20,25))
        except:
            return      

    def nextPhoto(self, visit):
        print('\033[1;31mIndo para a próxima foto...\033[0;0m')
        if visit == 1:
            self.driver.find_element_by_xpath('/html/body/div[5]/div[1]/div/div/a').click()
        else:
            self.driver.find_element_by_xpath('/html/body/div[5]/div[1]/div/div/a[2]').click()
        sleep(randint(20,25))


hashtags = input('Digite hashtags válidas separadas por um espaço: ')
total = int(input('Digite o total de postagens que você quer curtir: '))

user = input('Digite o @ do seu instagram: ')
password = input('Digite a senha do seu instagram: ')

bot = Instagram(user, password, hashtags.split(), total)
bot.execute()