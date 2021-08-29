path = '.'
f = open(path+'/files/server.txt', encoding = 'utf8')
server = f.read()
f.close()
print(server)
textFont = path+'/files/arial.ttf'
MX = MY = 0
def where(someThing, someWhere):
    i = -1
    for t in someWhere:
        i += 1
        if t == someThing:
            return i
    return -1
def re(r):
    return(r)
import os
listdir_sheets = os.listdir(path+'/sheets') if os.path.exists(path+'/sheets') else []
sheets_file = 0
while sheets_file < len(listdir_sheets):
    if os.path.isdir('./sheets/%s' %(listdir_sheets[sheets_file])):
        del listdir_sheets[sheets_file]
    else:
        sheets_file += 1
import math
def deg(r):
    return(math.pi/180*r)
import webbrowser
def webOpen(url):
    webbrowser.open(url)
import urllib.request
def webRead(url):
    with urllib.request.urlopen(url) as response:
        return(response.read().decode('utf-8'))
import json
listdir_examples = json.loads(webRead(server+'examples.json')) if webRead(server+'examples.json') else []
import tkinter
win = tkinter.Tk()
vnw = win.winfo_screenwidth()/100
vnh = win.winfo_screenheight()/100
vw = vh = 0
import pygame
pygame.init()
class getContext2d:
    def __init__(self, canvas, lineWidth = 10, fillStyle = (255, 255, 255), strokeStyle = (0, 0, 0), font = '10px '+textFont):
        self.canvas = canvas
        self.lineWidth = lineWidth
        self.fillStyle = fillStyle
        self.strokeStyle = strokeStyle
        self.nowXY = [0, 0]
        self.font = font
    def fillRect(self, x, y, w, h):
        pygame.draw.rect(self.canvas, self.fillStyle, [x, y, w, h], 0)
    def strokeRect(self, x, y, w, h):
        pygame.draw.rect(self.canvas, self.strokeStyle, [x, y, w, h], int(self.lineWidth))
    def fillText(self, t, x, y):
        font = self.font.split()
        flag = len(font) == 3
        b = font[0] == 'bg' if flag else False
        s = int(font[1].replace('px', '')) if flag else int(font[0].replace('px', ''))
        f = font[2] if flag else font[1]
        font = pygame.font.Font(f, int(s*0.8))
        if b:
            self.canvas.blit(font.render(t, True, self.fillStyle, self.strokeStyle), (int(x), int(y)))
        else:
            self.canvas.blit(font.render(t, True, self.fillStyle), (int(x), int(y-0.3*vnw)))
    def drawImage(self, i, xy, wh = False, r = False):
        if wh:
            i = pygame.transform.scale(i, (int(wh[0]), int(wh[1])))
        if r:
            i = pygame.transform.rotate(i, int(r))
        self.canvas.blit(i, (int(xy[0]), int(xy[1])))
    def fillBox(self, x, y, w, h, r):
        pygame.draw.rect(self.canvas, self.fillStyle, [re(x+r), re(y), re(w-2*r), re(h)], 0)
        pygame.draw.rect(self.canvas, self.fillStyle, [re(x), re(y+r), re(w), re(h-2*r)], 0)
        pygame.draw.circle(self.canvas, self.fillStyle, (re(x+r), re(y+r)), re(r), 0)
        pygame.draw.circle(self.canvas, self.fillStyle, (re(x+r), re(y+h-r)), re(r), 0)
        pygame.draw.circle(self.canvas, self.fillStyle, (re(x+w-r), re(y+r)), re(r), 0)
        pygame.draw.circle(self.canvas, self.fillStyle, (re(x+w-r), re(y+h-r)), re(r), 0)
    def strokeBox(self, x, y, w, h, r):
        lw = self.lineWidth
        pygame.draw.line(self.canvas, self.strokeStyle, (re(x+r+lw), re(y)), (re(x+w-2*r+lw), re(y)), int(self.lineWidth))
        pygame.draw.line(self.canvas, self.strokeStyle, (re(x+w), re(y+r+lw)), (re(x+w), re(y+h-2*r+lw)), int(self.lineWidth))
        pygame.draw.line(self.canvas, self.strokeStyle, (re(x+w-2*r+lw), re(y+h)), (re(x+r+lw), re(y+h)), int(self.lineWidth))
        pygame.draw.line(self.canvas, self.strokeStyle, (re(x), re(y+h-2*r+lw)), (re(x), re(y+r+lw)), int(self.lineWidth))
    def moveTo(self, x = 'old', y = 'old'):
        x = x if x != 'old' else self.nowXY[0]
        y = y if y != 'old' else self.nowXY[1]
        self.nowXY = [x, y]
    def lineTo(self, x, y):
        x = x if x != 'old' else self.nowXY[0]
        y = y if y != 'old' else self.nowXY[1]
        pygame.draw.line(self.canvas, self.strokeStyle, (re(self.nowXY[0]), re(self.nowXY[1])), (re(x), re(y)), int(self.lineWidth))
        self.nowXY = [x, y]
