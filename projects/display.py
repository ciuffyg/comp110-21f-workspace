import tkinter as tk
import pandas as pd
from random import uniform, randint

class Player:
    """Defines a player and their attributes."""
    first_name: str
    last_name: str
    pos: str
    age: int
    team: str

    play: float
    mpg: float

    three_r: float
    ft_r: float
    orb_p: float
    drb_p: float
    ast_p: float
    stl_p: float
    blk_p: float
    tov_p: float
    usg_p: float
    three_p: float
    two_p: float
    ft_p: float

    fg_a: int
    fg_m: int
    ft: int
    pts: int
    reb: int
    ast: int
    stl: int
    blk: int
    to: int
    
    def __init__(self, a: str, b: str, c: str, age: int, d: str, play: float, mpg: float, e: float, f: float, g: float, h: float, i: float, j: float, k: float, ll: float, m: float, n: float, o: float, p: float):
        self.first_name = a
        self.last_name = b
        self.pos = c
        self.age = age
        self.team = d
        self.play = play
        self.mpg = mpg
        self.three_r = e
        self.ft_r = f
        self.orb_p = g
        self.drb_p = h
        self.ast_p = i
        self.stl_p = j
        self.blk_p = k
        self.tov_p = ll
        self.usg_p = m
        self.three_p = n
        self.two_p = o
        self.ft_p = p

        self.fg_a = 0
        self.fg_m = 0
        self.ft = 0
        self.pts = 0
        self.reb = 0
        self.ast = 0
        self.stl = 0
        self.blk = 0
        self.to = 0
    
    def __repr__(self) -> str:
        return (f'{self.first_name} {self.last_name}')

    def read(self):
        print(f"{self.first_name} {self.last_name} ({self.age}) {self.team} {self.pos}\n    {self.play}\n")

    def stat_rep(self) -> str:
        result = str = f"PTS {self.pts} | FGA: {self.fg_a} | FGM: {self.fg_m} | FT: {self.ft} | REB: {self.reb} | AST: {self.ast} | STL: {self.stl} | BLK: {self.blk} | TO: {self.to}"
        return result

    def clear_stat(self):
        self.fg_a = 0
        self.fg_m = 0
        self.ft = 0
        self.pts = 0
        self.reb = 0
        self.ast = 0
        self.stl = 0
        self.blk = 0
        self.to = 0


df = pd.read_csv(
    r"C:\Users\Gianluca Ciuffreda\comp110-21f-workspace\projects\nbastats.csv", 
    names=['First', 'Last', 'Pos', 'Age', 'Team', 'Play', 'MPG', '3PAr', 'FTr', 'ORB%', 'DRB%', 'AST%', 'STL%', 'BLK%', 'TOV%', 'USG%', '3P%', '2P%', 'FT%'], 
)

homeid: str
awayid: str

home_roster: list[Player] = []
away_roster: list[Player] = []
a_oncourt: list[Player] = []
b_oncourt: list[Player] = []

home_top: dict[int, Player] = {
    1: [],
    2: [],
    3: [],
    4: [],
    5: []
    }
away_top: dict[int, Player] = {
    1: [],
    2: [],
    3: [],
    4: [],
    5: []
    }

possession: list[Player]
home_score: int = 0
away_score: int = 0
playclock: int = 0
clock: int = 2880


def initiate(a: str, b: str) -> None:
    global a_oncourt, b_oncourt, home_score, away_score, playclock, clock, home_top, away_top
    home_score = 0
    away_score = 0
    playclock = 0
    clock = 2880
    tm1: str = a
    tm2: str = b
    i: int = 0
    while i < 605:
        p: Player = Player(
            df["First"][i],   # type: ignore
            df["Last"][i],  # type: ignore
            df["Pos"][i],  # type: ignore
            df["Age"][i],  # type: ignore
            df["Team"][i],  # type: ignore
            df["Play"][i],  # type: ignore
            df["MPG"][i],  # type: ignore
            df["3PAr"][i],  # type: ignore
            df["FTr"][i],  # type: ignore
            df["ORB%"][i],  # type: ignore
            df["DRB%"][i],  # type: ignore
            df["AST%"][i],  # type: ignore
            df["STL%"][i],  # type: ignore
            df["BLK%"][i],  # type: ignore
            df["TOV%"][i],  # type: ignore
            df["USG%"][i],  # type: ignore
            df["3P%"][i],  # type: ignore
            df["2P%"][i],  # type: ignore
            df["FT%"][i],  # type: ignore
        )
        if p.team == tm1:
            home_roster.append(p)
        elif p.team == tm2:
            away_roster.append(p)
        i += 1
    a_oncourt = sub_court(home_roster)
    b_oncourt = sub_court(away_roster)
    for player in home_roster:
        player.clear_stat()
    for player in away_roster:
        player.clear_stat()
    ind: int = 4
    for key in home_top:
        home_top[key] = home_roster[ind]
        ind -= 1
    ind = 4
    for key in away_top:
        away_top[key] = away_roster[ind]
        ind -= 1
    print("initiated teams.")


