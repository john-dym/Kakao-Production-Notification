from random import randint, choice
from breezypythongui import EasyFrame # Reference at http://kennethalambert.com/breezypythongui/quickref.html
import time

part_names = ['TM1', 'TM2', 'TM3', 'TM4']
parts_per_minute = 1200
start_part_no = randint(1000, 100000)
MULTIPLES = 50  # Transmissions per line, Usually 30 mins worth of production
MIN_RUN_QTY = 1600

class prod_sim_GUI(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, background="#ff91be")
        self.addLabel("TIME", 0, 0, sticky="NWSE", background="#2eff9d")
        self.addLabel("Production Planning", 0, 1, 7, sticky="NWSE", background="#2eff9d")
        self.addLabel("Model", 1, 0, rowspan=2, sticky="NWSE", background="#2eff9d")
        self.addLabel("Start No", 1, 1, rowspan=2, sticky="NWSE", background="#2eff9d")
        self.addLabel("Input", 1, 2, columnspan=2, sticky="NWSE", background="#2eff9d")
        self.addLabel("Plan", 2, 2, sticky="NWSE", background="#2eff9d")
        self.addLabel("Act", 2, 3, sticky="NWSE", background="#2eff9d")
        self.addLabel("Model", 1, 4, rowspan=2, sticky="NWSE", background="#2eff9d")
        self.addLabel("Start No", 1, 5, rowspan=2, sticky="NWSE", background="#2eff9d")
        self.addLabel("Input", 1, 6, columnspan=2, sticky="NWSE", background="#2eff9d")
        self.addLabel("Plan", 2, 6, sticky="NWSE", background="#2eff9d")
        self.addLabel("Act", 2, 7, sticky="NWSE", background="#2eff9d")
        self.addButton("prod_run", 0, 8, command=self.production_run)
        # Left side of GUI
        self.TM_line_11 = self.addLabel("TM1", 4, 0, sticky="NWSE", background="#2eff9d")
        self.TM_line_12 = self.addLabel("000001", 4, 1, sticky="NWSE", background="#2eff9d")
        self.TM_line_13 = self.addLabel("50", 4, 2, sticky="NSE", background="#2eff9d")
        self.TM_line_14 = self.addLabel("50", 4, 3, sticky="NSE", background="#2eff9d")

        self.TM_line_21 = self.addLabel("TM1", 5, 0, sticky="NWSE", background="#2eff9d")
        self.TM_line_22 = self.addLabel("000001", 5, 1, sticky="NWSE", background="#2eff9d")
        self.TM_line_23 = self.addLabel("0", 5, 2, sticky="NSE", background="#2eff9d")
        self.TM_line_24 = self.addLabel("50", 5, 3, sticky="NSE", background="#2eff9d")

        self.TM_line_31 = self.addLabel("TM1", 6, 0, sticky="NWSE", background="#2eff9d")
        self.TM_line_32 = self.addLabel("000001", 6, 1, sticky="NWSE", background="#2eff9d")
        self.TM_line_33 = self.addLabel("0", 6, 2, sticky="NSE", background="#2eff9d")
        self.TM_line_34 = self.addLabel("50", 6, 3, sticky="NSE", background="#2eff9d")

        self.TM_line_41 = self.addLabel("TM1", 7, 0, sticky="NWSE", background="#2eff9d")
        self.TM_line_42 = self.addLabel("000001", 7, 1, sticky="NWSE", background="#2eff9d")
        self.TM_line_43 = self.addLabel("0", 7, 2, sticky="NSE", background="#2eff9d")
        self.TM_line_44 = self.addLabel("50", 7, 3, sticky="NSE", background="#2eff9d")

        self.TM_line_51 = self.addLabel("TM1", 8, 0, sticky="NWSE", background="#2eff9d")
        self.TM_line_52 = self.addLabel("000001", 8, 1, sticky="NWSE", background="#2eff9d")
        self.TM_line_53 = self.addLabel("0", 8, 2, sticky="NSE", background="#2eff9d")
        self.TM_line_54 = self.addLabel("50", 8, 3, sticky="NSE", background="#2eff9d")

        self.TM_line_61 = self.addLabel("TM1", 9, 0, sticky="NWSE", background="#2eff9d")
        self.TM_line_62 = self.addLabel("000001", 9, 1, sticky="NWSE", background="#2eff9d")
        self.TM_line_63 = self.addLabel("0", 9, 2, sticky="NSE", background="#2eff9d")
        self.TM_line_64 = self.addLabel("50", 9, 3, sticky="NSE", background="#2eff9d")

        self.TM_line_71 = self.addLabel("TM1",10, 0, sticky="NWSE", background="#2eff9d")
        self.TM_line_72 = self.addLabel("000001",10, 1, sticky="NWSE", background="#2eff9d")
        self.TM_line_73 = self.addLabel("0",10, 2, sticky="NSE", background="#2eff9d")
        self.TM_line_74 = self.addLabel("50",10, 3, sticky="NSE", background="#2eff9d")

        self.TM_line_81 = self.addLabel("TM1",11, 0, sticky="NWSE", background="#2eff9d")
        self.TM_line_82 = self.addLabel("000001",11, 1, sticky="NWSE", background="#2eff9d")
        self.TM_line_83 = self.addLabel("0",11, 2, sticky="NSE", background="#2eff9d")
        self.TM_line_84 = self.addLabel("50",11, 3, sticky="NSE", background="#2eff9d")

        self.TM_line_91 = self.addLabel("TM1",12, 0, sticky="NWSE", background="#2eff9d")
        self.TM_line_92 = self.addLabel("000001",12, 1, sticky="NWSE", background="#2eff9d")
        self.TM_line_93 = self.addLabel("0",12, 2, sticky="NSE", background="#2eff9d")
        self.TM_line_94 = self.addLabel("50",12, 3, sticky="NSE", background="#2eff9d")

        self.TM_line_101 = self.addLabel("TM1",13, 0, sticky="NWSE", background="#2eff9d")
        self.TM_line_102 = self.addLabel("000001",13, 1, sticky="NWSE", background="#2eff9d")
        self.TM_line_103 = self.addLabel("0",13, 2, sticky="NSE", background="#2eff9d")
        self.TM_line_104 = self.addLabel("50",13, 3, sticky="NSE", background="#2eff9d")
        #Right side of GUI
        self.TM_line_111 = self.addLabel("TM1", 4, 4, sticky="NWSE", background="#2eff9d")
        self.TM_line_112 = self.addLabel("000001", 4, 5, sticky="NWSE", background="#2eff9d")
        self.TM_line_113 = self.addLabel("0", 4, 6, sticky="NSE", background="#2eff9d")
        self.TM_line_114 = self.addLabel("50", 4, 7, sticky="NSE", background="#2eff9d")

        self.TM_line_121 = self.addLabel("TM1", 5, 4, sticky="NWSE", background="#2eff9d")
        self.TM_line_122 = self.addLabel("000001", 5, 5, sticky="NWSE", background="#2eff9d")
        self.TM_line_123 = self.addLabel("0", 5, 6, sticky="NSE", background="#2eff9d")
        self.TM_line_124 = self.addLabel("50", 5, 7, sticky="NSE", background="#2eff9d")

        self.TM_line_131 = self.addLabel("TM1", 6, 4, sticky="NWSE", background="#2eff9d")
        self.TM_line_132 = self.addLabel("000001", 6, 5, sticky="NWSE", background="#2eff9d")
        self.TM_line_133 = self.addLabel("0", 6, 6, sticky="NSE", background="#2eff9d")
        self.TM_line_134 = self.addLabel("50", 6, 7, sticky="NSE", background="#2eff9d")

        self.TM_line_141 = self.addLabel("TM1", 7, 4, sticky="NWSE", background="#2eff9d")
        self.TM_line_142 = self.addLabel("000001", 7, 5, sticky="NWSE", background="#2eff9d")
        self.TM_line_143 = self.addLabel("0", 7, 6, sticky="NSE", background="#2eff9d")
        self.TM_line_144 = self.addLabel("50", 7, 7, sticky="NSE", background="#2eff9d")

        self.TM_line_151 = self.addLabel("TM1", 8, 4, sticky="NWSE", background="#2eff9d")
        self.TM_line_152 = self.addLabel("000001", 8, 5, sticky="NWSE", background="#2eff9d")
        self.TM_line_153 = self.addLabel("0", 8, 6, sticky="NSE", background="#2eff9d")
        self.TM_line_154 = self.addLabel("50", 8, 7, sticky="NSE", background="#2eff9d")

        self.TM_line_161 = self.addLabel("TM1", 9, 4, sticky="NWSE", background="#2eff9d")
        self.TM_line_162 = self.addLabel("000001", 9, 5, sticky="NWSE", background="#2eff9d")
        self.TM_line_163 = self.addLabel("0", 9, 6, sticky="NSE", background="#2eff9d")
        self.TM_line_164 = self.addLabel("50", 9, 7, sticky="NSE", background="#2eff9d")

        self.TM_line_171 = self.addLabel("TM1", 10, 4, sticky="NWSE", background="#2eff9d")
        self.TM_line_172 = self.addLabel("000001", 10, 5, sticky="NWSE", background="#2eff9d")
        self.TM_line_173 = self.addLabel("0", 10, 6, sticky="NSE", background="#2eff9d")
        self.TM_line_174 = self.addLabel("50", 10, 7, sticky="NSE", background="#2eff9d")

        self.TM_line_181 = self.addLabel("TM1", 11, 4, sticky="NWSE", background="#2eff9d")
        self.TM_line_182 = self.addLabel("000001", 11, 5, sticky="NWSE", background="#2eff9d")
        self.TM_line_183 = self.addLabel("0", 11, 6, sticky="NSE", background="#2eff9d")
        self.TM_line_184 = self.addLabel("50", 11, 7, sticky="NSE", background="#2eff9d")

        self.TM_line_191 = self.addLabel("TM1", 12, 4, sticky="NWSE", background="#2eff9d")
        self.TM_line_192 = self.addLabel("000001", 12, 5, sticky="NWSE", background="#2eff9d")
        self.TM_line_193 = self.addLabel("0", 12, 6, sticky="NSE", background="#2eff9d")
        self.TM_line_194 = self.addLabel("50", 12, 7, sticky="NSE", background="#2eff9d")

        self.TM_line_201 = self.addLabel("TM1", 13, 4, sticky="NWSE", background="#2eff9d")
        self.TM_line_202 = self.addLabel("000001", 13, 5, sticky="NWSE", background="#2eff9d")
        self.TM_line_203 = self.addLabel("0", 13, 6, sticky="NSE", background="#2eff9d")
        self.TM_line_204 = self.addLabel("50", 13, 7, sticky="NSE", background="#2eff9d")

    def production_run(self):
        prod_list = prod_to_list(rand_prod_sched(MIN_RUN_QTY))
        # gui_labels = [["self.TM_line_11", "self.TM_line_12", "self.TM_line_13", "self.TM_line_14"],["self.TM_line_21", "self.TM_line_22", "self.TM_line_23", "self.TM_line_24"],["self.TM_line_31", "self.TM_line_32", "self.TM_line_33", "self.TM_line_34"],["self.TM_line_41", "self.TM_line_42", "self.TM_line_43", "self.TM_line_44"],["self.TM_line_51", "self.TM_line_52", "self.TM_line_53", "self.TM_line_54"],["self.TM_line_61", "self.TM_line_62", "self.TM_line_63", "self.TM_line_64"],["self.TM_line_71", "self.TM_line_72", "self.TM_line_73", "self.TM_line_74"],["self.TM_line_81", "self.TM_line_82", "self.TM_line_83", "self.TM_line_84"],["self.TM_line_91", "self.TM_line_92", "self.TM_line_93", "self.TM_line_94"],["self.TM_line_101", "self.TM_line_102", "self.TM_line_103", "self.TM_line_104"],["self.TM_line_111", "self.TM_line_112", "self.TM_line_113", "self.TM_line_114"],["self.TM_line_121", "self.TM_line_122", "self.TM_line_123", "self.TM_line_124"],["self.TM_line_131", "self.TM_line_132", "self.TM_line_133", "self.TM_line_134"],["self.TM_line_141", "self.TM_line_142", "self.TM_line_143", "self.TM_line_144"],["self.TM_line_151", "self.TM_line_152", "self.TM_line_153", "self.TM_line_154"],["self.TM_line_161", "self.TM_line_162", "self.TM_line_163", "self.TM_line_164"],["self.TM_line_171", "self.TM_line_172", "self.TM_line_173", "self.TM_line_174"],["self.TM_line_181", "self.TM_line_182", "self.TM_line_183", "self.TM_line_184"],["self.TM_line_191", "self.TM_line_192", "self.TM_line_193", "self.TM_line_194"],["self.TM_line_201", "self.TM_line_202", "self.TM_line_203", "self.TM_line_204"]]
        while len(prod_list) > 1:
            prod_run(prod_list)
            if len(prod_list) > 0:
                self.TM_line_11["text"] = prod_list[0][0]
                self.TM_line_12["text"] = prod_list[0][1]
                self.TM_line_13["text"] = prod_list[0][2]
                self.TM_line_14["text"] = prod_list[0][3]
            else:
                self.TM_line_11["text"] = ""
                self.TM_line_12["text"] = ""
                self.TM_line_13["text"] = ""
                self.TM_line_14["text"] = ""

            if len(prod_list) > 1:
                self.TM_line_21["text"] = prod_list[1][0]
                self.TM_line_22["text"] = prod_list[1][1]
                self.TM_line_23["text"] = prod_list[1][2]
                self.TM_line_24["text"] = prod_list[1][3]
            else:
                self.TM_line_21["text"] = ""
                self.TM_line_22["text"] = ""
                self.TM_line_23["text"] = ""
                self.TM_line_24["text"] = ""

            if len(prod_list) > 2:
                self.TM_line_31["text"] = prod_list[2][0]
                self.TM_line_32["text"] = prod_list[2][1]
                self.TM_line_33["text"] = prod_list[2][2]
                self.TM_line_34["text"] = prod_list[2][3]
            else:
                self.TM_line_31["text"] = ""
                self.TM_line_32["text"] = ""
                self.TM_line_33["text"] = ""
                self.TM_line_34["text"] = ""

            if len(prod_list) > 3:
                self.TM_line_41["text"] = prod_list[3][0]
                self.TM_line_42["text"] = prod_list[3][1]
                self.TM_line_43["text"] = prod_list[3][2]
                self.TM_line_44["text"] = prod_list[3][3]
            else:
                self.TM_line_41["text"] = ""
                self.TM_line_42["text"] = ""
                self.TM_line_43["text"] = ""
                self.TM_line_44["text"] = ""

            if len(prod_list) > 4:
                self.TM_line_51["text"] = prod_list[4][0]
                self.TM_line_52["text"] = prod_list[4][1]
                self.TM_line_53["text"] = prod_list[4][2]
                self.TM_line_54["text"] = prod_list[4][3]
            else:
                self.TM_line_51["text"] = ""
                self.TM_line_52["text"] = ""
                self.TM_line_53["text"] = ""
                self.TM_line_54["text"] = ""

            if len(prod_list) > 5:
                self.TM_line_61["text"] = prod_list[5][0]
                self.TM_line_62["text"] = prod_list[5][1]
                self.TM_line_63["text"] = prod_list[5][2]
                self.TM_line_64["text"] = prod_list[5][3]
            else:
                self.TM_line_61["text"] = ""
                self.TM_line_62["text"] = ""
                self.TM_line_63["text"] = ""
                self.TM_line_64["text"] = ""

            if len(prod_list) > 6:
                self.TM_line_71["text"] = prod_list[6][0]
                self.TM_line_72["text"] = prod_list[6][1]
                self.TM_line_73["text"] = prod_list[6][2]
                self.TM_line_74["text"] = prod_list[6][3]
            else:
                self.TM_line_71["text"] = ""
                self.TM_line_72["text"] = ""
                self.TM_line_73["text"] = ""
                self.TM_line_74["text"] = ""

            if len(prod_list) > 7:
                self.TM_line_81["text"] = prod_list[7][0]
                self.TM_line_82["text"] = prod_list[7][1]
                self.TM_line_83["text"] = prod_list[7][2]
                self.TM_line_84["text"] = prod_list[7][3]
            else:
                self.TM_line_81["text"] = ""
                self.TM_line_82["text"] = ""
                self.TM_line_83["text"] = ""
                self.TM_line_84["text"] = ""

            if len(prod_list) > 8:
                self.TM_line_91["text"] = prod_list[8][0]
                self.TM_line_92["text"] = prod_list[8][1]
                self.TM_line_93["text"] = prod_list[8][2]
                self.TM_line_94["text"] = prod_list[8][3]
            else:
                self.TM_line_91["text"] = ""
                self.TM_line_92["text"] = ""
                self.TM_line_93["text"] = ""
                self.TM_line_94["text"] = ""

            if len(prod_list) > 9:
                self.TM_line_101["text"] = prod_list[9][0]
                self.TM_line_102["text"] = prod_list[9][1]
                self.TM_line_103["text"] = prod_list[9][2]
                self.TM_line_104["text"] = prod_list[9][3]
            else:
                self.TM_line_101["text"] = ""
                self.TM_line_102["text"] = ""
                self.TM_line_103["text"] = ""
                self.TM_line_104["text"] = ""

            if len(prod_list) > 10:
                self.TM_line_111["text"] = prod_list[10][0]
                self.TM_line_112["text"] = prod_list[10][1]
                self.TM_line_113["text"] = prod_list[10][2]
                self.TM_line_114["text"] = prod_list[10][3]
            else:
                self.TM_line_111["text"] = ""
                self.TM_line_112["text"] = ""
                self.TM_line_113["text"] = ""
                self.TM_line_114["text"] = ""

            if len(prod_list) > 11:
                self.TM_line_121["text"] = prod_list[11][0]
                self.TM_line_122["text"] = prod_list[11][1]
                self.TM_line_123["text"] = prod_list[11][2]
                self.TM_line_124["text"] = prod_list[11][3]
            else:
                self.TM_line_121["text"] = ""
                self.TM_line_122["text"] = ""
                self.TM_line_123["text"] = ""
                self.TM_line_124["text"] = ""

            if len(prod_list) > 12:
                self.TM_line_131["text"] = prod_list[12][0]
                self.TM_line_132["text"] = prod_list[12][1]
                self.TM_line_133["text"] = prod_list[12][2]
                self.TM_line_134["text"] = prod_list[12][3]
            else:
                self.TM_line_131["text"] = ""
                self.TM_line_132["text"] = ""
                self.TM_line_133["text"] = ""
                self.TM_line_134["text"] = ""

            if len(prod_list) > 13:
                self.TM_line_141["text"] = prod_list[13][0]
                self.TM_line_142["text"] = prod_list[13][1]
                self.TM_line_143["text"] = prod_list[13][2]
                self.TM_line_144["text"] = prod_list[13][3]
            else:
                self.TM_line_141["text"] = ""
                self.TM_line_142["text"] = ""
                self.TM_line_143["text"] = ""
                self.TM_line_144["text"] = ""

            if len(prod_list) > 14:
                self.TM_line_151["text"] = prod_list[14][0]
                self.TM_line_152["text"] = prod_list[14][1]
                self.TM_line_153["text"] = prod_list[14][2]
                self.TM_line_154["text"] = prod_list[14][3]
            else:
                self.TM_line_151["text"] = ""
                self.TM_line_152["text"] = ""
                self.TM_line_153["text"] = ""
                self.TM_line_154["text"] = ""

            if len(prod_list) > 15:
                self.TM_line_161["text"] = prod_list[15][0]
                self.TM_line_162["text"] = prod_list[15][1]
                self.TM_line_163["text"] = prod_list[15][2]
                self.TM_line_164["text"] = prod_list[15][3]
            else:
                self.TM_line_161["text"] = ""
                self.TM_line_162["text"] = ""
                self.TM_line_163["text"] = ""
                self.TM_line_164["text"] = ""

            if len(prod_list) > 16:
                self.TM_line_171["text"] = prod_list[16][0]
                self.TM_line_172["text"] = prod_list[16][1]
                self.TM_line_173["text"] = prod_list[16][2]
                self.TM_line_174["text"] = prod_list[16][3]
            else:
                self.TM_line_171["text"] = ""
                self.TM_line_172["text"] = ""
                self.TM_line_173["text"] = ""
                self.TM_line_174["text"] = ""

            if len(prod_list) > 17:
                self.TM_line_181["text"] = prod_list[17][0]
                self.TM_line_182["text"] = prod_list[17][1]
                self.TM_line_183["text"] = prod_list[17][2]
                self.TM_line_184["text"] = prod_list[17][3]
            else:
                self.TM_line_181["text"] = ""
                self.TM_line_182["text"] = ""
                self.TM_line_183["text"] = ""
                self.TM_line_184["text"] = ""

            if len(prod_list) > 18:
                self.TM_line_191["text"] = prod_list[18][0]
                self.TM_line_192["text"] = prod_list[18][1]
                self.TM_line_193["text"] = prod_list[18][2]
                self.TM_line_194["text"] = prod_list[18][3]
            else:
                self.TM_line_191["text"] = ""
                self.TM_line_192["text"] = ""
                self.TM_line_193["text"] = ""
                self.TM_line_194["text"] = ""

            if len(prod_list) > 19:
                self.TM_line_201["text"] = prod_list[19][0]
                self.TM_line_202["text"] = prod_list[19][1]
                self.TM_line_203["text"] = prod_list[19][2]
                self.TM_line_204["text"] = prod_list[19][3]
            else:
                self.TM_line_201["text"] = ""
                self.TM_line_202["text"] = ""
                self.TM_line_203["text"] = ""
                self.TM_line_204["text"] = ""

            AHK_file_output(prod_list)
            self.update()
        pass