class canvas:
    def __init__(self, width = 0, height = 0, bgc = (0, 0, 0), title = '', icon = '', bgm_volume = 80, se_volume = 80):
        self.this = False
        global vw, vh
        self.width, self.height = width, height
        vw, vh = width/100, height/100
        self.bgc = bgc
        self.running = False
        self.page = {'self':'sheets'}
        self.own = {'player_character':[], 'player_modeling':[], 'shop_character':[], 'shop_modeling':[], 'shop_music':[], 'start_official':[path+'/song/神殿裡昏迷｜coma_in_temple'], 'start_mine':[]}
        self.title = title
        self.getContext2d = False
        self.alpha = pygame.Surface((width, height), pygame.SRCALPHA)
        self.alpha_getContex2 = False
        self.icon =  icon
        self.login_page = 'login_old'
        self.bgm_volume = bgm_volume
        self.se_volume = se_volume
        self.pageButtons = {'home':[], 'player':[], 'shop':[], 'start':[], 'setting':[], 'login':[], 'playing':[]}
        self.pageBackgroundImage = {'xy':-40, 'home':False, 'player':False, 'shop':False, 'start':False, 'setting':False, 'login':False, 'playing':False}
        self.pageBackgroundMusic = {'home':False, 'player':False, 'shop':False, 'start':False, 'setting':False, 'login':False, 'playing':False}
        self.key = {}
        self.init()
        self.set_icon()
    def init(self):
        self.this = pygame.display.set_mode((int(self.width), int(self.height)), pygame.RESIZABLE)
        pygame.display.set_caption(self.title)
        self.getContext2d = getContext2d(canvas = self.this)
        self.alpha_getContext2d = getContext2d(canvas = self.alpha)
        self.this.fill(self.bgc)
    def set_icon(self):
        if self.icon != '':
            icon = pygame.image.load(self.icon)
            pygame.display.set_icon(icon)
    def pageIs(self, type):
        re = False
        if type == 'homeS':
            re = self.page['self'] == 'home'
        elif type == 'homeC':
            re = self.page['self'] == 'player' or self.page['self'] == 'shop' or self.page['self'] == 'start' or self.page['self'] == 'setting'
        elif type == 'homeN':
            self.page['self'] == 'login' or self.page['self'] == 'home'
        return re
    def draw_switcherBg(self):
        self.getContext2d.fillStyle = color.white
        self.getContext2d.fillRect(1*vw, 14*vh, 98*vw, 84*vh)
    def draw_switcherFg(self):
        self.alpha.fill((0, 0, 0, 0))
        self.alpha_getContext2d.fillStyle = (0, 0, 0, 80)
        self.alpha_getContext2d.strokeStyle = (0, 0, 0, 0)
        self.alpha_getContext2d.lineWidth = 0.8*vw
        if self.is_hover(2*vw, 16*vh, 13*vw, 80*vh):
            self.alpha_getContext2d.fillRect(2*vw, 16*vh, 13*vw, 80*vh)
            self.alpha_getContext2d.moveTo((8+1)*vw, (56-3)*vh)
            self.alpha_getContext2d.lineTo((8-1)*vw, 56*vh)
            self.alpha_getContext2d.lineTo((8+1)*vw, (56+3)*vh)
        if self.is_hover(85*vw, 16*vh, 13*vw, 80*vh):
            self.alpha_getContext2d.fillRect(85*vw, 16*vh, 13*vw, 80*vh)
            self.alpha_getContext2d.moveTo((91.5-1)*vw, (56-3)*vh)
            self.alpha_getContext2d.lineTo((91.5+1)*vw, 56*vh)
            self.alpha_getContext2d.lineTo((91.5-1)*vw, (56+3)*vh)
        self.this.blit(self.alpha, (0, 0))
    def is_hover(self, x, y, w, h):
        return(MX > x and MX < x+w and MY > y and MY < y+h)
    def getContext(self, type):
        if type == '2d':
            return(self.getContext2d)