def sub_court(a: list[Player]) -> list[Player]:
    a_index: dict[Player, list[float]] = {}
    step: float = 0.000
    result: list[Player] = []
    max_: float = 0.000
    count: int = 5
    i: int = 0
    while i < len(a):
        x: float = step
        y: float = a[i].play + step
        a_index[a[i]] = [x, y]
        if y > max_:
            max_ = y
        i += 1
        step = y
    while count > 0:
        r: float = uniform(0.000, max_)
        for key in a_index:
            if r > a_index[key][0] and r <= a_index[key][1]:
                who: Player = key
                dup: int = 0
                i2: int = 0
                while i2 < len(result):
                    if who == result[i2]:
                        dup += 1
                    i2 += 1
                if dup == 0:
                    result.append(who)
                    count -= 1
    # print("subbed in players.")
    return result


def change(a: list[Player], b: list[Player], c: list[Player]) -> str:
    if a != b:
        global possession
        possession = b
        return (f"{b[0].team} ball.")
    else:
        possession = c
        return (f"{c[0].team} ball.")


def rebound(a: list[Player], b: list[Player]):
    global possession, clock, playclock
    a_index: dict[Player, list[float]] = {}
    b_index: dict[Player, list[float]] = {}
    offe: list[Player]
    defe: list[Player]
    step: float = 0.000
    max_: float = 0.000
    i: int = 0
    if possession == home_roster:
        offe = home_roster
        defe = away_roster
        while i < len(a):
            y: float = a[i].orb_p + step
            a_index[a[i]] = [step, y]
            if y > max_:
                max_ = y
            i += 1
            step = y
        i = 0
        while i < len(b):
            y: float = b[i].drb_p + step
            b_index[b[i]] = [step, y]
            if y > max_:
                max_ = y
            i += 1
            step = y
    else:
        defe = home_roster
        offe = away_roster
        while i < len(a):
            y: float = a[i].drb_p + step
            a_index[a[i]] = [step, y]
            if y > max_:
                max_ = y
            i += 1
            step = y
        i = 0
        while i < len(b):
            y: float = b[i].orb_p + step
            b_index[b[i]] = [step, y]
            if y > max_:
                max_ = y
            i += 1
            step = y
    who: float = uniform(0.000, max_)
    for key in a_index:
        if who > a_index[key][0] and who <= a_index[key][1]:
            # print(f"{a_index[key]} got the rebound.")
            playclock += randint(0, 24 - playclock)
            possession = offe
            key.reb += 1
    for key in b_index:
        if who > b_index[key][0] and who <= b_index[key][1]:
            # print(f"{b_index[key]} got the rebound.")
            possession = defe
            clock -= playclock
            key.reb += 1
            

def shot(a: Player, b: Player) -> int:
    global clock, playclock
    t: float = uniform(0.000, 1.000)
    pt: int = 0
    playclock += randint(0, 16 - playclock)
    a.fg_a += 1
    if t <= a.three_r:
        hit: float = uniform(0.000, 1.000)
        if hit <= a.three_p:
            pt += 3
            a.pts += 3
            a.fg_m += 1
            clock -= playclock
        else:
            rebound(a_oncourt, b_oncourt) 
    else:
        block: float = uniform(0.000, 1.000)
        if block <= b.blk_p:
            # print("shot blocked.")
            b.blk += 1
            clock -= playclock
        else:
            hit: float = uniform(0.000, 1.000)
            if hit <= a.two_p:
                pt += 2
                a.pts += 2
                a.fg_m += 1
                clock -= playclock
            else:
                rebound(a_oncourt, b_oncourt)
    return pt
    