def debug(var):
    print(var)

# Creates a random production schedule
def rand_prod_sched(min_run_qty):
    sum_prod = 0
    rand_part = ''
    prod_schedule = []
    while sum_prod < min_run_qty:
        rand_qty = MULTIPLES * randint(1,10)
        try:
            while rand_part == prod_schedule[len(prod_schedule) - 1][0]:
                rand_part = choice(part_names)
        except:
            rand_part = choice(part_names)
        prod_schedule.append([rand_part, rand_qty])
        sum_prod += rand_qty
    return prod_schedule

# Converts random production schedule into a list in multiples of MULTPILES in form [tm_name, qty_ran, planned_qty]
def prod_to_list(prod_sched):
    lyst = [["", "", "", ""]]
    tm_number = start_part_no
    for x in prod_sched:
        prod_qty_multiples = x[1] // MULTIPLES
        for lyst_app in range(prod_qty_multiples):
            lyst.append([x[0], tm_number, 0, MULTIPLES])
            tm_number += MULTIPLES
    return lyst

# Runs the prod schedule one part at a time.
def prod_run(prod_list):
    parts_per_sec = parts_per_minute / 60
    # while len(prod_list) > 1:
    if prod_list[1][2] == prod_list[1][3]:
        prod_list.pop(0)
        if len(prod_list) > 1:
            prod_list[1][2] += 1
    else:
        prod_list[1][2] += 1
    time.sleep(1 / parts_per_sec)

# Simulates AutoHotKey output the production screen data to a .txt file to be parsed by the actual notification program
def AHK_file_output(prod_list):
    txt_output = ""
    if len(prod_list) > 20:
        prod_list_length = 20
    else:
        prod_list_length = len(prod_list)
    for x in range(prod_list_length):
        for y in range(4):
            txt_output += str(prod_list[x][y]) + ", "
        txt_output = txt_output[:-2]
        txt_output += "\n"
    f = open("production.txt", "w")
    f.write(txt_output)
    f.close()


def main():
    test = prod_sim_GUI().mainloop()

if __name__ == "__main__":
    main()
