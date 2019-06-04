import random


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    GREEN = '\033[96m'
    WARNING = '\033[31m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Enemy:
    def __init__(self, name, hp, mp, atk, df, magic, items):
        self.hp = hp
        self.mp = mp
        self.maxhp = hp
        self.maxmp = mp
        self.atk = atk
        self.atkh = atk+20
        self.atkl = atk-20
        self.df = df
        self.magic = magic
        self.actions = ['Attack', 'Magic', 'Use Item']
        self.items = items
        self.name = name

    def generate_damage(self):
        return random.randrange(self.atkl, self.atkh)

    def take_dmg(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp

    def get_hp(self):
        return self.hp

    def get_maxhp(self):
        return self.maxhp

    def get_maxmp(self):
        return self.maxmp

    def get_mp(self):
        return self.mp

    def reduce_mp(self, cost):
        self.mp -= cost

    def get_spell_name(self, i):
        return self.magic[i]['name']

    def get_spell_cost(self, i):
        return self.magic[i]['cost']

    def choose_action(self):
        i = 1
        print('Choose Actions')
        for item in self.actions:
            print(str(i) + '.' + item)
            i += 1

    def choose_spell(self):
        i = 1
        print(bcolors.WARNING + 'SPELLS AND COSTS' + bcolors.ENDC)
        print(bcolors.OKGREEN + '\tAvailable MP: ' + str(self.mp) + bcolors.ENDC)
        for spell in self.magic:
            print('\t' + str(i) + '.' + spell.name + '(Cost:' + str(spell.cost) + ')')
            i += 1

    def heal(self, healpts):
        self.hp += healpts
        if self.hp > self.maxhp:
            self.hp = self.maxhp
        return self.hp

    def choose_item(self):
        i = 1
        print(bcolors.WARNING + '\tITEMS LIST' + bcolors.ENDC)
        for item in self.items:
            print('\t' + str(i) + '.' + item.name + ' - ' + item.desc + "(x" + str(item.qty) + ')')
            i += 1

    def heal_mp(self, healpts):
        self.mp += healpts
        if self.mp > self.maxmp:
            self.mp = self.maxmp
        return self.mp

    def print_stats(self):
        temp1 = (self.hp/self.maxhp) * 100
        temp1 = int(temp1//5)
        str1 = bcolors.WARNING + self.name + bcolors.ENDC
        if len(self.name) < 12:
            diff = 12 - len(self.name)
            for i in range(diff+1):
                str1 += ' '
        str1 += bcolors.OKGREEN + '' + str(self.hp) + '/' + str(self.maxhp) + ' |'
        for i in range(temp1):
            str1 += '/'
        temp2 = 20 - temp1
        for j in range(temp2):
            str1 += ' '
        str1 += ' |' + bcolors.ENDC
        temp1 = (self.mp/self.maxmp) * 100
        temp1 = int(temp1//10)
        str2 = bcolors.GREEN + str(self.mp) + '/' + str(self.maxmp) + ' |'
        for i in range(temp1):
            str2 += '/'
        temp2 = 10 - temp1
        for j in range(temp2+1):
            str2 += ' '
        str2 += '|' + bcolors.ENDC
        print(str1+'     '+str2)
    # def print_stats(self):