class color:
    def __init__(self):
        self.darkBrown = (113, 71, 0)
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.orange = (255, 214, 128)
        self.skyblue = (87, 201, 238)
        self.skyblue_w = (180, 227, 243)
        self.gray = (144, 144, 144)
        self.gray_w = (222, 222, 222)
color = color()
cvs = canvas(width = 80*vnw, height = 80*vnh, title = '[alda-pl] Alda Play List', icon = path+'/files/alda-cd.svg', bgc = color.white)
ctx = cvs.getContext('2d')
cvs.running = True
alertBox = []
images = {}
images['logo'] = path+'/files/alda-logo-horizontal.svg'
images['cd'] = path+'/files/alda-cd.svg'
images['play'] = path+'/files/play.svg'
images['pause'] = path+'/files/pause.svg'
images['stop'] = path+'/files/stop.svg'
for image in images:
    images[image] = pygame.image.load(images[image])
    images[image] = [images[image], images[image].get_rect()[2], images[image].get_rect()[3], images[image].get_rect()[3]/images[image].get_rect()[2]]
buttons = {}
buttons['sheets'] = [50*vw+(-1-10)*vnw, (images['logo'][3]*20+2)*vnw, 10*vnw, 3*vnw, 0.5*vnw]
buttons['examples'] = [50*vw+vnw, (images['logo'][3]*20+2)*vnw, 10*vnw, 3*vnw, 0.5*vnw]
buttons_player = {}
buttons_player['play'] = [100*vw-12.5*vnw, 100*vh-3.5*vnw, 3*vnw, 2*vnw, 0.1*vnw]
buttons_player['pause'] = [100*vw-8.5*vnw, 100*vh-3.5*vnw, 3*vnw, 2*vnw, 0.1*vnw]
buttons_player['stop'] = [100*vw-4.5*vnw, 100*vh-3.5*vnw, 3*vnw, 2*vnw, 0.1*vnw]
song = ['--------', 'stop', 0, 'sheets']
scroll = 0