def whogotit(a: list[Player]) -> Player:
    a_index: dict[Player, list[float]] = {}
    step: float = 0.000
    result: Player = a[0]
    max_: float = 0.000
    i: int = 0
    while i < len(a):
        x: float = step
        y: float = a[i].usg_p + step
        a_index[a[i]] = [x, y]
        if y > max_:
            max_ = y
        i += 1
        step = y
    r: float = uniform(0.000, max_)
    for key in a_index:
        if r > a_index[key][0] and r <= a_index[key][1]:
            result = key
            return result


def whoondefense(a: list[Player]) -> Player:
    max_: int = len(a)
    i: int = randint(0, max_ - 1)
    result: Player = a[i]
    return result


def play(a: Player, b: Player):
    global possession, home_score, away_score, clock, playclock, a_oncourt, b_oncourt, home_roster, away_roster
    r: float = uniform(0.000, 100.000)
    playclock += randint(1, 8)
    if r >= 0 and r <= b.stl_p:
        # print(f"{b.first_name} {b.last_name} stole the ball.")
        change(possession, home_roster, away_roster)
        clock -= playclock
        b.stl += 1
    elif r > b.stl_p and r <= (b.stl_p + a.tov_p):
        # print("turnover.")
        change(possession, home_roster, away_roster)
        clock -= playclock
        a.to += 1
    else:
        if possession == home_roster:
            home_score += shot(a, b)
            possession = away_roster
        else:
            away_score += shot(a, b)
            possession = home_roster
    playclock = 0
    # a_oncourt = sub_court(home_roster)
    # b_oncourt = sub_court(away_roster)
    # print("a play happened.")


def match(a: list[Player], b: list[Player]) -> None:
    global clock, possession, home_top, away_top
    possession = a 
    while clock > 0:
        ballwith: Player
        defender: Player
        if possession == a:
            ballwith = whogotit(a_oncourt)
            defender = whoondefense(b_oncourt)
        else:
            ballwith = whogotit(b_oncourt)
            defender = whoondefense(a_oncourt)
        play(ballwith, defender)
    print(home_score)
    print(away_score)
    print(home_top)
    print(away_top)