while cvs.running:
    is_clicked = False
    cvs.this.fill(cvs.bgc)
    MX = pygame.mouse.get_pos()[0]
    MY = pygame.mouse.get_pos()[1]
    buttons['sheets'] = [50*vw+(-1-10)*vnw, (images['logo'][3]*20+2)*vnw, 10*vnw, 3*vnw, 0.5*vnw]
    buttons['examples'] = [50*vw+vnw, (images['logo'][3]*20+2)*vnw, 10*vnw, 3*vnw, 0.5*vnw]
    buttons_player['play'] = [100*vw-12.5*vnw, 100*vh-3.5*vnw, 3*vnw, 2*vnw, 0.1*vnw]
    buttons_player['pause'] = [100*vw-8.5*vnw, 100*vh-3.5*vnw, 3*vnw, 2*vnw, 0.1*vnw]
    buttons_player['stop'] = [100*vw-4.5*vnw, 100*vh-3.5*vnw, 3*vnw, 2*vnw, 0.1*vnw]
    listdir = listdir_sheets if cvs.page['self'] == 'sheets' else listdir_examples
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            cvs.running = False
            pygame.quit()
            for efp in os.listdir(path+'/examples'):
                os.remove('%s/examples/%s' %(path, efp))
            exit()
        if event.type == pygame.VIDEORESIZE:
            vw, vh = event.size[0]/100, event.size[1]/100
        if event.type == pygame.MOUSEBUTTONDOWN:
            if cvs.is_hover(0, 100*vh-5*vnw, 100*vw, 6*vnw):
                is_clicked = True
            for button in buttons:
                if cvs.is_hover(buttons[button][0], buttons[button][1], buttons[button][2], buttons[button][3]):
                    cvs.page['self'] = button
                    scroll = 0
                    is_clicked = True
            for button in buttons_player:
                if cvs.is_hover(buttons_player[button][0], buttons_player[button][1], buttons_player[button][2], buttons_player[button][3]):
                    is_clicked = True
                    if button == 'play':
                        if song[1] == 'stop':
                            if os.path.exists('./%s/%s' %(song[3], song[0])) and os.path.isfile('./%s/%s' %(song[3], song[0])):
                                os.system('.\\files\\alda.exe play -f ./%s/%s' %(song[3], song[0]))
                        elif song[1] == 'pause':
                            os.system('.\\files\\alda.exe play')
                    else:
                        os.system('.\\files\\alda.exe stop')
                    song[1] = button
            for i in range(0, len(listdir)):
                if cvs.is_hover(2*vnw, (images['logo'][3]*20+7+i*2+scroll)*vnw, 100*vw - 4*vnw, 2*vnw) and (images['logo'][3]*20+7+i*2+scroll)*vnw >= (images['logo'][3]*20+7)*vnw and (images['logo'][3]*20+7+i*2+scroll+2)*vnw < 100*vw - 5*vnw and is_clicked == False:
                    if cvs.page['self'] == 'sheets':
                        clickPath = './sheets/%s' %(listdir[i])
                        if os.path.exists(clickPath):
                            if os.path.isfile(clickPath):
                                os.system('.\\files\\alda.exe stop')
                                song = [listdir[i], 'stop', 0, 'sheets']
                    elif cvs.page['self'] == 'examples':
                        clickPath = '%s/examples/%s' %(path, listdir[i])
                        if os.path.exists(clickPath) != True:
                            f = open(clickPath, 'a+')
                            f.close()
                        fileIndex = webRead('%sexamples/%s' %(server, listdir[i]))
                        if fileIndex:
                            f = open(clickPath, 'w')
                            f.write(fileIndex)
                            f.close()
                            os.system('.\\files\\alda.exe stop')
                            song = [listdir[i], 'stop', 0, 'examples']
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                cvs.key['ArrowUp'] = True
            elif event.key == pygame.K_DOWN:
                cvs.key['ArrowDown'] = True
            elif event.key == pygame.K_SPACE:
                if song[1] == 'play':
                    os.system('.\\files\\alda.exe stop')
                    song[1] = 'pause'
                else:
                    if song[1] == 'stop':
                        if os.path.exists('./%s/%s' %(song[3], song[0])) and os.path.isfile('./%s/%s' %(song[3], song[0])):
                            os.system('.\\files\\alda.exe play -f ./%s/%s' %(song[3], song[0]))
                    elif song[1] == 'pause':
                        os.system('.\\files\\alda.exe play')
                    song[1] = 'play'
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                cvs.key['ArrowUp'] = False
            elif event.key == pygame.K_DOWN:
                cvs.key['ArrowDown'] = False
    if 'ArrowUp' in cvs.key and cvs.key['ArrowUp']:
        scroll = scroll+1 if scroll < 0 else scroll
    if 'ArrowDown' in cvs.key and cvs.key['ArrowDown']:
        scroll = scroll-1 if scroll > -len(listdir)*2+(100*vh/vnw-5-images['logo'][3]*20-7) else scroll
    for i in range(0, len(listdir)):
        ctx.fillStyle = color.skyblue if cvs.is_hover(2*vnw, (images['logo'][3]*20+7+i*2+scroll)*vnw, 100*vw - 4*vnw, 2*vnw) else color.black
        ctx.font = str(int(2*vnw))+'px '+textFont
        ctx.fillText(listdir[i], 2*vnw, (images['logo'][3]*20+7+i*2+scroll)*vnw)
    ctx.fillStyle = color.white
    ctx.fillRect(0, 0, 100*vw, (images['logo'][3]*20+7)*vnw)
    ctx.fillRect(100*vw-2*vnw, 0, 2*vnw, 100*vh)
    ctx.drawImage(images['logo'][0], ((100*vw-20*vnw)/2, 1*vnw), (20*vnw, images['logo'][3]*20*vnw))
    for button in buttons:
        ctx.lineWidth = 0.2*vnw
        ctx.fillStyle = color.skyblue
        ctx.fillBox(buttons[button][0]-ctx.lineWidth, buttons[button][1]-ctx.lineWidth, buttons[button][2]+ctx.lineWidth*2, buttons[button][3]+ctx.lineWidth*2, buttons[button][4])
        ctx.fillStyle = color.skyblue_w if cvs.page['self'] == button or cvs.is_hover(buttons[button][0], buttons[button][1], buttons[button][2], buttons[button][3]) else color.white
        ctx.fillBox(buttons[button][0], buttons[button][1], buttons[button][2], buttons[button][3], buttons[button][4])
        ctx.fillStyle = color.black
        ctx.font = str(int(2*vnw))+'px '+textFont
        ctx.fillText(button, buttons[button][0]+(5-len(button)/2*0.8)*vnw, buttons[button][1]+1*vnw)
    ctx.fillStyle = color.gray_w
    ctx.fillRect(0, 100*vh-5*vnw, 100*vw, 6*vnw)
    ctx.fillStyle = color.black
    ctx.font = str(int(2.5*vnw))+'px '+textFont
    ctx.fillText('%s: %s' %(song[3], song[0]), 5*vnw, 100*vh-3.25*vnw)
    ctx.fillStyle = color.gray_w
    ctx.fillRect(100*vw-14*vnw, 100*vh-5*vnw, 100*vw, 6*vnw)
    for button in buttons_player:
        ctx.lineWidth = 0.17*vnw
        ctx.fillStyle = color.gray
        ctx.fillBox(buttons_player[button][0]-ctx.lineWidth, buttons_player[button][1]-ctx.lineWidth, buttons_player[button][2]+ctx.lineWidth*2, buttons_player[button][3]+ctx.lineWidth*2, buttons_player[button][4])
        ctx.fillStyle = color.gray_w if cvs.page['self'] == button or cvs.is_hover(buttons_player[button][0], buttons_player[button][1], buttons_player[button][2], buttons_player[button][3]) else color.white
        ctx.fillBox(buttons_player[button][0], buttons_player[button][1], buttons_player[button][2], buttons_player[button][3], buttons_player[button][4])
        ctx.fillStyle = color.black
        ctx.font = str(int(2*vnw))+'px '+textFont
        ctx.drawImage(images[button][0], (buttons_player[button][0]+(3-1.5/images[button][3])/2*vnw, buttons_player[button][1]+0.25*vnw), (1.5*vnw/images[button][3], 1.5*vnw))
    # rabs = -((pow(2, 0.5)-1)*3*vnw/2/45*abs(abs(song[2]%90-45)-45))
    # rabs = -abs(3*vnw - pow(2, 0.5)/2*3*vnw * math.cos(math.pi/4 - deg(song[2])))
    cd = pygame.transform.scale(images['cd'][0], (int(3*vnw), int(3*vnw)))
    cd = pygame.transform.rotate(cd, int(song[2]))
    rabs = (images['cd'][1] - cd.get_rect()[2])/2
    ctx.drawImage(cd, (0.25*vnw+rabs, 100*vh-4.75*vnw+rabs))#, wh = (3*vnw, 3*vnw), r = song[2] if song[1] != 'stop' else False)
    song[2] = 0 if song[1] == 'stop' else song[2] + 1 if song[1] == 'play' else song[2]
    pygame.time.Clock().tick(500)
    pygame.display.update()