class MyWindow:
    def __init__(self, root):
        root.title("NBA SIM 2022")
        root.geometry("1920x1080")
        root.maxsize(1920, 1080)
        root.minsize(640,360)
        root.iconbitmap('assets/nbalogo.ico')

        self.bg_image = tk.PhotoImage(file="assets/gamebg_1.png")
        self.bg = tk.Label(root, image=self.bg_image)
        self.bg.place(x=0,y=0)

        # self.photo = tk.PhotoImage(file="nbalogo.png")
        # image1 = tk.Label(root, image=self.photo, width="64", height="142")
        # image1.place(x=300)
        # label = tk.Label(root, text="NBA", font=("Calibri", 60), foreground="dark blue")
        # label.place(x=370)
        # label = tk.Label(root, text="SIM\n2022", font=("Calibri", 30), foreground="red")
        # label.place(x=520)

        # display scores
        self.scoreh_value = tk.StringVar()
        self.scoreh = tk.Label(root, textvariable=self.scoreh_value, font=("Calibri", 75))
        self.scoreh.place(x=710, y=240)
        self.scorea_value = tk.StringVar()
        self.scorea = tk.Label(root, textvariable=self.scorea_value, font=("Calibri", 75))
        self.scorea.place(x=1040, y=240)
        # display team
        self.label2_text = tk.StringVar()
        self.label2 = tk.Label(root, textvariable=self.label2_text, font=("Calibri", 40), foreground="white")
        self.label2.place(x=90, y=810)

        # dropdown menu to select team
        self.option = tk.StringVar()
        dropdown = tk.OptionMenu(root,self.option, "ATL", "BOS", "BRK", "CHI", "CHO", "CLE", "DAL", "DEN", "DET", "GSW", "HOU", "IND", "LAC", "LAL", "MEM", "MIA", "MIL", "MIN", "NOP", "NYK", "OKC", "ORL", "PHI", "PHO", "POR", "SAC", "SAS", "TOR", "UTA", "WAS")
        dropdown.place(x=750, y=415)

        # team entry button
        button2 = tk.Button(root, command=self.pick_home, text="Select Home", font="Calibri")
        button2.place(x=750, y=440)

        self.label3_text = tk.StringVar()
        self.label3 = tk.Label(root, textvariable=self.label3_text, font=("Calibri", 40), foreground="white")
        self.label3.place(x=1305, y=810)

        # dropdown menu to select team
        self.option2 = tk.StringVar()
        dropdown2 = tk.OptionMenu(root, self.option2, "ATL", "BOS", "BRK", "CHI", "CHO", "CLE", "DAL", "DEN", "DET", "GSW", "HOU", "IND", "LAC", "LAL", "MEM", "MIA", "MIL", "MIN", "NOP", "NYK", "OKC", "ORL", "PHI", "PHO", "POR", "SAC", "SAS", "TOR", "UTA", "WAS")
        dropdown2.place(x=1075, y=415)

        # team entry button
        button3 = tk.Button(root, command=self.pick_away, text="Select Away", font="Calibri")
        button3.place(x=1075, y=440)

        # home team banner
        self.bannerh = tk.PhotoImage(file="assets/logos/nbalogo.png")
        self.homebanner = tk.Label(root, image=self.bannerh)
        self.homebanner.place(x=80, y=100)
        
        # away team banner
        self.bannera = tk.PhotoImage(file="assets/logos/nbalogo.png")
        self.awaybanner = tk.Label(root, image=self.bannera)
        self.awaybanner.place(x=1300, y=100)

        # home team logo
        # self.logoh = tk.PhotoImage(file="assets/logos/nbalogo.png")
        # self.homelogo = tk.Label(root, image=self.bannerh)
        # self.homelogo.place(x=85, y=580)
        
        # away team logo
        # self.logoa = tk.PhotoImage(file="assets/logos/nbalogo.png")
        # self.awaylogo = tk.Label(root, image=self.bannera)
        # self.awaylogo.place(relx=.9, rely=.65)

        # display stat report
        self.label4_text = tk.StringVar()
        self.label4 = tk.Label(root, textvariable=self.label4_text, font=("Calibri", 20))
        self.label4.place(x=1075, y=600)

        button4 = tk.Button(root, command=self.runsim,text="Play", font=("Calibri", 20))
        button4.place(x=920, y=420)


    def pick_home(self):
        global homeid
        text = self.option.get()
        homeid = text
        b: dict[str, list(str)] = {
            "BOS":["assets/banners/banner_bos.png","assets/logos/logo_bos.png"],
            "ATL":["assets/banners/banner_atl.png","assets/logos/logo_atl.png"],
            "BRK":["assets/banners/banner_brk.png","assets/logos/logo_brk.png"],
            "CHI":["assets/banners/banner_chi.png","assets/logos/logo_chi.png"],
            "CHO":["assets/banners/banner_cho.png","assets/logos/logo_cho.png"],
            "CLE":["assets/banners/banner_cle.png","assets/logos/logo_cle.png"],
            "DAL":["assets/banners/banner_dal.png","assets/logos/logo_dal.png"],
            "DEN":["assets/banners/banner_den.png","assets/logos/logo_den.png"],
            "DET":["assets/banners/banner_det.png","assets/logos/logo_det.png"],
            "GSW":["assets/banners/banner_gsw.png","assets/logos/logo_gsw.png"],
            "HOU":["assets/banners/banner_hou.png","assets/logos/logo_hou.png"],
            "IND":["assets/banners/banner_ind.png","assets/logos/logo_ind.png"],
            "LAC":["assets/banners/banner_lac.png","assets/logos/logo_lac.png"],
            "LAL":["assets/banners/banner_lal.png","assets/logos/logo_lal.png"],
            "MEM":["assets/banners/banner_mem.png","assets/logos/logo_mem.png"],
            "MIA":["assets/banners/banner_mia.png","assets/logos/logo_mia.png"],
            "MIL":["assets/banners/banner_mil.png","assets/logos/logo_mil.png"],
            "MIN":["assets/banners/banner_min.png","assets/logos/logo_min.png"],
            "NOP":["assets/banners/banner_nop.png","assets/logos/logo_nop.png"],
            "NYK":["assets/banners/banner_nyk.png","assets/logos/logo_nyk.png"],
            "OKC":["assets/banners/banner_okc.png","assets/logos/logo_okc.png"],
            "ORL":["assets/banners/banner_orl.png","assets/logos/logo_orl.png"],
            "PHI":["assets/banners/banner_phi.png","assets/logos/logo_phi.png"],
            "PHO":["assets/banners/banner_pho.png","assets/logos/logo_pho.png"],
            "POR":["assets/banners/banner_por.png","assets/logos/logo_por.png"],
            "SAC":["assets/banners/banner_sac.png","assets/logos/logo_sac.png"],
            "SAS":["assets/banners/banner_sas.png","assets/logos/logo_sas.png"],
            "TOR":["assets/banners/banner_tor.png","assets/logos/logo_tor.png"],
            "UTA":["assets/banners/banner_uta.png","assets/logos/logo_uta.png"],
            "WAS":["assets/banners/banner_was.png","assets/logos/logo_was.png"]
            }
        t: dict[str, list(str)] = {
            "ATL":["Atlanta Hawks", "red"],
            "BOS":["Boston Celtics", "green"],
            "BRK":["Brooklyn Nets", "black"],
            "CHI":["Chicago Bulls", "red"],
            "CHO":["Charlotte Hornets", "light blue"],
            "CLE":["Cleveland Cavaliers", "yellow"],
            "DAL":["Dallas Mavericks", "dark blue"],
            "DEN":["Denver Nuggets", "yellow"],
            "DET":["Detroit Pistons", "red"],
            "GSW":["Golden St Warriors", "yellow"],
            "HOU":["Houston Rockets", "red"],
            "IND":["Indiana Pacers", "dark blue"],
            "LAC":["Los Angeles Clippers", "blue"],
            "LAL":["Los Angeles Lakers", "yellow"],
            "MEM":["Memphis Grizzlies", "grey"],
            "MIA":["Miami Heat", "red"],
            "MIL":["Milwaukee Bucks", "green"],
            "MIN":["Minnesota Timberwolves", "blue"],
            "NOP":["New Orleans Pelicans", "gold"],
            "NYK":["New Yorks Knicks", "orange"],
            "OKC":["Oklahoma City Thunder", "orange"],
            "ORL":["Orlando Magic", "dark blue"],
            "PHI":["Philadelphia 76ers", "red"],
            "PHO":["Phoenix Suns", "orange"],
            "POR":["Portland Trailblazers", "red"],
            "SAC":["Sacramento Kings", "purple"],
            "SAS":["San Antonio Spurs", "black"],
            "TOR":["Toronto Raptors", "red"],
            "UTA":["Utah Jazz", "dark blue"],
            "WAS":["Washington Wizards", "red"]
        }
        self.label2_text.set(t[text][0])
        self.label2.configure(background=t[text][1])
        self.bannerh = tk.PhotoImage(file=b[text][0])
        self.homebanner.configure(image=self.bannerh)
        # self.logoh = tk.PhotoImage(file=b[text][1])
        # self.homelogo.configure(image=self.logoh)
        

    def pick_away(self):
        global awayid
        text = self.option2.get()
        awayid = text
        b: dict[str, list(str)] = {
            "BOS":["assets/banners/banner_bos.png","assets/logos/logo_bos.png"],
            "ATL":["assets/banners/banner_atl.png","assets/logos/logo_atl.png"],
            "BRK":["assets/banners/banner_brk.png","assets/logos/logo_brk.png"],
            "CHI":["assets/banners/banner_chi.png","assets/logos/logo_chi.png"],
            "CHO":["assets/banners/banner_cho.png","assets/logos/logo_cho.png"],
            "CLE":["assets/banners/banner_cle.png","assets/logos/logo_cle.png"],
            "DAL":["assets/banners/banner_dal.png","assets/logos/logo_dal.png"],
            "DEN":["assets/banners/banner_den.png","assets/logos/logo_den.png"],
            "DET":["assets/banners/banner_det.png","assets/logos/logo_det.png"],
            "GSW":["assets/banners/banner_gsw.png","assets/logos/logo_gsw.png"],
            "HOU":["assets/banners/banner_hou.png","assets/logos/logo_hou.png"],
            "IND":["assets/banners/banner_ind.png","assets/logos/logo_ind.png"],
            "LAC":["assets/banners/banner_lac.png","assets/logos/logo_lac.png"],
            "LAL":["assets/banners/banner_lal.png","assets/logos/logo_lal.png"],
            "MEM":["assets/banners/banner_mem.png","assets/logos/logo_mem.png"],
            "MIA":["assets/banners/banner_mia.png","assets/logos/logo_mia.png"],
            "MIL":["assets/banners/banner_mil.png","assets/logos/logo_mil.png"],
            "MIN":["assets/banners/banner_min.png","assets/logos/logo_min.png"],
            "NOP":["assets/banners/banner_nop.png","assets/logos/logo_nop.png"],
            "NYK":["assets/banners/banner_nyk.png","assets/logos/logo_nyk.png"],
            "OKC":["assets/banners/banner_okc.png","assets/logos/logo_okc.png"],
            "ORL":["assets/banners/banner_orl.png","assets/logos/logo_orl.png"],
            "PHI":["assets/banners/banner_phi.png","assets/logos/logo_phi.png"],
            "PHO":["assets/banners/banner_pho.png","assets/logos/logo_pho.png"],
            "POR":["assets/banners/banner_por.png","assets/logos/logo_por.png"],
            "SAC":["assets/banners/banner_sac.png","assets/logos/logo_sac.png"],
            "SAS":["assets/banners/banner_sas.png","assets/logos/logo_sas.png"],
            "TOR":["assets/banners/banner_tor.png","assets/logos/logo_tor.png"],
            "UTA":["assets/banners/banner_uta.png","assets/logos/logo_uta.png"],
            "WAS":["assets/banners/banner_was.png","assets/logos/logo_was.png"]
            }
        t: dict[str, list(str)] = {
            "ATL":["Atlanta Hawks", "red"],
            "BOS":["Boston Celtics", "green"],
            "BRK":["Brooklyn Nets", "black"],
            "CHI":["Chicago Bulls", "red"],
            "CHO":["Charlotte Hornets", "light blue"],
            "CLE":["Cleveland Cavaliers", "yellow"],
            "DAL":["Dallas Mavericks", "dark blue"],
            "DEN":["Denver Nuggets", "yellow"],
            "DET":["Detroit Pistons", "red"],
            "GSW":["Golden St Warriors", "yellow"],
            "HOU":["Houston Rockets", "red"],
            "IND":["Indiana Pacers", "dark blue"],
            "LAC":["Los Angeles Clippers", "blue"],
            "LAL":["Los Angeles Lakers", "yellow"],
            "MEM":["Memphis Grizzlies", "grey"],
            "MIA":["Miami Heat", "red"],
            "MIL":["Milwaukee Bucks", "green"],
            "MIN":["Minnesota Timberwolves", "blue"],
            "NOP":["New Orleans Pelicans", "gold"],
            "NYK":["New Yorks Knicks", "orange"],
            "OKC":["Oklahoma City Thunder", "orange"],
            "ORL":["Orlando Magic", "dark blue"],
            "PHI":["Philadelphia 76ers", "red"],
            "PHO":["Phoenix Suns", "orange"],
            "POR":["Portland Trailblazers", "red"],
            "SAC":["Sacramento Kings", "purple"],
            "SAS":["San Antonio Spurs", "black"],
            "TOR":["Toronto Raptors", "red"],
            "UTA":["Utah Jazz", "dark blue"],
            "WAS":["Washington Wizards", "red"]
        }
        self.label3_text.set(t[text][0])
        self.label3.configure(background=t[text][1])
        self.bannera = tk.PhotoImage(file=b[text][0])
        self.awaybanner.configure(image=self.bannera)
        # self.logoa = tk.PhotoImage(file=b[text][1])
        # self.awaylogo.configure(image=self.logoa)
    
    
    def runsim(self):
        global home_roster, away_roster, homeid, awayid
        initiate(homeid, awayid)
        match(home_roster, away_roster)
        texta = str(away_score)
        self.scorea_value.set(texta)
        texth = str(home_score)
        self.scoreh_value.set(texth)
        stat1 = str(away_roster[2].stat_rep())
        self.label4_text.set(stat1)


root = tk.Tk()
MyWindow(root)
root.mainloop()